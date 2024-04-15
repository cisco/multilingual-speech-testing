"""
Cisco Systems, Inc. and its affiliates
"""
"""
QSF survey preparation utilities.
"""
import pandas as pd
import sys
import os
import json
import random
import re

from templates.template_helpers.sit_questions import (
    create_training_question,
    create_testing_question,
)
from templates.template_helpers.sit_blocks import (
    create_new_testing_block,
    create_new_flow_block,
    create_hearing_test_block,
)

from qualtrics_utils.survey_components import (
    get_number_of_survey_components,
    get_survey_component_index_map,
)
from qualtrics_utils.survey_questions import (
    get_current_number_of_questions,
    insert_question_referecences_on_block,
    update_survey_number_of_questions,
)
from qualtrics_utils.survey_constants import QUESTION_ID_PREFIX
from qualtrics_utils.survey_metadata import get_survey_id, generate_qualtrics_block_id
from qualtrics_utils.survey_payload_elements import (
    get_survey_block_element_payload_map,
    insert_new_survey_block_element_payload,
)
from qualtrics_utils.survey_flow import (
    get_survey_flow_index_by_block_id,
    get_survey_flow_index_map,
    update_flow_by_payload_index,
)


def sample_dataframe(input_df, sample_size, target_column, target_value, seed):
    """Get a random sample of size "sample_size" of the column "target_column" with the 
    value "target_value".

    Args:
        input_df (pd.DataFrame): input dataframe.
        sample_size (int): Sample size. If greater than len(input_df)
        target_column (string): filtering column
        target_value (string): target value of the column
        seed (int): random state of the sample method.
    Returns:
        pd.DataFrame: dataframe sample
    """

    assert len(input_df) > 0
    assert target_column in input_df.columns.tolist()

    total_sample_df = input_df[input_df[target_column] == target_value]
    total_sample_size = len(total_sample_df)

    if total_sample_size > sample_size:
        return total_sample_df.sample(sample_size, random_state=seed)
    else:
        return total_sample_df.sample(sample_size, replace=True, random_state=seed)


def prepare_survey_quotas(training_df, validation_df, testing_df, qualtrics_conf):
    """Prepare survey quotas. 
    Prepare survey using qualtrics_conf quota parameters for training, validation and testing.
    
    Args:
        training_df (pd.DataFrame): training dataset 
        validation_df (pd.DataFrame): validation dataset 
        testing_df (pd.DataFrame): testing dataset 
        qualtrics_conf (json): json qualtrics configuration file (qualtrics_qsf_conf)

    Returns:
        tuple: (training data dataframe, survey block dictionary block: testing+validation dataframe)
    """

    assert len(training_df) > 0
    assert len(validation_df) > 0
    assert len(testing_df) > 0
    assert "block" in testing_df.columns.tolist()

    seed = qualtrics_conf["seed"]
    training_questions_quota = qualtrics_conf["training"]
    validation_questions_quota = qualtrics_conf["validation"]

    # 1) sampling training data
    df_training_clean_sample = sample_dataframe(
        training_df,
        training_questions_quota["clean"]["number_files"],
        "type",
        "clean",
        seed=seed,
    )
    df_training_noisy_sample = sample_dataframe(
        training_df,
        training_questions_quota["noisy"]["number_files"],
        "type",
        "noisy",
        seed=seed,
    )
    df_training_block = pd.concat(
        [df_training_clean_sample, df_training_noisy_sample]
    ).sample(frac=1, random_state=seed)
    df_training_block = df_training_block.assign(dataset_type="training")
    df_training_block.reset_index(inplace=True, drop=True)

    # 2) sampling testing and validation data by block
    # mapping block -> (testing + validation)
    survey_data_mapping = {}
    for block_number in testing_df.block.unique():

        # get current testing df block
        df_testing_block = testing_df[testing_df.block == block_number]

        # sample validation quotas
        df_validation_clean_sample = sample_dataframe(
            validation_df,
            validation_questions_quota["clean"]["number_files"],
            "type",
            "clean",
            seed=seed,
        )
        df_validation_noisy_sample = sample_dataframe(
            validation_df,
            validation_questions_quota["noisy"]["number_files"],
            "type",
            "noisy",
            seed=seed,
        )
        df_validation_block = pd.concat(
            [df_validation_clean_sample, df_validation_noisy_sample]
        )

        df_validation_block = df_validation_block.assign(dataset_type="validation")
        df_validation_block = df_validation_block.assign(block=block_number)
        df_testing_block = df_testing_block.assign(dataset_type="testing")
        df_testing_block = df_testing_block.assign(type=None)
        common_columns = list(
            set(df_validation_block.columns.tolist()).intersection(
                df_testing_block.columns.tolist()
            )
        )

        # concat testing and validation
        df_total = pd.concat(
            [df_validation_block[common_columns], df_testing_block[common_columns]]
        )

        # sample and save
        survey_data_mapping[block_number] = df_total.sample(frac=1, random_state=seed)

    return df_training_block, survey_data_mapping


