"""
Cisco Systems, Inc. and its affiliates
"""
"""
Validation utilities for input files.
"""
import pandas as pd
import sys
import os
import json
import logging


def read_hearing_test_metafile(filepath):
    """Validate hearing test metafile.
    The hearing test containst the audio files used to validate the participants in the survey. 
    Args:
        filepath (str): Input hearing test csv.
    Returns
        input_df (pd.DataFrame): hearing test dataframe
    Raise:
        AssertionError: Missing column
        AssertionError: None values
        AssertionError: Size equal 0   
    """
    logger = logging.getLogger(__name__)
    assert os.path.exists(
        filepath
    ), "The hearing test metafile does not exists, {}".format(filepath)
    input_df = pd.read_csv(filepath, dtype={"target": str})

    # check size
    assert len(input_df) > 0, "Zero length DataFrame, size: {}".format(len(input_df))
    assert (
        len(input_df) == 6
    ), "The hearing test files should be 6, current size: {}".format(len(input_df))

    MANDATORY_COLUMNS = ("filename", "target", "resource_link")

    # check mandatory columns
    for column in MANDATORY_COLUMNS:
        assert column in input_df.columns.tolist(), "Missing column: {} ".format(column)
        assert (
            not input_df[column].isnull().values.any()
        ), "NaN/None values detected in column: {} ".format(column)

    logger.info(
        "HEARING TEST => NUMBER OF AUDIO FILES: {}, # UNIQUE AUDIO FILES {}, # UNIQUE LINKS {}".format(
            len(input_df),
            input_df.filepath.unique().size,
            input_df.resource_link.unique().size,
        )
    )
    return input_df


def read_training_metafile(filepath):
    """Validate input training metafile.
    The training metafile contains the information of the training before
    the main survey. 
    Args:
        filepath (str): Input training csv.
    Returns
        input_df (pd.DataFrame): training dataframe.
    Raise:
        AssertionError: Missing column
        AssertionError: None values
        AssertionError: Size equal 0   
    """
    logger = logging.getLogger(__name__)
    assert os.path.exists(filepath), "The training metafile does not exists, {}".format(
        filepath
    )
    input_df = pd.read_csv(filepath)

    # check size
    assert len(input_df) > 0, "Zero length DataFrame, size: {}".format(len(input_df))

    MANDATORY_COLUMNS = ("filename", "type", "target", "resource_link")

    # check mandatory columns
    for column in MANDATORY_COLUMNS:
        assert column in input_df.columns.tolist(), "Missing column: {} ".format(column)
        assert (
            not input_df[column].isnull().values.any()
        ), "NaN/None values detected in column: {} ".format(column)

    # check alternative column (at least one)
    assert any(
        ["alternative" in column for column in input_df.columns.tolist()]
    ), "No alternative columns were provided. columns {} ".format(
        input_df.columns.tolist()
    )

    logger.info(
        "TRAINING => NUMBER OF AUDIO FILES: {}, # UNIQUE AUDIO FILES {}, # UNIQUE LINKS {}".format(
            len(input_df),
            input_df.filepath.unique().size,
            input_df.resource_link.unique().size,
        )
    )
    return input_df


def read_validation_metafile(filepath):
    """Validate input validation metafile.
    The validation metafile contains the information of the files used to
    validate (anti-cheating validations) the participants in the main survey. 
    Args:
        filepath (str): Input validation csv.
    Returns
        input_df (pd.DataFrame): validation dataframe.
    Raise:
        AssertionError: Missing column
        AssertionError: None values
        AssertionError: Size equal 0   
    """
    logger = logging.getLogger(__name__)
    assert os.path.exists(
        filepath
    ), "The validation metafile does not exist, {}".format(filepath)
    input_df = pd.read_csv(filepath)

    # check size
    assert len(input_df) > 0, "Zero length DataFrame, size: {}".format(len(input_df))

    MANDATORY_COLUMNS = ("filename", "block", "target", "resource_link")

    # check mandatory columns
    for column in MANDATORY_COLUMNS:
        assert column in input_df.columns.tolist(), "Missing column: {} ".format(column)
        assert (
            not input_df[column].isnull().values.any()
        ), "NaN/None values detected in column: {} ".format(column)

    # check alternative column (at least one)
    assert any(
        ["alternative" in column for column in input_df.columns.tolist()]
    ), "No alternative columns were provided. columns {} ".format(
        input_df.columns.tolist()
    )

    logger.info(
        "VALIDATION => NUMBER OF AUDIO FILES: {}, # UNIQUE AUDIO FILES {}, # UNIQUE LINKS {}".format(
            len(input_df),
            input_df.filepath.unique().size,
            input_df.resource_link.unique().size,
        )
    )

    return input_df


