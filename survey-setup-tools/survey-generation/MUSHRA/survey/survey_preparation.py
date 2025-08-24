"""
Cisco Systems, Inc. and its affiliates
"""
"""
MUSHRA survey preparation utilities
"""

from collections import defaultdict
import os
import pandas as pd
import random

from template_helpers.mushra_questions import (
    create_testing_question,
    create_training_choice_template,
    create_training_text_question,
    create_passive_training_question,
    create_dynamic_training_question,
)

from template_helpers.mushra_blocks import (
    create_new_testing_block,
    create_new_dynamic_training_block,
    create_new_flow_block,
    create_new_dynamic_training_flow_block,
    create_hearing_test_block,
)

from qualtrics_utils.survey_components import (
    get_number_of_survey_components,
    get_survey_component_index_map,
)

from qualtrics_utils.survey_questions import (
    get_current_number_of_questions,
    update_survey_number_of_questions,
    insert_question_referecences_on_block,
)

from qualtrics_utils.survey_constants import (
    QUESTION_ID_PREFIX,
)
from qualtrics_utils.survey_metadata import (
    get_survey_id,
    generate_qualtrics_block_id,
)
from qualtrics_utils.survey_payload_elements import (
    get_survey_block_element_payload_map,
    insert_new_survey_block_element_payload,
)
from qualtrics_utils.survey_flow import (
    get_survey_flow_index_map,
    get_survey_flow_index_by_block_id,
)

def sample_hearing_test_files(hearing_test_files):
    """Sample hearing test files based on easy, medium and hard conditions.
    The hearing test files are classified in easy, medium, and hard. The
    hearing test consists in 6 files, 2 per category.

    Args:
        hearing_test_files (dict):
        Dictionary category -> [{resource_link -> "filepath", digits -> "123"}]

    return
        list (resource_link, digit)
    """
    hearing_test_samples = []
    for category in hearing_test_files:
        items = hearing_test_files[category]
        sampled_items = random.sample(items, 2)
        for item in sampled_items:
            hearing_test_samples.append((item["resource_link"], item["digits"]))

    return hearing_test_samples

def remove_block_from_flow(block_name_description, survey_data):
    """Remove a block from the flow
    There are sections of the survey that can be set as optional.
    For these cases, this method can be called to remove the block
    from the flow of the survey.

    Args:
        block_name_description (str): Name of the block in the survey.
        survey_data (dict): survey QSF file.

    Returns:
        survey data (dict): Updated survey data
    """
    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Get the block element index
    block_element_payload_index_map = get_survey_block_element_payload_map(survey_data)
    block_index = block_element_payload_index_map[block_name_description]

    # Get passive training block ID
    block_id = survey_data["SurveyElements"][
        component_index_survey_map["Survey Blocks"]
    ]["Payload"][block_index]["ID"]

    # Find the index in the flow with the block id of the passive training section
    target_index = get_survey_flow_index_by_block_id(survey_data, block_id)

    # Remove by index
    survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]]["Payload"][
        "Flow"
    ].pop(target_index)

    return survey_data


