"""
Cisco Systems, Inc. and its affiliates
"""
"""
Template helper utilities for questions in the survey.
"""
import pandas as pd
import sys
import os
import random
import copy
import json

from templates.templates.block_templates import (
    TRAINING_QUESTION,
    TESTING_QUESTION,
    BLOCK_TEMPLATE,
    FLOW_BLOCK_TEMPLATE,
)


def create_training_question(
    surveyID, export_tag, question_id, training_type, target, alternatives, audio_link
) -> dict:
    """Create a new training question. 
    
    Args:
        surveyID (str): ID of the survey 
        export_tag (str): export tag 
        question_id (int): question ID. i.e QIDXX
        training_type (string): 'noisy', 'clean', 'ambiguous'
        target (string): target (ground thruth label)
        alternatives (list): alternative list of labels
        audio_link (string): audio link
    Return:
        survey element (dict): survey element template
    """

    assert training_type in ["noisy", "clean", "ambiguous"]

    audio_placeholder = "AUDIO_LINK_PLACEHOLDER"
    training_type_placeholder = "TRAINING_TYPE_PLACEHOLDER"
    export_tag_placeholder = "EXPORT_TAG_PLACEHOLDER"

    # get a new
    new_training_question = copy.deepcopy(TRAINING_QUESTION)

    # change training type placeholder
    new_training_question["Payload"]["QuestionJS"] = new_training_question["Payload"][
        "QuestionJS"
    ].replace(training_type_placeholder, training_type)

    # change audio URL
    new_training_question["Payload"]["QuestionText"] = new_training_question["Payload"][
        "QuestionText"
    ].replace(audio_placeholder, audio_link)
    new_training_question["Payload"]["QuestionText_Unsafe"] = new_training_question[
        "Payload"
    ]["QuestionText_Unsafe"].replace(audio_placeholder, audio_link)

    # change audio URL other languages
    available_languages = new_training_question["Payload"]["Language"].keys()
    for current_language in available_languages:
        new_training_question["Payload"]["Language"][current_language][
            "QuestionText"
        ] = new_training_question["Payload"]["Language"][current_language][
            "QuestionText"
        ].replace(
            audio_placeholder, audio_link
        )

    # prepare alternatives
    current_choise_index = 1
    choises = {str(current_choise_index): {"Display": target}}

    for alternative in alternatives:
        current_choise_index += 1
        choises[str(current_choise_index)] = {"Display": alternative}

    choise_order = [int(item) for item in choises.keys()]

    new_training_question["Payload"]["Choices"] = choises
    new_training_question["Payload"]["ChoiceOrder"] = choise_order

    # change target and alternatives for the other languages
    for current_language in available_languages:
        new_training_question["Payload"]["Language"][current_language][
            "Choices"
        ] = choises

    # change surveyID
    new_training_question["SurveyID"] = surveyID

    # replace export tag
    new_training_question["Payload"]["DataExportTag"] = export_tag

    # change question_id
    new_training_question["PrimaryAttribute"] = question_id
    new_training_question["Payload"]["QuestionID"] = question_id

    return new_training_question


def create_testing_question(
    surveyID,
    export_tag,
    question_id,
    testing_type,
    target,
    alternatives,
    audio_link,
    is_validation,
) -> dict:
    """Create a new testing question. 
    
    Args:
        surveyID (str): ID of the survey 
        export_tag (str): export tag 
        question_id (int): question ID. i.e QIDXX
        testing_type (string): 'noisy', 'clean'
        target (string): target (ground thruth label)
        alternatives (list): alternative list of labels
        audio_link (string): audio link
    Return:
        survey element (dict): survey element template
    """

    assert is_validation in [True, False]
    if is_validation == True:
        assert testing_type in ["noisy", "clean"]

    is_validation_response = "true" if is_validation == True else "false"

    audio_placeholder = "AUDIO_LINK_PLACEHOLDER"
    testing_type_placeholder = "TESTING_TYPE_PLACEHOLDER"
    export_tag_placeholder = "EXPORT_TAG_PLACEHOLDER"
    is_validation_placeholder = "IS_VALIDATION_PLACEHOLDER"

    # get a new
    new_testing_question = copy.deepcopy(TESTING_QUESTION)

    # change testing type placeholder
    if is_validation == True:
        new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
            "QuestionJS"
        ].replace(testing_type_placeholder, testing_type)
    else:
        new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
            "QuestionJS"
        ].replace(testing_type_placeholder, "testing")

    # change audio URL
    new_testing_question["Payload"]["QuestionText"] = new_testing_question["Payload"][
        "QuestionText"
    ].replace(audio_placeholder, audio_link)
    new_testing_question["Payload"]["QuestionText_Unsafe"] = new_testing_question[
        "Payload"
    ]["QuestionText_Unsafe"].replace(audio_placeholder, audio_link)

    # change audio URL other languages
    available_languages = new_testing_question["Payload"]["Language"].keys()
    for current_language in available_languages:
        new_testing_question["Payload"]["Language"][current_language][
            "QuestionText"
        ] = new_testing_question["Payload"]["Language"][current_language][
            "QuestionText"
        ].replace(
            audio_placeholder, audio_link
        )

    # prepare alternatives
    current_choise_index = 1
    choises = {str(current_choise_index): {"Display": target}}

    for alternative in alternatives:
        current_choise_index += 1
        choises[str(current_choise_index)] = {"Display": alternative}

    choise_order = [int(item) for item in choises.keys()]

    new_testing_question["Payload"]["Choices"] = choises
    new_testing_question["Payload"]["ChoiceOrder"] = choise_order

    # change target and alternatives for the other languages
    for current_language in available_languages:
        new_testing_question["Payload"]["Language"][current_language][
            "Choices"
        ] = choises

    # change surveyID
    new_testing_question["SurveyID"] = surveyID

    # replace export tag
    new_testing_question["Payload"]["DataExportTag"] = export_tag

    # change question_id
    new_testing_question["PrimaryAttribute"] = question_id
    new_testing_question["Payload"]["QuestionID"] = question_id

    # change isValidation
    new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
        "QuestionJS"
    ].replace(is_validation_placeholder, is_validation_response)

    return new_testing_question