def read_survey_experiment_input_metafile(filepath):
    """Validate survey experiment input metafile   

    Args:
        filepath (str): Input experiment csv.
    
    Returns:
        input_df (pd.DataFrame): experiment (survey) dataframe.
    Raises:
        AssertionError: Missing column
        AssertionError: None values
        AssertionError: Size equal 0        
    """
    logger = logging.getLogger(__name__)
    assert os.path.exists(
        filepath
    ), "The experiment metafile does not exist, {}".format(filepath)
    input_df = pd.read_csv(filepath)

    # check size
    assert len(input_df) > 0, "Zero length DataFrame, size: {}".format(len(input_df))

    MANDATORY_COLUMNS = ("filename", "block", "target", "resource_link")

    # check mandatory columns
    for column in MANDATORY_COLUMNS:
        assert column in input_df.columns.tolist(), "Missing column: {} ".format(column)
        assert (
            not input_df[column].isnull().values.any()
        ), "NaN/None values detected in column: {} ".format(column)

    # check alternative column (at least one)
    assert any(
        ["alternative" in column for column in input_df.columns.tolist()]
    ), "No alternative columns were provided. columns {} ".format(
        input_df.columns.tolist()
    )

    logger.info(
        "TESTING => NUMBER OF AUDIO FILES: {}, # UNIQUE AUDIO FILES {}, # UNIQUE LINKS {}".format(
            len(input_df),
            input_df.filepath.unique().size,
            input_df.resource_link.unique().size,
        )
    )

    return input_df


def validate_test_language(survey_target_language, supported_languages):
    """Validate target language.
    Args:
        survey_target_language (str): Survey target language.
        
    Raises:
        AssertionError: missing internal configuration file.
        AssertionError: survey target language not supported.         
    """
    assert (
        survey_target_language in supported_languages
    ), "The target language {} is not supported. Supported list: {}".format(
        survey_target_language, supported_languages
    )


def validate_json_input(args_dict):
    """Validate json experiment configuration input.
    Args:
        args_dict (json): argument dictionary.
    Returns:
        None
    Exceptions:
        AssertionError        
    """
    # check survey config parameters
    survey_config_keys = [
        "experiment_metafile",
        "experiment_name",
        "test_language",
        "payment_rate",
        "bonus",
        "output_dir",
    ]
    qualtrics_qsf_keys = []

    assert "survey_config" in args_dict.keys()
    for validation_key in survey_config_keys:
        assert (
            validation_key in args_dict["survey_config"].keys()
        ), "Missing parameter: {}, type: dictionary".format(validation_key)
        assert (
            not args_dict["survey_config"][validation_key] is None
        ), "Null parameter: {},  type: string".format(validation_key)

    # test internal configuration
    internal_config_path = "supported-languages/languages_speech_intelligibility_test.json"
    assert os.path.exists(
        internal_config_path
    ), "The internal configuration does not exist: {}".format(internal_config_path)

    with open(internal_config_path) as f:
        internal_config = json.load(f)

    supported_languages = [
        item.lower()
        for item in internal_config["qualtrics_supported_languages"].values()
    ]

    # check test_language
    target_deployment_language = args_dict["survey_config"]["test_language"]
    validate_test_language(target_deployment_language, supported_languages)

    # check hearing test
    survey_option = "hearing_test"
    assert "survey_options" in args_dict.keys()

    # assert missing or null
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option] is None
    ), "Null parameter: {},  type: string".format(survey_option)

    # assert missing or null over the metafile
    assert (
        "hearing_test_metafile" in args_dict["survey_options"]["hearing_test"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["hearing_test_metafile"] is None
    ), "Null parameter: {},  type: string".format(survey_option)

    # assert missing or null over the hearing test threshold
    assert (
        "hearing_test_threshold" in args_dict["survey_options"]["hearing_test"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["hearing_test_threshold"] is None
    ), "Null parameter: {},  type: string".format(survey_option)

    # check training parameters
    survey_option = "training"
    assert "survey_options" in args_dict.keys()
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option] is None
    ), "Null parameter: {},  type: string".format(survey_option)

    assert (
        not args_dict["survey_options"][survey_option]["clean"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["clean"]["number_files"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["clean"]["valid_expected"]
        is None
    ), "Null parameter: {},  type: string".format(survey_option)

    assert (
        not args_dict["survey_options"][survey_option]["noisy"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["noisy"]["number_files"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["noisy"]["valid_expected"]
        is None
    ), "Null parameter: {},  type: string".format(survey_option)

    # assert missing or null over the metafile
    assert (
        "training_metafile" in args_dict["survey_options"]["training"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["training_metafile"] is None
    ), "Null parameter: {},  type: string".format(survey_option)

    # check validation parameters
    survey_option = "validation"
    assert "survey_options" in args_dict.keys()
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option] is None
    ), "Null parameter: {},  type: string".format(survey_option)

    assert (
        not args_dict["survey_options"][survey_option]["clean"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["clean"]["number_files"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["clean"]["valid_expected"]
        is None
    ), "Null parameter: {},  type: string".format(survey_option)

    assert (
        not args_dict["survey_options"][survey_option]["noisy"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["noisy"]["number_files"] is None
    ), "Null parameter: {},  type: string".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["noisy"]["valid_expected"]
        is None
    ), "Null parameter: {},  type: string".format(survey_option)

    # assert missing or null over the metafile
    assert (
        "validation_metafile" in args_dict["survey_options"]["validation"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option]["validation_metafile"] is None
    ), "Null parameter: {},  type: string".format(survey_option)

    # check seed
    survey_option = "seed"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    current_seed = args_dict["survey_options"][survey_option]
    if not current_seed is None:
        assert isinstance(current_seed, int)