def prepare_survey_quotas(testing_df, qualtrics_conf, conditions):
    """Prepare survey quotas.
    Prepare survey using qualtrics_conf quota parameters for validation and testing.

    Args:
        testing_df (pd.DataFrame): testing dataset  (survey_input_metafile)
        qualtrics_conf (json): json qualtrics configuration file (qualtrics_qsf_conf)

    Returns:
        tuple: (training data dataframe, survey block dictionary block: testing+validation dataframe)
    """
    assert len(testing_df) > 0
    MAX_NUMBER_OF_AUDIO_FILES_PER_QUESTION = 25

    seed = qualtrics_conf["seed"]
    number_of_blocks = qualtrics_conf["blocks"]["number_of_blocks"]
    number_of_questions_per_block = qualtrics_conf["blocks"][
        "number_of_questions_per_block"
    ]
    number_of_conditions = len(conditions)

    # Default value for questions per block
    if number_of_blocks is None and number_of_questions_per_block is None:
        number_of_questions_per_block = (
            MAX_NUMBER_OF_AUDIO_FILES_PER_QUESTION // number_of_conditions
        )

    if number_of_questions_per_block is None and (not number_of_blocks is None):
        number_of_questions_per_block = len(testing_df) // number_of_blocks

    #####################################
    # PART 1: Assign blocks to testing df
    #####################################
    testing_df["block"] = None
    current_block_index = 1
    for index, _ in testing_df.iterrows():
        # Assign index
        testing_df.at[index, "block"] = current_block_index

        # Update block index according to the max number of questions
        # (advance counter when quota is reached)
        if (index + 1) % number_of_questions_per_block == 0:
            current_block_index += 1

    ###########################################
    # PART 2: Ensure mostly uniform block sizes
    ###########################################
    # Get the number of files in the last block
    last_block_size = len(testing_df[testing_df["block"] == current_block_index])

    # Double check:
    # The final block key was never used
    # (current_block_index was advanced after finishing last row in df)
    # Action: reset current_block_index to previous block index
    if last_block_size == 0:
        current_block_index -= 1
        last_block_size = len(testing_df[testing_df["block"] == current_block_index])

    # CASE 1:
    # The len of the final block is equal to the len of other blocks
    if last_block_size == number_of_questions_per_block:
        print("Block distribution is even - no adjustments needed")

    # CASE 2 + 3:
    # last_block_size < number_of_questions_per_block
    else:
        # Get unique blocks:
        # This is the list of "complete" blocks (i.e. everything before the last block)
        # which are definitely uniform in size (while the last one might have fewer questions).
        # The next steps produce a (more) uniform distribution if last block does not match in size
        unique_complete_blocks = list(
            testing_df[testing_df["block"] != current_block_index].block.unique()
        )

        # If the number of unique complete blocks
        # is smaller than the number of files in the last block
        #       e.g.:
        #       len(unique_complete_blocks) == 10 blocks
        #       last_block_size == 12 questions
        # then we multiply the list of unique_complete_blocks block IDs
        # so that the sequence of unique_complete_blocks block IDs repeats {last_block_size} times
        # --> this will facilitate redistributing questions from final block to other blocks
        #
        # NOTE this should be a very rare case -
        # usually there will be 5-6 conditions and the default MAX_NUMBER_OF_AUDIO_FILES_PER_QUESTION == 25
        # so default number of questions will be 4 or 5:
        #       MAX_NUMBER_OF_AUDIO_FILES_PER_QUESTION // 5 == 5
        #       MAX_NUMBER_OF_AUDIO_FILES_PER_QUESTION // 6 == 4
        if len(unique_complete_blocks) < last_block_size:
            unique_complete_blocks = unique_complete_blocks * last_block_size

        # CASE 2:
        # Last block < half len of other blocks
        # Action: Distribute last block among other files
        if last_block_size < number_of_questions_per_block // 2:
            print(
                f"Block {current_block_index} questions will be redistributed to other blocks"
            )
            for index, selected_block in zip(
                # indices of questions in last block
                testing_df[testing_df["block"] == current_block_index].index,
                # iterate through other block IDs
                unique_complete_blocks[0:last_block_size],
            ):
                # reassign selected question index to other block
                testing_df.at[index, "block"] = selected_block

        # CASE 3:
        # Last block > half len of other blocks (but number of questions is not reached)
        # Action: randomly re-assign questions from the dataset to supplement small final block
        elif (
            last_block_size > number_of_questions_per_block // 2
            and last_block_size < number_of_questions_per_block
        ):
            # number of questions missing
            fill_number = number_of_questions_per_block - last_block_size

            # question block of size N-1 is allowed;
            # if just 1 Q is missing, do nothing
            if fill_number == 1:
                print(
                    f"Block {current_block_index} contains N-1 questions (no resampling from other blocks needed)"
                )

            else:
                for index in range(0, fill_number):
                    print(
                        f"Block {current_block_index} will be supplemented by reassigning questions from other blocks"
                    )

                    # randomly sample a question index from another block
                    question_to_reassign = testing_df[
                        testing_df["block"] != current_block_index
                    ].sample(1)
                    question_to_reassign_index = question_to_reassign.index[0]
                    testing_df.at[
                        question_to_reassign_index, "block"
                    ] = current_block_index

    # for testing:
    """
    for block in testing_df.block.unique():
        print('block', block)
        print('size', len(testing_df.loc[testing_df.block==block]))
    """
    # mapping block -> testing dataframe
    survey_data_mapping = {}
    for block_number in testing_df.block.unique():
        # Get current testing df block
        df_testing_block = testing_df[testing_df.block == block_number]

        # Assign dataset type
        df_testing_block = df_testing_block.assign(dataset_type="testing")

        # Randomize and save
        survey_data_mapping[block_number] = df_testing_block.sample(
            frac=1, random_state=seed
        )

    return survey_data_mapping



