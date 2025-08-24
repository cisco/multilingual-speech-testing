"""
Cisco Systems, Inc. and its affiliates
"""
"""
Survey preparation utilities
"""
import pandas as pd
import os
import sys
import random
import shutil
import base64
import hashlib
import logging
import json

from qualtrics_utils.survey_flow import update_survey_embedded_data_fields

from utils.qsf_survey_preparation import (
    prepare_survey_quotas,
    prepare_survey_dataframe,
    prepare_training_questions,
    update_survey_training_questions,
    prepare_testing_questions,
    update_survey_testing_questions,
    update_survey_testing_flow,
    update_survey_target_language,
    update_survey_hearing_test_block,
)


def get_language_code(tgt_language):
    """
    from internal_config["qualtrics_supported_languages"],
    get language code (e.g. "EN") for target language (e.g. english)
    """
    internal_config_path = "supported-languages/languages_speech_intelligibility_test.json"

    with open(internal_config_path) as f:
        internal_config = json.load(f)

    lang_dict = internal_config["qualtrics_supported_languages"]
    tgt_lang_code = [
        lang_code
        for lang_code, spelled_lang in lang_dict.items()
        if spelled_lang.lower() == tgt_language
    ][0]
    return tgt_lang_code


def generate_experiment_seed():
    """Generate a random seed for the experiment."""
    return random.randint(0, MAX_JSON_INT_VALUE)


def generate_experiment_name(experiment_name, seed):
    """Generate experiment name.
    Generate hash name for the experiment, the same experiment
    can be generated with different seeds.
    """
    return hashlib.md5((experiment_name + str(seed)).encode("utf-8")).hexdigest()


def update_payment_embedded_data_fields(
    survey_template,
    survey_configuration,
    total_training_questions,
    total_main_questions,
):
    """Update payment embedded data fields
    Args:
        survey_template(dict): JSON input QSF qualtrics file.
        survey_configuration (dict): survey configuration dictionary    
        total_training_questions (int): total number of training questions.
        total_main_questions (int): total number (max block size) of testing questions.
    Returns:
        survey_data (dict): Updated version of the survey_data JSON file.
    """
    logger = logging.getLogger(__name__)
    QUESTION_ANSWERING_TIME = 3
    MINUTES_IN_HOUR = 60
    ROUND_UP = 1

    # estimate the duration of the survey
    duration_train = (
        round(total_training_questions * QUESTION_ANSWERING_TIME / MINUTES_IN_HOUR)
        + ROUND_UP
    )
    duration_main = (
        round(total_main_questions * QUESTION_ANSWERING_TIME / MINUTES_IN_HOUR)
        + ROUND_UP
    )
    duration_total_survey = duration_train + duration_main

    # estimate the base payment
    payment_rate = survey_configuration["payment_rate"]
    base_pay = round((payment_rate / MINUTES_IN_HOUR) * duration_total_survey, 2)

    # set up payment embedded data.
    payment_embedded_data = {}
    payment_embedded_data["hourly_rate"] = str(payment_rate)
    payment_embedded_data["bonus_rate"] = survey_configuration["bonus"]
    payment_embedded_data["duration_total_survey"] = str(duration_total_survey)
    payment_embedded_data["duration_train"] = str(duration_train)
    payment_embedded_data["duration_main"] = str(duration_main)
    payment_embedded_data["base_pay"] = str(base_pay)

    logger.info(
        "UPDATING EMBEDDED DATA FIELDS PAYMENT INFORMATION {} ".format(
            payment_embedded_data
        )
    )

    # update payment information according to the target platform
    survey_template = update_survey_embedded_data_fields(
        survey_template, payment_embedded_data
    )

    return survey_template


def update_hearing_test_embedded_data_fields(
    survey_template, survey_options, hearing_test_options
):
    """Update hearing test embedded data fields.
    Args:
        survey_template(dict): JSON input QSF qualtrics file.
        survey_options (dict): survey options dictionary.
        hearing_test_options (dict): Hearing test id -> (resource_link, value) dict.
    Returns:
        survey_data(dict): Updated version of the survey_data JSON file.
    """
    logger = logging.getLogger(__name__)

    # set up hearing test embedded data
    DEFAULT_HEARING_CORRECT_ANSWERS = 0
    hearing_test_embedded_data = {}
    hearing_test_embedded_data["hearing_correct_answers"] = str(
        DEFAULT_HEARING_CORRECT_ANSWERS
    )
    hearing_test_embedded_data["hearing_threshold"] = str(
        survey_options["hearing_test"]["hearing_test_threshold"]
    )

    # hearing test values
    for ht_id, value in hearing_test_options.items():
        target_digits_value = str(value[1])
        target_digits_id = "ht_audio_{}".format(ht_id)
        hearing_test_embedded_data[target_digits_id] = target_digits_value

    logger.info(
        "UPDATING EMBEDDED DATA FIELDS HEARING TEST {} ".format(
            hearing_test_embedded_data
        )
    )

    # update hearing test values
    survey_template = update_survey_embedded_data_fields(
        survey_template, hearing_test_embedded_data
    )

    return survey_template


