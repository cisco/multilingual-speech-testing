"""
Cisco Systems, Inc. and its affiliates
"""
#!/usr/bin/env python
# coding: utf-8

"""
Subjective Intelligibility test
Create template qsf file to generate tests.

Usage:
python create_sit_test.py -ji configuration_file.json
"""

import pandas as pd
import sys
import os
import argparse
import hashlib
import uuid
import json
import logging
import multiprocessing
from datetime import datetime

from utils.general import (
    get_language_code,
    generate_experiment_seed,
    generate_experiment_name,
    update_payment_embedded_data_fields,
    update_hearing_test_embedded_data_fields,
    update_training_embedded_data_fields,
    update_validation_embedded_data_fields,
    update_qsf_template_with_experiment_data,
    save_survey_metadata,
)

from utils.qsf_survey_preparation import (
    prepare_survey_quotas,
    prepare_survey_dataframe,
)

from utils.validation import (
    validate_json_input,
    read_hearing_test_metafile,
    read_training_metafile,
    read_validation_metafile,
    read_survey_experiment_input_metafile,
)

MAX_JSON_INT_VALUE = 2147483647
BASELINE_QSF_PATH = "templates/baseline_qsf/speech_intelligibility_baseline.qsf"


def main(args):
    """QSF survey preparation generation
    """
    survey_configuration = args.survey_config
    survey_options = args.survey_options

    survey_target_language = survey_configuration["test_language"]
    survey_target_language_code = get_language_code(survey_target_language)

    # generate seed if required
    seed = survey_options["seed"]
    if seed is None:
        seed = generate_experiment_seed()
        args.survey_options["seed"] = seed

    experiment_name = args.survey_config["experiment_name"]
    experiment_name_hash = generate_experiment_name(experiment_name, seed)

    output_dir = args.survey_config["output_dir"]
    output_dir = os.path.join(output_dir, experiment_name, experiment_name_hash)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # set up loggging
    login_output_filepath = os.path.join(output_dir, "survey_generation.log")

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # output file login
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(login_output_filepath, mode="w+"),
            logging.StreamHandler(),
        ],
    )

    logger = logging.getLogger(__name__)
    logger.info("STARTING SIT SURVEY GENERATION")
    logger.info(
        "EXPERIMENT: {}, HASH NAME: {}".format(experiment_name, experiment_name_hash)
    )
    logger.info("OUTPUT DIRECTORY: {} ".format(output_dir))

    # Experiment csv
    experiment_metafile = survey_configuration["experiment_metafile"]

    # Hearing, training and validation csvs
    hearing_test_metafile_path = survey_options["hearing_test"]["hearing_test_metafile"]
    training_metafile_path = survey_options["training"]["training_metafile"]
    validation_metafile_path = survey_options["validation"]["validation_metafile"]

    df_experiment = read_survey_experiment_input_metafile(experiment_metafile)
    df_hearing_test = read_hearing_test_metafile(hearing_test_metafile_path)
    df_training = read_training_metafile(training_metafile_path)
    df_validation = read_validation_metafile(validation_metafile_path)

    # Update qualtrics configuration file.
    logger.info("PREPARE SURVEY: TRAINING, TESTING, AND VALIDATION METAFILES")
    logger.info("EXPERIMENT SEED: {}".format(survey_options["seed"]))

    # generate training block, and survey blocks
    df_training_block, survey_data_mapping = prepare_survey_quotas(
        training_df=df_training,
        validation_df=df_validation,
        testing_df=df_experiment,
        qualtrics_conf=survey_options,
    )

    # generate survey data
    df_survey = prepare_survey_dataframe(survey_data_mapping)

    logger.info(
        "SAMPLED NUMBER OF QUESTIONS IN TRAINING {}".format(len(df_training_block))
    )

    logger.info(
        "TRAINING QUESTIONS TYPES: {}".format(
            str(df_training_block.type.value_counts().to_dict())
        )
    )

    logger.info("NUMBER OF BLOCKS IN THE SURVEY: {}".format(len(survey_data_mapping)))
    logger.info("SURVEY QUESTION TYPES PER BLOCK: ")

    for key, value in survey_data_mapping.items():
        block_distribution_quota = (
            survey_data_mapping[key]["dataset_type"].value_counts().to_dict()
        )
        logger.info(
            "BLOCK: {}, QUESTION TYPES {}".format(key, str(block_distribution_quota))
        )

    # compute total questions on training and testing/main questions.
    total_training_questions = len(df_training_block)
    total_main_questions = df_survey.block.value_counts().max()

    # QSF file preparation
    logger.info("SURVEY QSF FILE PREPARATION")
    with open(BASELINE_QSF_PATH) as f:
        survey_template = json.load(f)

    # update payment embeddeed data fields
    survey_template = update_payment_embedded_data_fields(
        survey_template,
        survey_configuration,
        total_training_questions,
        total_main_questions,
    )

    # update hearing test embedded data fields
    hearing_test_options = {
        str(index + 1): (row["resource_link"], row["target"])
        for index, row in df_hearing_test.iterrows()
    }
    survey_template = update_hearing_test_embedded_data_fields(
        survey_template, survey_options, hearing_test_options
    )

    # set up training embedded data
    survey_template = update_training_embedded_data_fields(
        survey_template, survey_options, total_training_questions
    )

    # set up validation embedded data
    survey_template = update_validation_embedded_data_fields(
        survey_template, survey_options, total_main_questions
    )

    # update survey audio and question metadata
    survey_template = update_qsf_template_with_experiment_data(
        survey_template,
        hearing_test_options,
        df_training_block,
        df_survey,
        survey_target_language_code,
    )

    # save survey metadata
    save_survey_metadata(
        survey_template, experiment_name_hash, output_dir, df_training_block, df_survey
    )

    # save generation recipe
    recipe_filepath = os.path.join(output_dir, "survey_recipe.json")
    with open(recipe_filepath, "w") as out_file:
        recipe_dict = vars(args)
        recipe_dict["user"] = os.environ.get("USER")
        recipe_dict["generation_date"] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        json.dump(recipe_dict, out_file, indent=4)

    logger.info("SURVEY RECIPE: {} ".format(recipe_filepath))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SIT testing generation")

    parser.add_argument(
        "-ji", "--json_input", required=True, type=str, help="json input metafile"
    )

    current_arguments, _ = parser.parse_known_args()
    json_configuration_input = vars(current_arguments).get("json_input", None)

    if not json_configuration_input is None:
        if os.path.exists(json_configuration_input):
            with open(json_configuration_input) as f:
                args = json.load(f)

    print(json.dumps(args, indent=4))

    validate_json_input(args)

    main(argparse.Namespace(**args))