def prepare_dynamic_training_questions(
    training_condition_links,
    survey_data,
):
    """Prepare dynamic training questions.
    These are questions presented to the user for listening and rate.
    They have a format identical to the questions in the rating job.

    Args:
        training_condition_links (dict): Dictionary of samples -> (link,score)
        survey_data (JSON): Survey QSF data.

    Returns:
        pd.DataFrame
    """

    # Extract indexes and create a DataFrame
    samples = [item for item in training_condition_links.keys()]
    training_df = pd.DataFrame(samples, columns=["sample_index"])

    training_df["training_question_template"] = None
    training_df["QID"] = None
    training_df["qualtrics_component_index"] = None
    training_df["export_tag"] = None

    # Get survey_id
    SURVEY_ID = get_survey_id(survey_data=survey_data)

    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )
    current_number_of_components = get_number_of_survey_components(survey_data) + 1

    condition_index_mapping = {}
    # Compute metadata
    for index, row in training_df.iterrows():
        # Set question_id
        question_id = QUESTION_ID_PREFIX + str(current_number_of_questions)
        training_df.at[index, "QID"] = question_id

        # condition -> link mapping
        current_question_links = training_condition_links[row["sample_index"]]

        # Set export tag
        export_tag = "Q" + str(current_number_of_questions)
        training_df.at[index, "export_tag"] = export_tag

        # Set component id
        qualtrics_component_index = current_number_of_components
        training_df.at[index, "qualtrics_component_index"] = qualtrics_component_index

        # Create new testing question
        new_training_question, condition_mapping = create_dynamic_training_question(
            surveyID=SURVEY_ID,
            export_tag=export_tag,
            question_id=question_id,
            conditions_link_map=current_question_links,
        )

        condition_index_mapping[export_tag] = condition_mapping

        training_df.at[index, "training_question_template"] = new_training_question

        current_number_of_questions += 1
        current_number_of_components += 1

    return training_df, condition_index_mapping


def prepare_testing_questions(
    testing_df,
    survey_data,
    target_question,
):
    """Prepare testing (main task) questions.
    These are the questions of the blocks in the MUSHRA survey.

    Args:
        testing_df (pd.DataFrame): training block dataframe questions.
        survey_data (JSON): Survey QSF data.
        target_question (str): target question of the survey.
    Returns:
        pd.DataFrame
    """
    testing_df["testing_question_template"] = None
    testing_df["QID"] = None
    testing_df["qualtrics_component_index"] = None
    testing_df["is_validation"] = None
    testing_df["export_tag"] = None

    # Get survey_id
    SURVEY_ID = get_survey_id(survey_data=survey_data)

    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )
    current_number_of_components = get_number_of_survey_components(survey_data) + 1

    # Create map between conditon and condition column name in the dataframe
    condition_columns = [
        column for column in testing_df.columns.tolist() if "link" in column
    ]
    condition_columns_map = {
        item.split("_condition_")[0]: item for item in condition_columns
    }

    condition_index_mapping = {}

    # Compute metadata
    for index, row in testing_df.iterrows():
        # Get block id
        block_id = row["block"]

        # Set question_id
        question_id = QUESTION_ID_PREFIX + str(current_number_of_questions)
        testing_df.at[index, "QID"] = question_id

        # condition -> link mapping
        current_question_links = {}
        for condition, condition_column in condition_columns_map.items():
            current_question_links[condition] = row[condition_column]

        # Set export tag
        export_tag = "Q" + str(current_number_of_questions)
        testing_df.at[index, "export_tag"] = export_tag

        # Set component id
        qualtrics_component_index = current_number_of_components
        testing_df.at[index, "qualtrics_component_index"] = qualtrics_component_index

        # # Create new testing question
        new_testing_question, condition_mapping = create_testing_question(
            surveyID=SURVEY_ID,
            export_tag=export_tag,
            question_id=question_id,
            block_id=block_id,
            show_reference_in_header=True,
            target_question=target_question,
            conditions_link_map=current_question_links,
        )

        condition_index_mapping[export_tag] = condition_mapping

        testing_df.at[index, "testing_question_template"] = new_testing_question

        current_number_of_questions += 1
        current_number_of_components += 1

    return testing_df, condition_index_mapping