def prepare_survey_dataframe(survey_data_mapping):
    """Prepare survey (testing and validation files) DataFrame.
    The survey dataframe consists of blocks, these blocks contain
    experiment files and validation files.
    Args:
        survey_data_mapping (dict): block -> dataframe
    Returns:
        pd.DataFrame: Dataframe containing all the blocks in the survey_data_mapping.
    """
    # concatenate dataframe blocks
    df_survey = pd.concat(
        [survey_data_mapping[block] for block in survey_data_mapping.keys()]
    )
    df_survey.sort_values(by=["block"], inplace=True)
    df_survey.reset_index(inplace=True, drop=True)

    return df_survey


def prepare_training_questions(training_df, survey_data):
    """Prepare training survey questions.

    Args:
        training_df (pd.DataFrame): training block dataframe questions.
        survey_data (JSON): Survey QSF data.
    Returns:
        pd.DataFrame
    """

    assert len(training_df) > 0

    training_df["training_question_template"] = None
    training_df["QID"] = None
    training_df["qualtrics_component_index"] = None

    # get survey_id
    SURVEY_ID = get_survey_id(survey_data=survey_data)

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Get current number of questions and components
    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )
    current_number_of_components = get_number_of_survey_components(survey_data) + 1

    # get all alternative columns
    alternative_columns = [
        column
        for column in training_df.columns.tolist()
        if re.search("alternative[0-9]+", column)
    ]

    for index, row in training_df.iterrows():

        training_type = row["type"]
        target = row["target"]

        alternatives = [row[alternative] for alternative in alternative_columns]
        resource_link = row["resource_link"]

        # generate question_id
        question_id = QUESTION_ID_PREFIX + str(current_number_of_questions)
        training_df.at[index, "QID"] = question_id

        # generate export tag
        export_tag = "Q" + str(current_number_of_questions)
        training_df.at[index, "export_tag"] = export_tag

        # generate component id
        component_id = current_number_of_components
        training_df.at[index, "qualtrics_component_index"] = component_id

        # generate training question
        new_training_question = create_training_question(
            surveyID=SURVEY_ID,
            export_tag=export_tag,
            question_id=question_id,
            training_type=training_type,
            target=target,
            alternatives=alternatives,
            audio_link=resource_link,
        )

        training_df.at[index, "training_question_template"] = new_training_question

        current_number_of_questions += 1
        current_number_of_components += 1

    return training_df


def update_survey_training_questions(survey_data, training_df):
    """Update survey training questions.
    Update/Chage the number of questions of the trainingBlock of the survey.

    Args:
        survey_data (JSON): Survey QSF data.
        training_df (pd.DataFrame): training dataframe with all the question
        
    Returns:
        survey_data (JSON):  Updated Survey QSF data.
    """

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # update current number of question according to the size of the dataframe.
    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )
    current_number_of_questions += len(training_df)

    for index, row in training_df.iterrows():

        # get training question and the component index
        training_question = row["training_question_template"]
        qualtrics_component_index = row["qualtrics_component_index"]

        # if surveyElement already exists, update.
        if qualtrics_component_index < len(survey_data["SurveyElements"]):
            survey_data["SurveyElements"][qualtrics_component_index] = training_question
        else:  # add a new surveyElement
            survey_data["SurveyElements"].append(training_question)

    # insert references to the questions in the corresponding blocks
    block_index_map = get_survey_block_element_payload_map(survey_data)
    question_id_list = [item for item in training_df.QID.tolist() if not item is None]
    survey_data = insert_question_referecences_on_block(
        survey_data, question_id_list, block_index_map["trainingBlock"]
    )

    # Update total number of questions
    survey_data = update_survey_number_of_questions(
        survey_data, component_index_survey_map, current_number_of_questions
    )
    return survey_data


