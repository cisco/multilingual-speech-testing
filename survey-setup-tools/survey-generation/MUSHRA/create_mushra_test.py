"""
Cisco Systems, Inc. and its affiliates
"""
#!/usr/bin/env python
# coding: utf-8

"""
Create MUSHRA test
MUSHRA template for external use.
Create template QSF file to generate tests.

Usage:
python create_mushra_test.py -ji configuration_file.json
"""

import pandas as pd

import os
import argparse
import hashlib
import json
import logging
import random
from collections import defaultdict
import glob

from survey.survey_preparation import (
    make_df_testing,
    prepare_survey_quotas,
    sample_hearing_test_files,
    update_metafile_for_survey_creation,
    update_survey_testing_questions,
    update_survey_dynamic_training_questions,
    update_survey_testing_flow,
    update_survey_dynamic_training_flow,
    update_survey_hearing_test_block,
    prepare_testing_questions,
    prepare_dynamic_training_questions,
    remove_block_from_flow,
    update_upload_metafile_with_with_qualtrics_info,
)

from utils.validation import (
    validate_json_input,
)

from qualtrics_utils.survey_flow import (
    create_or_update_survey_embedded_data_field,
)


MAX_JSON_INT_VALUE = 2147483647
BASELINE_QSF_PATH = "baseline_qsf/mushra_survey.qsf"

# NOTE: this part is hardcoded, the IDs in the flow depend on the survey itself.
RANDOMIZER_DYNAMIC_TRAINING_BLOCK_ID = 10
RANDOMIZER_TESTING_BLOCK_ID = 12