def update_survey_hearing_test_block(survey_data, hearing_test_options):
    """Update survey hearing test block.
    Update the audio links for the hearing test based on the hearing_test_options
    Args:
        survey_data (JSON): Survey QSF data.
        hearing_test_options(dict): {option: link, digits}.
    Return:
        survey_data (JSON): Updated Survey.
    """
    SURVEY_HEARING_TEST_COMPONENT_ID = "QID54"

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)
    hearing_test_component_index = component_index_survey_map[
        SURVEY_HEARING_TEST_COMPONENT_ID
    ]
    new_hearing_test_block = create_hearing_test_block(hearing_test_options)
    survey_data["SurveyElements"][hearing_test_component_index] = new_hearing_test_block

    return survey_data


def update_survey_testing_questions(survey_data, testing_df):
    """Update survey testing questions.
    Update/Chage the number of questions and **blocks** of the testingBlock of the survey.
    The testing questions are divided by blocks, each block has N questions.

    Args:
        survey_data (JSON): Survey QSF data.
        testing_df (pd.DataFrame):

    Returns:
        survey_data (JSON):  Updated Survey QSF data.
    """
    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Update current number of question according to the size of the dataframe.
    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )

    current_number_of_questions += len(testing_df)

    # Update survey data
    for block_number in testing_df.block.unique():
        # Get the target block
        current_testing_block_df = testing_df[testing_df.block == block_number]

        # TODO maybe iterate through unique comp IDs/testing q's instead?
        for index, row in current_testing_block_df.iterrows():
            # TODO but here we are iterating for each row

            # Component id
            qualtrics_component_index = row["qualtrics_component_index"]

            # Question
            testing_question = row["testing_question_template"]

            # if surveyElement already exists, update.
            # TODO there is an inefficiency here
            # where identical questions will replace themselves due to meta restructure
            # needs to be resolved for efficiency but is functional
            if qualtrics_component_index < len(survey_data["SurveyElements"]):
                survey_data["SurveyElements"][
                    qualtrics_component_index
                ] = testing_question
            else:  # add a new surveyElement
                survey_data["SurveyElements"].append(testing_question)

        # Create block and add the references
        # Generate block id
        new_block_id = generate_qualtrics_block_id()
        new_block_name = "testingBlock_" + str(int(block_number))
        new_block = create_new_testing_block(
            block_id=new_block_id, block_name=new_block_name
        )

        # Add new block
        survey_data = insert_new_survey_block_element_payload(
            survey_data=survey_data, survey_block_id="-", block_template=new_block
        )

        # Insert references to the questions in the corresponding blocks
        block_index_map = get_survey_block_element_payload_map(survey_data=survey_data)
        survey_data = insert_question_referecences_on_block(
            survey_data,
            current_testing_block_df.QID.tolist(),
            block_index_map[new_block_name],
        )

        # Update total number of questions
        component_index_survey_map = get_survey_component_index_map(
            survey_data=survey_data
        )
        survey_data = update_survey_number_of_questions(
            survey_data, component_index_survey_map, current_number_of_questions
        )

    return survey_data

def update_metafile_for_survey_creation(
    input_df, upload_df, target_filename_column="filename"
):
    """
    input_df rows --> questions in survey
    upload_df rows --> files in survey
    """
    # Define common key between dataframe and folder (name without extension)
    input_df["common_key"] = input_df.apply(
        lambda row: os.path.basename(row[target_filename_column]).split(".")[0], axis=1
    )

    # Create mappings: common key - filepaths/s3_filepaths/s3_links
    filepath_mappings = defaultdict(dict)
    s3_filepath_mappings = defaultdict(dict)
    s3_link_mappings = defaultdict(dict)
    for _, row in upload_df.iterrows():
        filepath_mappings[row["common_key"]][row["condition"]] = row["resource_link"]
        s3_filepath_mappings[row["common_key"]][row["condition"]] = row["resource_link"]
        s3_link_mappings[row["common_key"]][row["condition"]] = row["resource_link"]

    # Add filepath cols for each
    for current_condition in upload_df.condition.unique():
        # add condition col
        condition_filepath_column = str(current_condition) + "_condition_filepath"
        input_df[condition_filepath_column] = None
        input_df[condition_filepath_column] = input_df.apply(
            lambda row: filepath_mappings[row["common_key"]][current_condition], axis=1
        )

        # add condition s3 filepath col
        condition_filepath_s3_column = condition_filepath_column.replace(
            "_filepath", "_s3_filepath"
        )
        input_df[condition_filepath_s3_column] = None
        input_df[condition_filepath_s3_column] = input_df.apply(
            lambda row: s3_filepath_mappings[row["common_key"]][current_condition],
            axis=1,
        )

        # add condition s3 link col
        s3_link_column_name = condition_filepath_s3_column + "_link"
        input_df[s3_link_column_name] = None
        input_df[s3_link_column_name] = input_df.apply(
            lambda row: s3_link_mappings[row["common_key"]][current_condition], axis=1
        )

    return input_df