def prepare_testing_questions(testing_df, survey_data):
    """Prepare testing (main task) questions.
    These questions include validation questions and training questions.

    Args:
        testing_df (pd.DataFrame): training block dataframe questions.
        survey_data (JSON): Survey QSF data.
    Returns:
        pd.DataFrame
    """
    testing_df["testing_question_template"] = None
    testing_df["QID"] = None
    testing_df["qualtrics_component_index"] = None

    # get survey_id
    SURVEY_ID = get_survey_id(survey_data=survey_data)

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )
    current_number_of_components = get_number_of_survey_components(survey_data) + 1

    alternative_columns = [
        column
        for column in testing_df.columns.tolist()
        if re.search("alternative[0-9]+", column)
    ]

    # compute metadata
    for (index, row,) in testing_df.iterrows():

        testing_type = row["type"] if not pd.isna(row["type"]) else "testing"

        # options
        target = row["target"]
        alternatives = [row[alternative] for alternative in alternative_columns]

        # generate question_id
        question_id = QUESTION_ID_PREFIX + str(current_number_of_questions)
        testing_df.at[index, "QID"] = question_id

        resource_link = row["resource_link"]

        # generate export tag
        export_tag = "Q" + str(current_number_of_questions)
        testing_df.at[index, "export_tag"] = export_tag

        # generate component id
        qualtrics_component_index = current_number_of_components
        testing_df.at[index, "qualtrics_component_index"] = qualtrics_component_index

        # compute validation flag
        is_validation = True if row["dataset_type"] == "validation" else False
        testing_df.at[index, "is_validation"] = is_validation

        new_testing_question = create_testing_question(
            surveyID=SURVEY_ID,
            export_tag=export_tag,
            question_id=question_id,
            testing_type=testing_type,
            target=target,
            alternatives=alternatives,
            audio_link=resource_link,
            is_validation=is_validation,
        )

        testing_df.at[index, "testing_question_template"] = new_testing_question

        current_number_of_questions += 1
        current_number_of_components += 1

    return testing_df


def update_survey_testing_questions(survey_data, testing_df):
    """Update survey training questions.
    Update/Change the number of questions and **blocks** of the testingBlock of the survey.
    The testing questions are divided by blocks, each block has N questions.

    Args:
        survey_data (JSON): Survey QSF data.
        testing_df (pd.DataFrame): 
        
    Returns:
        survey_data (JSON):  Updated Survey QSF data.
    """

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # update current number of question according to the size of the dataframe.
    current_number_of_questions = (
        get_current_number_of_questions(survey_data, component_index_survey_map) + 1
    )
    current_number_of_questions += len(testing_df)

    # update survey data
    for block_number in list(testing_df.block.unique()):

        # get the target block
        current_testing_block_df = testing_df[testing_df.block == block_number]
        for index, row in current_testing_block_df.iterrows():

            # component id
            qualtrics_component_index = row["qualtrics_component_index"]

            # question
            testing_question = row["testing_question_template"]

            # if surveyElement already exists, update.
            if qualtrics_component_index < len(survey_data["SurveyElements"]):
                survey_data["SurveyElements"][
                    qualtrics_component_index
                ] = testing_question
            else:  # add a new surveyElement
                survey_data["SurveyElements"].append(testing_question)

        # Create block and add the references

        # generate block id
        new_block_id = generate_qualtrics_block_id()
        new_block_name = "testingBlock_" + str(int(block_number))
        new_block = create_new_testing_block(
            block_id=new_block_id, block_name=new_block_name
        )

        # add new block
        survey_data = insert_new_survey_block_element_payload(
            survey_data=survey_data, survey_block_id="-", block_template=new_block
        )

        # insert references to the questions in the corresponding blocks
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


