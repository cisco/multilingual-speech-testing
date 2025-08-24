"""
Cisco Systems, Inc. and its affiliates
"""
"""
Validation utils for MUSHRA survey test generation

validation of the json input.
"""

import os
import pandas as pd
import logging

def validate_json_input(args_dict):
    """Validate MUSHRA json input.

    Args:
        args_dict (json): argument dictionary.

    Returns:
        None

    Exceptions:
        AssertionError
    """
    # Check survey config parameters
    survey_config_keys = [
        "experiment_name",
        "testing_metafile",
        "target_filename_column",
        "output_dir",
    ]

    # Validate all keys from the survey_config exists
    assert "survey_config" in args_dict.keys()
    for validation_key in survey_config_keys:
        assert (
            validation_key in args_dict["survey_config"].keys()
        ), "Missing parameter: {}, type: dictionary".format(validation_key)

        assert (
            not args_dict["survey_config"][validation_key] is None
        ), "Null parameter: {},  type: string".format(validation_key)

    # Check seed parameter
    survey_option = "seed"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    current_seed = args_dict["survey_options"][survey_option]
    if not current_seed is None:
        assert isinstance(current_seed, int)

    # Check target question parameter
    survey_option = "survey_question"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    survey_question = args_dict["survey_options"][survey_option]

    assert survey_question != "", "Target question can not be empty"
    assert not survey_question is None, "Target question can not be null"

    # Check training section
    survey_option = "training_set"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    training_section = args_dict["survey_options"][survey_option]

    # Validate dynamic training thresholds
    survey_option = "training_pass_threshold"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    survey_option = "training_attempts_limit"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    # Check block defintion
    survey_option = "blocks"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    survey_blocks = args_dict["survey_options"][survey_option]
    number_of_blocks = survey_blocks["number_of_blocks"]
    number_of_questions_per_block = survey_blocks["number_of_questions_per_block"]
    file_assignment = survey_blocks["file_assignment"]

    assert not (
        (not number_of_blocks is None) and (not number_of_questions_per_block is None)
    ), "The parameters: number_of_blocks and number_of_questions_per_block, can not be defined and the same time."

    valid_file_assignment_options = ["random", "ordered"]
    assert (
        file_assignment in valid_file_assignment_options
    ), f"The file_assignment in the survey_options should be one of: {valid_file_assignment_options}"

    # Validate reference threshold
    survey_option = "ref_threshold"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)
    assert (
        not args_dict["survey_options"][survey_option] is None
    ), "reference threshold can not be null"
    assert args_dict["survey_options"][survey_option] in range(
        0, 101
    ), "reference threshold should be in the range [0,100]"

    reference_threshold = args_dict["survey_options"][survey_option]

    # validate anchor threshold
    survey_option = "anchor_threshold"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    if args_dict["survey_options"][survey_option]:
        assert args_dict["survey_options"][survey_option] in range(
            0, 101
        ), "anchor threshold should be in the range [0,100]"

    # Validate anchor threshold
    survey_option = "anchor_min_distance_wrt_reference"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    if args_dict["survey_options"][survey_option]:
        assert args_dict["survey_options"][survey_option] in range(
            0, 101
        ), "anchor min distance wrt to the reference should be in the range [0,100]"

        anchor_max_distance_wrt_reference = args_dict["survey_options"][survey_option]

        # Assert the anchor threshold is not negative
        assert (
            reference_threshold - anchor_max_distance_wrt_reference
        ) > 0, "The anchor max distance wrt to the reference should be > 0"

    # Validate only one parameter can be defined.
    anchor_max_distance_wrt_reference = args_dict["survey_options"][
        "anchor_min_distance_wrt_reference"
    ]
    anchor_threshold = args_dict["survey_options"]["anchor_threshold"]

    # Validate that only one of the two parameters can be defined at a time
    assert (
        (anchor_max_distance_wrt_reference is None) != (anchor_threshold is None)
    ), "Either 'anchor_min_distance_wrt_reference' or 'anchor_threshold' must be defined, but not both."

    # Validate correct answers threshold
    survey_option = "correct_answers_threshold"
    assert (
        survey_option in args_dict["survey_options"].keys()
    ), "Missing parameter: {}, type: dictionary".format(survey_option)

    # Validate anchor and ref correct answets
    anchor_threshold_key = "anchor_correct_answers"
    assert (
        anchor_threshold_key in args_dict["survey_options"][survey_option].keys()
    ), "Missing parameter: {}, type dictionary".format(anchor_threshold_key)

    # Validate anchor and ref correct answets
    ref_threshold_key = "ref_correct_answers"
    assert (
        ref_threshold_key in args_dict["survey_options"][survey_option].keys()
    ), "Missing parameter: {}, type dictionary".format(ref_threshold_key)

    # Validate testing metafile
    testing_metafile_path = args_dict["survey_config"]["testing_metafile"]
    target_filepath_column = args_dict["survey_config"]["target_filename_column"]

    assert os.path.exists(
        testing_metafile_path
    ), "The provided testing metafile does not exists: {}".format(testing_metafile_path)

    # Validate conditions
    df_testing = pd.read_csv(testing_metafile_path)
    validate_survey_testing_input(df_testing, target_filepath_column)


def validate_survey_testing_input(df_testing, target_column):
    """Validate MIP survey testing dataframe.

    Args:
        df_testing (pd.DataFrame): testing dataframe.
        target_column (str): target column to index files.
        conditions (list): list of dicts {name -> path}.
    Returns:
        None

    Raises:
        AssertionError: Missing column
        AssertionError: None values
    """

    # Check size
    assert len(df_testing) > 0, "Zero length DataFrame, size: {}".format(
        len(df_testing)
    )

    mandatory_columns = [target_column, "condition", "resource_link"]

    # Check mandatory columns
    for column in mandatory_columns:
        assert column in df_testing.columns.tolist(), "Missing column: {} ".format(
            column
        )
        assert (
            not df_testing[column].isnull().values.any()
        ), "NaN/None values detected in column: {} ".format(column)

    target_filename_set = set(
        [item.split(".")[0] for item in df_testing[target_column].tolist()]
    )

    # Assert one of the names is "ref"
    condition_names = [
        item for item in set(df_testing["condition"].tolist())
    ]
    assert (
        "ref" in condition_names
    ), "The condition: 'ref' must exists in the conditions to run the test"
    assert (
        "anchor" in condition_names
    ), "The condition: 'anchor' must exists in the conditions to run the test"
    
    # Check file exists in all conditions
    for condition in condition_names:
        # files exists in every condition
        # For each unique filename, check if both 'ref' and 'anchor' conditions exist
        for filename in target_filename_set:
            conditions_for_file = df_testing[df_testing[target_column].str.startswith(filename)]['condition'].unique()
            assert condition in conditions_for_file, f"File '{filename}' is missing '{condition}' condition."