def update_survey_testing_flow(survey_data, RANDOMIZER_TESTING_BLOCK_ID):
    """Update survey testing flow.
    Add the the reference of all the testing blocks to the FLOW associated with the original/default
    testing block on the template.

    Args:
        survey_data (JSON): Survey QSF data.
        RANDOMIZER_TESTING_BLOCK_ID (int): index of the randomizer in the survey flow.
    Return:
        survey_data (JSON): Updated Survey
    """
    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Fetch all the new testing blocks from the survey     'testingBlock_'
    block_identifier = "testingBlock_"
    new_testing_blocks = {
        survey_data["SurveyElements"][component_index_survey_map["Survey Blocks"]][
            "Payload"
        ][payload_index]["ID"]: (
            payload_index,
            survey_data["SurveyElements"][component_index_survey_map["Survey Blocks"]][
                "Payload"
            ][payload_index]["Description"].split(block_identifier)[-1],
        )
        for block_element, payload_index in get_survey_block_element_payload_map(
            survey_data
        ).items()
        if block_identifier in block_element
    }

    randomizer_flow_id = survey_data["SurveyElements"][
        component_index_survey_map["Survey Flow"]
    ]["Payload"]["Flow"][RANDOMIZER_TESTING_BLOCK_ID]["FlowID"]

    # Compute the current max flow_id
    current_max_flow_id = (
        max(
            [
                int(item.split("_")[-1])
                for item in get_survey_flow_index_map(survey_data=survey_data).keys()
            ]
        )
        + 1
    )
    current_max_flow_id += 1

    # Create new flow block based on the flow_id that contains the original testing block
    new_template = create_new_flow_block(
        randomizer_flow_id, new_testing_blocks, current_max_flow_id
    )

    # NOTE: This part is hardcoded, it is the position 12 in the surveyflow "Flow" list.
    survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]]["Payload"][
        "Flow"
    ][RANDOMIZER_TESTING_BLOCK_ID] = new_template

    return survey_data


def update_survey_dynamic_training_flow(
    survey_data, subset, RANDOMIZER_DYNAMIC_TRAINING_BLOCK_ID
):
    """Update survey testing flow.
    Add the the reference of all the dynamic training blocks to the FLOW associated with the
    dynamic training block on the template.

    Args:
        survey_data (JSON): Survey QSF data.
        subset (int): subset of question to show to users.
        RANDOMIZER_DYNAMIC_TRAINING_BLOCK_ID (int): Randomizer block id.
    Return:
        survey_data (JSON): Updated Survey
    """
    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Fetch all the new testing blocks from the survey     'testingBlock_'
    block_identifier = "trainingDynamicBlock_"

    # BL:(payload_index, block_number)
    new_training_blocks = {
        survey_data["SurveyElements"][component_index_survey_map["Survey Blocks"]][
            "Payload"
        ][payload_index]["ID"]: (
            payload_index,
            survey_data["SurveyElements"][component_index_survey_map["Survey Blocks"]][
                "Payload"
            ][payload_index]["Description"].split(block_identifier)[-1],
        )
        for block_element, payload_index in get_survey_block_element_payload_map(
            survey_data
        ).items()
        if block_identifier in block_element
    }

    randomizer_flow_id = survey_data["SurveyElements"][
        component_index_survey_map["Survey Flow"]
    ]["Payload"]["Flow"][RANDOMIZER_DYNAMIC_TRAINING_BLOCK_ID]["FlowID"]

    # Compute the current max flow_id
    current_max_flow_id = (
        max(
            [
                int(item.split("_")[-1])
                for item in get_survey_flow_index_map(survey_data=survey_data).keys()
            ]
        )
        + 1
    )
    current_max_flow_id += 1

    # Create new flow block based on the flow_id that contains the original testing block
    new_template = create_new_dynamic_training_flow_block(
        randomizer_flow_id, new_training_blocks, current_max_flow_id, subset
    )

    # NOTE: This part is hardcoded, it is the position 10 in the surveyflow "Flow" list.
    survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]]["Payload"][
        "Flow"
    ][RANDOMIZER_DYNAMIC_TRAINING_BLOCK_ID] = new_template

    return survey_data