def update_training_embedded_data_fields(
    survey_template, survey_options, total_training_questions
):
    """Update training embedded data fields.
    Args:
        survey_template(dict): JSON input QSF qualtrics file.
        survey_options (dict): survey options dictionary.
    Returns:
        survey_data(dict): Updated version of the survey_data JSON file.
    """
    logger = logging.getLogger(__name__)

    training_test_embedded_data = {}
    training_test_embedded_data["train_clean_threshold"] = str(
        survey_options["training"]["clean"]["valid_expected"]
    )
    training_test_embedded_data["train_noisy_threshold"] = str(
        survey_options["training"]["noisy"]["valid_expected"]
    )
    training_test_embedded_data["train_total_clean"] = str(
        survey_options["training"]["clean"]["number_files"]
    )
    training_test_embedded_data["train_total_noisy"] = str(
        survey_options["training"]["noisy"]["number_files"]
    )
    training_test_embedded_data["total_training_questions"] = total_training_questions

    logger.info(
        "UPDATING EMBEDDED DATA FIELDS TRAINING TEST {} ".format(
            training_test_embedded_data
        )
    )

    # update training test values
    survey_template = update_survey_embedded_data_fields(
        survey_template, training_test_embedded_data
    )

    return survey_template


def update_validation_embedded_data_fields(
    survey_template, survey_options, total_main_questions
):
    """Update validation embedded data fields.
    Args:
        survey_template(dict): JSON input QSF qualtrics file.
        survey_options (dict): survey options dictionary.
    Returns:
        survey_data(dict): Updated version of the survey_data JSON file.
    """
    logger = logging.getLogger(__name__)

    validation_test_embedded_data = {}
    validation_test_embedded_data["main_clean_threshold"] = str(
        survey_options["validation"]["clean"]["valid_expected"]
    )
    validation_test_embedded_data["main_noisy_threshold"] = str(
        survey_options["validation"]["noisy"]["valid_expected"]
    )
    validation_test_embedded_data["main_total_clean"] = str(
        survey_options["validation"]["clean"]["number_files"]
    )
    validation_test_embedded_data["main_total_noisy"] = str(
        survey_options["validation"]["noisy"]["number_files"]
    )
    validation_test_embedded_data["total_main_questions"] = str(total_main_questions)

    logger.info(
        "UPDATING EMBEDDED DATA FIELDS VALIDATION TEST {} ".format(
            validation_test_embedded_data
        )
    )

    # update validation test values
    survey_template = update_survey_embedded_data_fields(
        survey_template, validation_test_embedded_data
    )

    return survey_template


def update_qsf_template_with_experiment_data(
    survey_template,
    hearing_test_options,
    df_training_block,
    df_survey,
    survey_target_language,
):
    """Update QSF template with experiment data.
    The experiment data consists of the hearing test options, the training audio files
    and the survey (main task) files.
    
    Args:
        survey_template(dict): JSON input QSF qualtrics file.
        hearing_test_options (dict): Hearing test id -> (resource_link, value) dict.
        df_training_block (pd.DataFrame): Training block dataframe. Training questions.
        df_survey(pd.DataFrame): Survey (testing + validation) dataframe. Experiment questions. 
        survey_target_language (str): Survey target language.
    Returns:
        survey_data(dict): Updated version of the survey_data JSON file.
    """
    logger = logging.getLogger(__name__)

    logger.info("SETTING UP SURVEY HEARING TEST INSIDE QSF FILE")
    survey_template = update_survey_hearing_test_block(
        survey_data=survey_template, hearing_test_options=hearing_test_options
    )

    logger.info("SETTING UP TRAINING QUESTIONS INSIDE THE QSF FILE")
    df_training_block = prepare_training_questions(
        training_df=df_training_block, survey_data=survey_template
    )
    survey_template = update_survey_training_questions(
        survey_data=survey_template, training_df=df_training_block
    )

    logger.info("SETTING UP SURVEY QUESTIONS INSIDE QSF FILE")
    df_survey = prepare_testing_questions(
        testing_df=df_survey, survey_data=survey_template
    )
    survey_template = update_survey_testing_questions(
        survey_data=survey_template, testing_df=df_survey
    )

    logger.info("SETTING UP SURVEY FLOW WITH NEW TESTING BLOCKS")
    survey_template = update_survey_testing_flow(survey_template)

    logger.info("SETTING UP SURVEY TARGET LANGUAGE: {}".format(survey_target_language))
    survey_template = update_survey_target_language(
        survey_data=survey_template, survey_target_language=survey_target_language
    )

    return survey_template


def save_survey_metadata(
    survey_template, experiment_name_hash, output_dir, df_training_block, df_survey
):
    """Save survey metadata.
    Save QSF file, training and survey csv. This metadata can be used to verify
    the set up of the survey.
    
    Args:
        survey_template (dict): JSON input QSF qualtrics file.
        experiment_name_hash (str): hash name of the experiment.
        output_dir (str): output directory of the metadata.
        df_training_block (pd.DataFrame): Dataframe containing the training metadata.
        df_survey (pd.DataFrame): Dataframe containing the survey metadata (testing + validation).
        
    Returns:
        None
    """
    logger = logging.getLogger(__name__)

    qsf_file_target_location = os.path.join(
        output_dir, "survey_qualtrics_{}.qsf".format(experiment_name_hash)
    )

    logger.info("SURVEY QSF FILE OUTPUT LOCATION: {}".format(qsf_file_target_location))

    with open(qsf_file_target_location, "w") as outfile:
        json.dump(survey_template, outfile, indent=4)

    logger.info("SURVEY QSF FILE SAVED!")

    logger.info("SAVING METADATA:")
    training_block_output_path = os.path.join(output_dir, "meta_training.csv")
    survey_block_output_path = os.path.join(output_dir, "meta_survey.csv")

    df_training_block.to_csv(training_block_output_path, index=None, header=True)
    df_survey.to_csv(survey_block_output_path, index=None, header=True)

    logger.info("SAVED TRAINING: {} ".format(training_block_output_path))
    logger.info("SAVED SURVEY: {} ".format(survey_block_output_path))