def update_survey_testing_flow(survey_data):
    """Update survey testing flow.
    Add the the reference of all the testing blocks to the FLOW associated with the original/default
    testing block on the template.
    
    Args:
        survey_data (JSON): Survey QSF data.
        
    Return:
        survey_data (JSON): Updated Survey
    """

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # fetch all the new testing blocks from the survey     'testingBlock_'
    new_testing_blocks = {
        survey_data["SurveyElements"][component_index_survey_map["Survey Blocks"]][
            "Payload"
        ][payload_index]["ID"]: payload_index
        for block_element, payload_index in get_survey_block_element_payload_map(
            survey_data
        ).items()
        if "testingBlock_" in block_element
    }

    # get the payload elements mapping
    survey_block_payload_index_map = get_survey_block_element_payload_map(
        survey_data=survey_data
    )

    # find the block id of the original testing block (the one by default in the survey)
    block_id_in_testing_block = survey_data["SurveyElements"][
        component_index_survey_map["Survey Blocks"]
    ]["Payload"][survey_block_payload_index_map["testingBlock"]]["ID"]

    # get the index of the FLOW that contains the original testing block
    randomizer_testing_flow_id = get_survey_flow_index_by_block_id(
        survey_data=survey_data, block_id=block_id_in_testing_block
    )

    # get the ID of the FLOW that contains the original testing block
    flow_id = survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]][
        "Payload"
    ]["Flow"][randomizer_testing_flow_id]["FlowID"]

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

    # create new flow block based on the flow_id that contains the original testing block
    new_template = create_new_flow_block(
        flow_id, new_testing_blocks, current_max_flow_id
    )

    # update survey data
    survey_data = update_flow_by_payload_index(
        survey_data=survey_data,
        survey_payload_flow_index=randomizer_testing_flow_id,
        flow_template=new_template,
    )

    return survey_data


def update_survey_target_language(survey_data, survey_target_language):
    """Update survey target language.
    Optimize the QSF file. Include the default language "EN" support for the target language.
    
    Args:
        survey_data (JSON): Survey QSF data.
        survey_target_language(string): Survey target Language. 
    Return:
        survey_data (JSON): Updated Survey.
    """

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # update list of supported languages
    survey_data["SurveyElements"][component_index_survey_map["Survey Options"]][
        "Payload"
    ]["AvailableLanguages"] = {"EN": [], survey_target_language: []}

    # Update all the components with multiple languages:
    for component_name, component_index in component_index_survey_map.items():

        if "Payload" in survey_data["SurveyElements"][component_index].keys():
            current_payload = survey_data["SurveyElements"][component_index]["Payload"]

            if (
                isinstance(current_payload, dict)
                and "Language" in current_payload.keys()
            ):
                languages = survey_data["SurveyElements"][component_index]["Payload"][
                    "Language"
                ]

                if (
                    isinstance(languages, dict)
                    and survey_target_language in languages.keys()
                ):
                    languages = {
                        survey_target_language: languages[survey_target_language]
                    }
                    survey_data["SurveyElements"][component_index]["Payload"][
                        "Language"
                    ] = languages
                else:  # Keep only default language.
                    survey_data["SurveyElements"][component_index]["Payload"][
                        "Language"
                    ] = {}

    return survey_data


def update_survey_hearing_test_block(survey_data, hearing_test_options):
    """Update survey hearing test block.
    Update the audio links for the hearing test based on the hearing_test_options 
    Args:
        survey_data (JSON): Survey QSF data.
        hearing_test_options(dict): {option: link, digits}. 
    Return:
        survey_data (JSON): Updated Survey.
    """
    SURVEY_HEARING_TEST_COMPONENT_ID = "QID1213622116"

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)
    hearing_test_component_index = component_index_survey_map[
        SURVEY_HEARING_TEST_COMPONENT_ID
    ]

    new_hearing_test_block = create_hearing_test_block(hearing_test_options)

    survey_data["SurveyElements"][hearing_test_component_index] = new_hearing_test_block

    return survey_data


def update_end_of_message(survey_data, flow_id, library_element_id):
    """update survey end of message of target flow_id
    
    Args:
        survey_data (JSON): Survey QSF data.
        flow_id (string): Flow ID of the end of message.
        library_element_id (string): ID of the new element in the survey
    Return:
        survey_data (JSON): Updated Survey.
    """
    found = False

    # get survey component index map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # Extract Payload from the Survey Flow
    survey_flow_ids = survey_data["SurveyElements"][
        component_index_survey_map["Survey Flow"]
    ]["Payload"]["Flow"]
    survey_flow_length = len(survey_flow_ids)

    for index, flow_dict in zip(range(0, survey_flow_length), survey_flow_ids):

        # find target flow ID
        if flow_id in json.dumps(flow_dict):

            # iterate over all the elements of the given flow_dict
            for i_index, i_item in zip(
                range(0, len(flow_dict["Flow"])), flow_dict["Flow"]
            ):
                if flow_id in i_item["FlowID"]:
                    # update
                    found = True
                    survey_data["SurveyElements"][
                        component_index_survey_map["Survey Flow"]
                    ]["Payload"]["Flow"][index]["Flow"][i_index]["Options"][
                        "EOSMessage"
                    ] = library_element_id
                    break
            break

    if found:
        return survey_data
    else:
        return None