def update_survey_passive_training_questions(survey_data, training_df):
    """Update survey passive training questions.
    Update/Chage the number of questions of the passive_training block of the survey.
    The passive training is a single block with N question. The questions can be dynamic.

    Args:
        survey_data (JSON): Survey QSF data.
        training_df (pd.DataFrame): Passive training dataframe data.

    Returns:
        survey_data (JSON):  Updated Survey QSF data.
    """

    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Update current number of question according to the size of the dataframe.
    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )
    current_number_of_questions += len(training_df)

    # Iterate over the training questions
    for index, row in training_df.iterrows():
        # Get training question and the component index
        training_question = row["training_question_template"]
        qualtrics_component_index = row["qualtrics_component_index"]

        # if surveyElement already exists, update.
        if qualtrics_component_index < len(survey_data["SurveyElements"]):
            survey_data["SurveyElements"][qualtrics_component_index] = training_question
        else:  # add a new surveyElement
            survey_data["SurveyElements"].append(training_question)

    # Insert references to the questions in the corresponding blocks
    block_index_map = get_survey_block_element_payload_map(survey_data)
    payload_index = block_index_map["passive_training"]

    question_id_list = [item for item in training_df.QID.tolist() if not item is None]

    # Define page breaks model
    page_break = {"Type": "Page Break"}

    new_question_ref_list = []
    for qid in question_id_list:
        current_question_ref = {"Type": "Question", "QuestionID": str(qid)}
        new_question_ref_list.append(current_question_ref)
        new_question_ref_list.append(page_break)

    # Remove last element (page break)
    new_question_ref_list = new_question_ref_list[0:-1]

    # Add question refereces to the block (payload_index) 'BlockElements'
    survey_data["SurveyElements"][0]["Payload"][payload_index][
        "BlockElements"
    ] = new_question_ref_list

    # Add question references to the Options of the blokc, Randomization
    survey_data["SurveyElements"][0]["Payload"][payload_index]["Options"][
        "BlockVisibility"
    ] = "Collapsed"

    # Update total number of questions
    survey_data = update_survey_number_of_questions(
        survey_data, component_index_survey_map, current_number_of_questions
    )

    return survey_data


def update_survey_dynamic_training_questions(survey_data, training_df):
    """Update survey passive training questions.
    Update/Chage the number of questions of the dynamic_training block (randomizer) of the survey.
    The dynamic training question are organized in one per block with N question.
    The questions can be dynamic.

    Args:
        survey_data (JSON): Survey QSF data.
        training_df (pd.DataFrame): Dynamic training dataframe data.

    Returns:
        survey_data (JSON):  Updated Survey QSF data.
    """

    # Get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Update current number of question according to the size of the dataframe.
    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )

    current_number_of_questions += len(training_df)

    # Update survey data
    for index, row in training_df.iterrows():
        current_question_id = row["QID"]

        # Component id
        qualtrics_component_index = row["qualtrics_component_index"]

        # Question template
        training_question = row["training_question_template"]

        # Replace existing element
        if qualtrics_component_index < len(survey_data["SurveyElements"]):
            survey_data["SurveyElements"][qualtrics_component_index] = training_question
        else:  # add a new surveyElement
            survey_data["SurveyElements"].append(training_question)

        # Create block and add the references
        # Generate block id
        new_block_id = generate_qualtrics_block_id()
        new_block_name = "trainingDynamicBlock_" + str(int(row["sample_index"]))

        # Create new block (similar to testing block)
        new_block = create_new_dynamic_training_block(
            block_id=new_block_id, block_name=new_block_name
        )

        survey_data = insert_new_survey_block_element_payload(
            survey_data=survey_data, survey_block_id="-", block_template=new_block
        )

        # Insert references to the questions in the corresponding blocks
        block_index_map = get_survey_block_element_payload_map(survey_data=survey_data)
        payload_index = block_index_map[new_block_name]
        new_question_ref = {"Type": "Question", "QuestionID": current_question_id}

        # Add new question reference to the recently added block
        survey_data["SurveyElements"][0]["Payload"][payload_index]["BlockElements"] = [
            new_question_ref
        ]

        # Update total number of questions
        component_index_survey_map = get_survey_component_index_map(
            survey_data=survey_data
        )

        survey_data = update_survey_number_of_questions(
            survey_data, component_index_survey_map, current_number_of_questions
        )

    return survey_data