def main(args):
    """QSF survey preparation generation"""

    # Global indexes for the blocks
    global RANDOMIZER_DYNAMIC_TRAINING_BLOCK_ID
    global RANDOMIZER_TESTING_BLOCK_ID

    # Extract survey configuration parameters
    experiment_name = args.survey_config["experiment_name"]
    testing_metafile = args.survey_config["testing_metafile"]
    target_filename_column = args.survey_config["target_filename_column"]
    output_directory = args.survey_config["output_dir"]

    # Extract survey option parameters
    survey_options = args.survey_options
    target_question = survey_options['survey_question']

    # Hearing, training and validation csvs
    hearing_test_files = survey_options["hearing_test"]
    training_set = survey_options["training_set"]
    training_pass_threshold = survey_options["training_pass_threshold"]
    training_attempts_limit = survey_options["training_attempts_limit"]

    df_testing = pd.read_csv(testing_metafile)

    reference_threshold = survey_options["ref_threshold"]
    anchor_threshold = survey_options["anchor_threshold"]
    anchor_min_distance_wrt_reference = survey_options[
        "anchor_min_distance_wrt_reference"
    ]
    
    # Set anchor type
    anchor_type = "relative"
    if anchor_min_distance_wrt_reference is None:
        anchor_type = "max"

    correct_answers_threshold = survey_options["correct_answers_threshold"]
    anchor_correct_answers = correct_answers_threshold["anchor_correct_answers"]
    ref_correct_answers = correct_answers_threshold["ref_correct_answers"]

    shuffle = survey_options["blocks"]["file_assignment"]

    # Extract seed
    seed = survey_options["seed"]
    if seed is None:
        # generate random seed
        survey_seed = random.randint(0, MAX_JSON_INT_VALUE)
        survey_options["seed"] = survey_seed
        args.survey_options["seed"] = survey_options["seed"]
        seed = survey_options["seed"]

    experiment_name = args.survey_config["experiment_name"]
    experiment_name_hash = hashlib.md5(
        (experiment_name + str(seed)).encode("utf-8")
    ).hexdigest()

    # Create output directory
    output_experiment_dir = os.path.join(
        output_directory, experiment_name, experiment_name_hash
    )

    if not os.path.exists(output_experiment_dir):
        os.makedirs(output_experiment_dir)

    # Set up loggging
    login_output_filepath = os.path.join(output_experiment_dir, "survey_generation.log")

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Output file login
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(login_output_filepath, mode="w+"),
            logging.StreamHandler(),
        ],
    )

    logger = logging.getLogger(__name__)

    logger.info("STARTING MUSHRA SURVEY GENERATION")
    logger.info(
        "EXPERIMENT: {}, S3 NAME: {}".format(experiment_name, experiment_name_hash)
    )
    logger.info("OUTPUT DIRECTORY: {} ".format(output_experiment_dir))

    enable_dynamic_training_section = True
    if training_set is None:
        enable_dynamic_training_section = False

    if enable_dynamic_training_section is True:
        # Get dynamic training set
        dynamic_training_task_samples = training_set

    # Sample 2 per easy, 2 medium, 2 hard
    hearing_test_sample = sample_hearing_test_files(hearing_test_files)

    # Conditions
    conditions = df_testing.condition.unique().tolist()

    # shuffle filenames such that the selection of questions per block is randomized
    if shuffle == "random":
        df_testing = df_testing.sample(frac=1).reset_index(drop=True)

    # Update qualtrics configuration file.
    logger.info("PREPARE SURVEY: TESTING METAFILES")
    logger.info("EXPERIMENT SEED: {}".format(survey_options["seed"]))

    # re-create metafile where rows --> questions (and cols for each condition)
    df_survey = update_metafile_for_survey_creation(
        input_df=df_testing, upload_df=df_testing
    )
    survey_data_mapping = prepare_survey_quotas(
        testing_df=df_testing, qualtrics_conf=survey_options, conditions=conditions
    )

    # Concat mappings in dataframe
    df_survey = pd.concat(
        [survey_data_mapping[key] for key in survey_data_mapping.keys()]
    )

    df_survey.sort_values(by=["block"], inplace=True)
    df_survey.reset_index(inplace=True, drop=True)

    logger.info("NUMBER OF BLOCKS IN THE SURVEY: {}".format(len(survey_data_mapping)))

    # df_survey = pd.read_csv("survey_data_442.csv")
    with open(BASELINE_QSF_PATH) as f:
        survey_data = json.load(f)

    # Prepare hearing test links
    hearing_test_links = {}
    for index, (condition_link, digits) in enumerate(hearing_test_sample):
        hearing_test_links[str(index + 1)] = (condition_link, digits)

    # Update hearing test block
    survey_data = update_survey_hearing_test_block(
        survey_data=survey_data, hearing_test_options=hearing_test_links
    )

    if enable_dynamic_training_section is True:
        # Prepare training questions
        # Generate presigned URLs
        dynamic_training_condition_links = {}
        for key in dynamic_training_task_samples.keys():
            current_sample_link = dynamic_training_task_samples[key]
            
            # Insert score and caption
            for condition in current_sample_link.keys():
                current_sample_link[condition] = current_sample_link[condition]

            dynamic_training_condition_links[key] = current_sample_link

        # Prepare dynamic training questions
        (
            dynamic_training_df,
            condition_index_mapping,
        ) = prepare_dynamic_training_questions(
            training_condition_links=dynamic_training_condition_links,
            survey_data=survey_data,
        )

        # Update question within the survey
        survey_data = update_survey_dynamic_training_questions(
            survey_data=survey_data, training_df=dynamic_training_df
        )

        # Update dynamic training flow
        survey_data = update_survey_dynamic_training_flow(
            survey_data, len(dynamic_training_df), RANDOMIZER_DYNAMIC_TRAINING_BLOCK_ID
        )
    else:
        # Remove passive training section from the flow.
        survey_data = remove_block_from_flow(
            block_name_description="dynamic_training", survey_data=survey_data
        )

        survey_data = remove_block_from_flow(
            block_name_description="dynamic_training_instructions",
            survey_data=survey_data,
        )

        # Adjust testing randomizer index
        RANDOMIZER_TESTING_BLOCK_ID = 9

    logger.info("=" * 100)

    # Preparing testing questions
    logger.info("PREPARING TESTING QUESTIONS")

    # Prepare testing question
    df_survey, condition_index_mapping = prepare_testing_questions(
        testing_df=df_survey, survey_data=survey_data, target_question=target_question
    )

    # Update flow in the survey to include all testing question
    survey_data = update_survey_testing_questions(
        survey_data=survey_data, testing_df=df_survey
    )

    logger.info("UPDATING SURVEY FLOW WITH NEW TESTING BLOCKS")
    survey_data = update_survey_testing_flow(survey_data, RANDOMIZER_TESTING_BLOCK_ID)
    logger.info("=" * 100)

    logger.info("UPDATING EMBEDDED VARIABLES: block selection")
    # Set embedded variables for blocks  (block_N_selected = 0)
    for block_id in df_survey.block.unique():
        block_name_template_name = "block_{}_selected".format(block_id)
        survey_data = create_or_update_survey_embedded_data_field(
            survey_data=survey_data,
            embedded_data_field=block_name_template_name,
            new_value=0,
        )

    logger.info("UPDATING EMBEDDED VARIABLES: hearing test, correct answers")
    # Update hearing test threshold
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="hearing_correct_answers_threshold",
        new_value=13,
    )

    for index, link_digit in hearing_test_links.items():
        audio_index = "ht_audio_" + index
        audio_digit = link_digit[1]
        survey_data = create_or_update_survey_embedded_data_field(
            survey_data=survey_data,
            embedded_data_field=audio_index,
            new_value=audio_digit,
        )

    logger.info("UPDATING EMBEDDED VARIABLES: correct answers threshold")

    # Update correct anchor answers threshold
    max_questions_per_block = df_survey.block.value_counts().max()
    if (
        anchor_correct_answers is None
        or anchor_correct_answers > max_questions_per_block
    ):
        anchor_correct_answers = (
            max_questions_per_block  # Set threshold at max for anchor (no errors)
        )
    logger.info("UPDATING EMBEDDED VARIABLES: anchor_correct_answers_threshold")
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="anchor_correct_answers_threshold",
        new_value=anchor_correct_answers,
    )

    # Update correct reference answers threshold
    if ref_correct_answers is None or ref_correct_answers > max_questions_per_block:
        ref_correct_answers = (
            max_questions_per_block  # Set threshold at max for ref (no errors)
        )
        
    logger.info("UPDATING EMBEDDED VARIABLES: ref_correct_answers_threshold")
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="ref_correct_answers_threshold",
        new_value=ref_correct_answers,
    )

    logger.info("UPDATING EMBEDDED VARIABLES: total questions per block")
    # Update total questions per block
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="total_questions_per_block",
        new_value=max_questions_per_block,
    )

    if enable_dynamic_training_section is True:
        logger.info("UPDATING EMBEDDED VARIABLES: total dynamic training questions")
        # Update total dynamic trainning questions
        survey_data = create_or_update_survey_embedded_data_field(
            survey_data=survey_data,
            embedded_data_field="total_dynamic_training_questions",
            new_value=len(dynamic_training_task_samples),
        )

    logger.info("UPDATING EMBEDDED VARIABLES: dynamic training pass threshold")

    if training_pass_threshold is None:
        training_pass_threshold = 37

    # Update dynamic training pass threshold
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="training_pass_threshold",
        new_value=training_pass_threshold,
    )

    logger.info("UPDATING EMBEDDED VARIABLES: dynamic training attemps limit")
    if training_attempts_limit is None:
        training_attempts_limit = 12

    # Update dynamic training pass threshold
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="training_question_attempts_limit",
        new_value=training_attempts_limit,
    )
    
    logger.info("UPDATING EMBEDDED VARIABLES: reference threshold")
    # Update reference threshold
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="ref_threshold",
        new_value=reference_threshold,
    )


    logger.info("UPDATING EMBEDDED VARIABLES: anchor type")
    # Update anchor type
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="anchor_type",
        new_value=anchor_type,
    )
    
    logger.info("UPDATING EMBEDDED VARIABLES: anchor threshold")
    # Set 100 when not defined    
    if anchor_threshold is None:
        anchor_threshold = 100

    # Update anchor threshold
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="anchor_threshold",
        new_value=anchor_threshold,
    )
    
    logger.info("UPDATING EMBEDDED VARIABLES: min_anchor_distance_wrt_reference")
    # Set zero when not defined.
    if anchor_min_distance_wrt_reference is None:
        anchor_min_distance_wrt_reference = 0

    # Update min anchor distance wrt reference    
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="min_anchor_distance_wrt_reference",
        new_value=anchor_min_distance_wrt_reference,
    )

    logger.info("UPDATING EMBEDDED VARIABLES: max possible audio files in survey")
    # Create max number of audio files
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="max_possible_audio_files_in_block",
        new_value=3 * max_questions_per_block * len(conditions),
    )

    logger.info("UPDATING EMBEDDED VARIABLES: bonus structure and payment rate")
    # Create max number of audio files

    # Placeholder for non-used payment dictionary
    payment_region_dict = {
        "payment_rate": 0,
        "base_pay": 0,
        "bonus_1_blocks": 0,
        "bonus_2_blocks": 0,
        "bonus_3_blocks": 0,
    }
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="payment_rate",
        new_value=str(payment_region_dict["payment_rate"]),
    )

    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="base_pay",
        new_value=str(payment_region_dict["base_pay"]),
    )

    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="bonus_1_blocks",
        new_value=str(payment_region_dict["bonus_1_blocks"]),
    )

    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="bonus_2_blocks",
        new_value=str(payment_region_dict["bonus_2_blocks"]),
    )

    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="bonus_3_blocks",
        new_value=str(payment_region_dict["bonus_3_blocks"]),
    )

    message = ""
    if float(payment_region_dict["bonus_1_blocks"]) != 0:
        message = " + $" + str(round(payment_region_dict["bonus_1_blocks"], 2))

    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="total_pay_bonus_1",
        new_value=str(str(round(payment_region_dict["base_pay"], 2)) + message),
    )

    message = ""
    if float(payment_region_dict["bonus_2_blocks"]) != 0:
        message = " + $" + str(round(payment_region_dict["bonus_2_blocks"], 2))

    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="total_pay_bonus_2",
        new_value=str(str(round(payment_region_dict["base_pay"], 2)) + message),
    )

    message = ""
    if float(payment_region_dict["bonus_3_blocks"]) != 0:
        message = " + $" + str(round(payment_region_dict["bonus_3_blocks"], 2))

    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="total_pay_bonus_3",
        new_value=str(str(round(payment_region_dict["base_pay"], 2)) + message),
    )

    # Set embedded variable for dynamic training job enable
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="dynamic_training_job",
        new_value="yes" if enable_dynamic_training_section is True else "no",
    )

    # Set survey main question
    survey_data = create_or_update_survey_embedded_data_field(
        survey_data=survey_data,
        embedded_data_field="survey_main_question",
        new_value=str(target_question),
    )

    logger.info("=" * 100)

    qsf_file_target_location = os.path.join(
        output_experiment_dir, "survey_qualtrics_{}.qsf".format(experiment_name_hash)
    )
    logger.info("SAVE SURVEY QSF FILE: {}".format(qsf_file_target_location))

    with open(qsf_file_target_location, "w") as outfile:
        json.dump(survey_data, outfile, separators=(',', ':'))

    logger.info("SAVING SURVEY BLOCKS")

    df_testing = make_df_testing(
        conditions, df_testing, target_filename_column
    )
    # update 'longform' metafile with qualtrics info (QID, export tag, component ID)
    # and save/upload
    df_full = update_upload_metafile_with_with_qualtrics_info(
        df_survey=df_survey,
        upload_df=df_testing,
        condition_index_mapping=condition_index_mapping,
    )

    survey_block_output_path = os.path.join(output_experiment_dir, "meta_survey.csv")
    meta_s3_path = os.path.join(output_experiment_dir, "meta_s3.csv")
    df_full.to_csv(survey_block_output_path, index=None, header=True)
    df_full.to_csv(meta_s3_path, index=None, header=True)

    # also overwrite meta file in local upload to s3 folder
    df_full.to_csv(
        os.path.join(output_experiment_dir, "meta_s3.csv"),
        index=None,
        header=True,
    )

    logger.info("SAVED SURVEY: {} ".format(survey_block_output_path))
    logger.info("=" * 100)

    # Save generation recipe
    recipe_filepath = os.path.join(output_experiment_dir, "survey_recipe.json")
    with open(recipe_filepath, "w") as out_file:
        recipe_dict = vars(args)

        json.dump(recipe_dict, out_file, indent=4)

    return experiment_name_hash


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MUSHRA testing generation")

    parser.add_argument(
        "-ji", "--json_input", required=True, type=str, help="json input metafile"
    )

    current_arguments, _ = parser.parse_known_args()
    json_configuration_input = vars(current_arguments).get("json_input", None)

    if json_configuration_input is not None:
        if os.path.exists(json_configuration_input):
            with open(json_configuration_input) as f:
                args = json.load(f)

    print(json.dumps(args, indent=4))

    validate_json_input(args)

    main(argparse.Namespace(**args))