def add_condition(
    df_testing, target_column, condition_name, condition_folder, target_files
):
    """
    args:   df_testing
            target_column
            condition_name
            condition_folder
            target_files

    rets:   pd.DataFrame
    """

    # Create dataframe for the found and filter files
    for file in target_files:
        new_row = pd.DataFrame(
            {
                target_column: [target_column],
                "common_key": [file.split(".")[0]],
                "filepath": [file],
                "condition": [condition_name],
            }
        )

        df_testing = pd.concat([df_testing, new_row])

    return df_testing

def make_df_testing(conditions, input_testing_df, target_filename_column="filename"):
    """
    Take input list of conditions and folder paths
    and return dataframe where each file is a row
    ('common_key' column identifies shared filenames across conditions)

    args:   conditions (dict)
            target_filename_column (default 'filename)
    rets:   pd.DataFrame
    """
    df_testing = pd.DataFrame(
        columns=[target_filename_column, "common_key", "filepath", "condition"]
    )

    for current_condition in conditions:
        df_testing = add_condition(
            df_testing=df_testing,
            target_column=target_filename_column,
            condition_name=current_condition,
            condition_folder=current_condition,
            target_files=set(input_testing_df[target_filename_column].unique().tolist()),
        )

    df_testing.reset_index(inplace=True, drop=True)
    input_testing_df["common_key"] = input_testing_df.apply(
        lambda row: os.path.basename(row[target_filename_column]).split(".")[0], axis=1
    )

    # make a copy because the full df is needed later
    input_testing_df_copy = input_testing_df.copy()
    for col in [target_filename_column, "filepath", "condition"]:
        if col in input_testing_df_copy.columns:
            input_testing_df_copy = input_testing_df_copy.drop(columns=[col])

    df_testing = df_testing.merge(input_testing_df_copy, how="left", on="common_key")

    return df_testing


def update_upload_metafile_with_with_qualtrics_info(
    df_survey, upload_df, condition_index_mapping
):
    # create mapping common_key - qualtrics info
    common_key_qualtrics_mapping = defaultdict(dict)
    for _, row in df_survey.iterrows():
        common_key_qualtrics_mapping[row["common_key"]]["QID"] = row["QID"]
        common_key_qualtrics_mapping[row["common_key"]]["export_tag"] = row[
            "export_tag"
        ]
        common_key_qualtrics_mapping[row["common_key"]][
            "qualtrics_component_index"
        ] = row["qualtrics_component_index"]

    # initialize new cols
    upload_df["QID"] = None
    upload_df["export_tag"] = None
    upload_df["qualtrics_component_index"] = None
    upload_df["condition_index"] = None

    # update upload_df
    for index, row in upload_df.iterrows():
        condition = row["condition"]
        upload_df.at[index, "QID"] = common_key_qualtrics_mapping[row["common_key"]][
            "QID"
        ]
        upload_df.at[index, "export_tag"] = common_key_qualtrics_mapping[
            row["common_key"]
        ]["export_tag"]
        upload_df.at[index, "qualtrics_component_index"] = common_key_qualtrics_mapping[
            row["common_key"]
        ]["qualtrics_component_index"]
        # only adds condition index for rated conditions (ref not always rating condition)
        upload_df.at[index, "condition_index"] = condition_index_mapping.get(
            common_key_qualtrics_mapping[row["common_key"]]["export_tag"], None
        ).get(condition, None)

    return upload_df
