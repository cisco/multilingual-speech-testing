"""
Cisco Systems, Inc. and its affiliates
"""
"""
MUSHRA question helpers
"""
import copy
import uuid

from templates.block_templates import (
    TESTING_QUESTION,
    PASSIVE_TRAINING_QUESTION,
    DYNAMIC_TRAINING_QUESTION,
    CHOISE_TEMPLATE,
    CHOISE_TRAINING_TEMPLATE,
    TRAINING_REFERENCE_QUESTION_TEMPLATE,
)


def create_training_text_question(reference_link):
    """Create a training text question.

    Args:
        reference_link (dict): reference link.

    Return
        str
    """
    REFERENCE_LINK_PLACEHOLDER = "REFERENCE_LINK"

    return TRAINING_REFERENCE_QUESTION_TEMPLATE.replace(
        REFERENCE_LINK_PLACEHOLDER, reference_link
    )


def create_training_choice_template(condition_links) -> dict:
    """Create a new training choise template.
    The dynamic training section has links that should change depending on the
    set used. These sets are questions with 4 questions:
        - ref: Reference, best example in the survey.
        - good: Good example, not as good as the reference.
        - poor: Poor example, lower quality compare with the good example.
        - anchor: The lowest quality example.

    Args:
        condition_links (dict): condition -> links

    Return
        choice_training_template (dict)
    """
    ANCHOR_LINK_PLACEHOLDER = "ANCHOR_LINK"
    CONDITION_1_LINK_PLACEHOLDER = "CONDITION_1_LINK"
    CONDITION_2_LINK_PLACEHOLDER = "CONDITION_2_LINK"
    REFERENCE_LINK_PLACEHOLDER = "REFERENCE_LINK"

    choice_training_template = copy.deepcopy(CHOISE_TRAINING_TEMPLATE)

    # Set anchor
    choice_training_template["1"]["Display"] = choice_training_template["1"][
        "Display"
    ].replace(ANCHOR_LINK_PLACEHOLDER, condition_links["anchor"])

    # Set condition_1 (good)
    choice_training_template["2"]["Display"] = choice_training_template["2"][
        "Display"
    ].replace(CONDITION_1_LINK_PLACEHOLDER, condition_links["good"])

    # Set condition_2 (poor)
    choice_training_template["3"]["Display"] = choice_training_template["3"][
        "Display"
    ].replace(CONDITION_2_LINK_PLACEHOLDER, condition_links["poor"])

    # Set reference
    choice_training_template["4"]["Display"] = choice_training_template["4"][
        "Display"
    ].replace(REFERENCE_LINK_PLACEHOLDER, condition_links["ref"])

    return choice_training_template


def create_testing_question(
    surveyID,
    export_tag,
    question_id,
    block_id,
    show_reference_in_header,
    target_question,
    conditions_link_map,
) -> dict:
    """Create a new testing question.
    The testing question for MUSHRA is composed of multiple audio files (conditions),
    and a target question.

    Args:
        surveyID (str): ID of the survey.
        export_tag (str): export tag.
        question_id (int): question ID. i.e QIDXX.
        block_id (int): Block ID of the question.
        show_reference_in_header (boolean): show reference in header (true|false)
        target_question(str): target question.
        conditions_link_map (dict): Conditions -> links mapping condition -> audio_link.
    Return:
        survey element (dict): survey element template
    """

    QUESTION_ID_PLACEHOLDER = "QUESTION_ID"
    QUESTION_TEXT_PLACEHOLDER = "QUESTION_TEMPLATE"

    AUDIO_ID_REFERENCE_PLACEHOLDER = "AUDIO_ID_REFERENCE"
    AUDIO_LINK_REFERENCE_PLACEHOLDER = "AUDIO_LINK_REFERENCE"

    AUDIO_ID_CONDITION_PLACEHOLDER = "AUDIO_ID"
    AUDIO_LINK_CONDITION_PLACEHOLDER = "AUDIO_LINK"

    ANCHOR_INDEX_PLACEHOLDER = "ANCHOR_INDEX"
    REF_INDEX_PLACEHOLDER = "REF_INDEX"
    # QUESTION_BLOCK_PLACEHOLDER = "QUESTION_BLOCK"

    # Copy template for question
    new_testing_question = copy.deepcopy(TESTING_QUESTION)

    # Update question ID (primary attribute)
    new_testing_question["PrimaryAttribute"] = question_id
    new_testing_question["Payload"]["QuestionID"] = question_id

    # Update question text (secondary attribue)
    new_testing_question["SecondaryAttribute"] = new_testing_question[
        "SecondaryAttribute"
    ].replace(QUESTION_TEXT_PLACEHOLDER, target_question)

    # Reference audio
    reference_audio_id = "ref"
    reference_audio_link = conditions_link_map[reference_audio_id]

    if show_reference_in_header is True:
        # Replace target question
        new_testing_question["Payload"]["QuestionText"] = new_testing_question[
            "Payload"
        ]["QuestionText"].replace(QUESTION_TEXT_PLACEHOLDER, target_question)

        # Update audio ID and audio URL
        new_testing_question["Payload"]["QuestionText"] = new_testing_question[
            "Payload"
        ]["QuestionText"].replace(AUDIO_ID_REFERENCE_PLACEHOLDER, str(uuid.uuid4()))

        # Update audio URL for Reference and Sample links
        new_testing_question["Payload"]["QuestionText"] = new_testing_question[
            "Payload"
        ]["QuestionText"].replace(
            AUDIO_LINK_REFERENCE_PLACEHOLDER, reference_audio_link
        )

        # Update question description
        new_testing_question["Payload"]["QuestionDescription"] = new_testing_question[
            "Payload"
        ]["QuestionDescription"].replace(QUESTION_TEXT_PLACEHOLDER, target_question)

    else:
        # Cut original text
        question_template_no_reference = new_testing_question["Payload"][
            "QuestionText"
        ].split("QUESTION_TEMPLATE")[0]

        # Set text
        new_testing_question["Payload"]["QuestionText"] = (
            question_template_no_reference + target_question
        )

    # Update slider start positions
    number_of_conditions = len(conditions_link_map) + 1
    slider_start_position = {int(index): 0 for index in range(1, number_of_conditions)}
    new_testing_question["Payload"]["Configuration"][
        "SliderStartPositions"
    ] = slider_start_position

    # Update choice order
    choise_order = list(range(1, number_of_conditions))
    new_testing_question["Payload"]["ChoiceOrder"] = choise_order

    # Update all condition
    condition_mapping = {}
    condition_choises = {}
    condition_index = 1
    REF_INDEX = None
    ANCHOR_INDEX = None

    for condition, question_link in conditions_link_map.items():
        condition_mapping[condition] = condition_index
        new_choise_template = copy.deepcopy(CHOISE_TEMPLATE)

        new_choise_template["Display"] = new_choise_template["Display"].replace(
            AUDIO_ID_CONDITION_PLACEHOLDER,   str(uuid.uuid4())
        )

        new_choise_template["Display"] = new_choise_template["Display"].replace(
            AUDIO_LINK_CONDITION_PLACEHOLDER, question_link
        )

        if condition == "ref":
            REF_INDEX = condition_index

        if condition == "anchor":
            ANCHOR_INDEX = condition_index

        # Save condtion
        condition_choises[str(condition_index)] = new_choise_template
        condition_index += 1

    # Set new conditions
    new_testing_question["Payload"]["Choices"] = condition_choises

    # Update javascript constants
    # Update ANCHOR INDEX
    new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
        "QuestionJS"
    ].replace(ANCHOR_INDEX_PLACEHOLDER, str(ANCHOR_INDEX))

    # Update REF INDEX
    new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
        "QuestionJS"
    ].replace(REF_INDEX_PLACEHOLDER, str(REF_INDEX))

    # Update surveyID
    new_testing_question["SurveyID"] = surveyID

    # Update export tag
    new_testing_question["Payload"]["DataExportTag"] = export_tag

    return new_testing_question, condition_mapping


def create_background_color_maps(score):
    """The passive training examples have an array,
    indicate the background area to color and the
    fading areas.

    Args:
        score (int): subjective score given by the researcher.

    Return:
        list of tuples. (area, opacity)
    """
    assert score > 0 and score <= 100, "Score should be between [0,100]"
    # Max steps to the left and right of the score
    DEFAULT_STEPS = 2
    FULL_OPACITY = 1
    MIDDLE_OPACITY = 0.5
    LOW_OPACITY = 0.25

    # Compute area based on the score
    score_left_limit = score // 10  ## floor to nearest 10
    score_right_limit = score_left_limit + 1  # ceiling + 1

    score_center = [(score_left_limit, FULL_OPACITY), (score_right_limit, FULL_OPACITY)]

    # Left faded areas
    score_left_faded = list(
        range(score_left_limit - DEFAULT_STEPS, score_left_limit, 1)
    )
    score_left_faded = [
        (score_left_faded[0], LOW_OPACITY),
        (score_left_faded[1], MIDDLE_OPACITY),
    ]

    # Right faded areas
    score_right_faded = list(
        range(score_right_limit + 1, score_right_limit + DEFAULT_STEPS + 1, 1)
    )
    score_right_faded = [
        (score_right_faded[0], MIDDLE_OPACITY),
        (score_right_faded[1], LOW_OPACITY),
    ]

    return score_left_faded + score_center + score_right_faded


def create_passive_training_question(
    surveyID,
    export_tag,
    question_id,
    question_description,
    conditions_link_map,
) -> dict:
    """Create a new passive training question.
    The passive training questions for MUSHRA are composed of multiple audio files (conditions),
    and a small description. These questions are templates to help the survey respondents
    calibrate their scoring based on the sample. . Users listen and read observations.

    Args:
        surveyID (str): ID of the survey.
        export_tag (str): export tag.
        question_id (int): question ID. i.e QIDXX.
        question_description (str): Specific condition description.
        conditions_link_map (dict): Conditions -> links mapping condition -> audio_link.
    Return:
        survey element (dict): survey element template
    """

    QUESTION_TEXT_PLACEHOLDER = "QUESTION_TEMPLATE"
    QUESTION_DESCRIPTION_PLACEHOLDER = "TASK_DESCRIPTION"

    AUDIO_ID_REFERENCE_PLACEHOLDER = "AUDIO_ID_REFERENCE"
    AUDIO_LINK_REFERENCE_PLACEHOLDER = "AUDIO_LINK_REFERENCE"

    AUDIO_ID_CONDITION_PLACEHOLDER = "AUDIO_ID"
    AUDIO_LINK_CONDITION_PLACEHOLDER = "AUDIO_LINK"

    BACKGROUND_CONDITION_SCORE_MAP = "BACKGROUND_CONDITION_SCORE_MAP"
    ALPHA_FADE_COLOR_CONDITION_SCORE_MAP = "ALPHA_FADE_COLOR_CONDITION_SCORE_MAP"
    CAPTIONS_PER_CONDITION_CONFIG = "CAPTIONS_PER_CONDITION_CONFIG"

    # Copy template for question
    new_testing_question = copy.deepcopy(PASSIVE_TRAINING_QUESTION)

    # Update question ID (primary attribute)
    new_testing_question["PrimaryAttribute"] = question_id
    new_testing_question["Payload"]["QuestionID"] = question_id

    # Reference audio
    reference_audio_id = "ref"
    reference_condition = conditions_link_map.pop(reference_audio_id)
    reference_audio_link = reference_condition[0]  ## reference audio link

    # Create background condition score map
    background_color_map = {}
    captions_map = {}
    condition_index = 1
    for condition, link_score_caption in conditions_link_map.items():
        score = link_score_caption[1]
        caption = link_score_caption[2]

        # Get background color map
        background_color_map[condition_index] = create_background_color_maps(score)

        # Save captions dictionary
        captions_map[condition_index] = caption
        condition_index += 1

    bg_score_condition_map = {}
    bg_alpha_fade_color_condition_score_map = {}
    for index, bg_color in background_color_map.items():
        # Set positive areas within the limits
        positive_areas = [
            item[0] for item in bg_color if item[0] >= 0 and item[0] <= 10
        ]

        # Set alpha colors within the positive area
        alpha_colors = [item[1] for item in bg_color if item[0] >= 0 and item[0] <= 10]

        bg_score_condition_map[index] = positive_areas
        bg_alpha_fade_color_condition_score_map[index] = alpha_colors

    # Replace target description
    new_testing_question["Payload"]["QuestionText"] = new_testing_question["Payload"][
        "QuestionText"
    ].replace(QUESTION_DESCRIPTION_PLACEHOLDER, question_description)

    # Update audio ID and audio URL
    new_testing_question["Payload"]["QuestionText"] = new_testing_question["Payload"][
        "QuestionText"
    ].replace(AUDIO_ID_REFERENCE_PLACEHOLDER, reference_audio_id)

    # Update audio URL for Reference and Sample links
    new_testing_question["Payload"]["QuestionText"] = new_testing_question["Payload"][
        "QuestionText"
    ].replace(AUDIO_LINK_REFERENCE_PLACEHOLDER, reference_audio_link)

    # Update background condition score map
    new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
        "QuestionJS"
    ].replace(BACKGROUND_CONDITION_SCORE_MAP, str(bg_score_condition_map))

    # Update alpha fade color condition score map
    new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
        "QuestionJS"
    ].replace(
        ALPHA_FADE_COLOR_CONDITION_SCORE_MAP,
        str(bg_alpha_fade_color_condition_score_map),
    )

    # Update captions per condition
    new_testing_question["Payload"]["QuestionJS"] = new_testing_question["Payload"][
        "QuestionJS"
    ].replace(CAPTIONS_PER_CONDITION_CONFIG, str(captions_map))

    # Update slider start positions
    number_of_conditions = len(conditions_link_map) + 1
    slider_start_position = {int(index): 0 for index in range(1, number_of_conditions)}
    new_testing_question["Payload"]["Configuration"][
        "SliderStartPositions"
    ] = slider_start_position

    # Update choice order
    choise_order = list(range(1, number_of_conditions))
    new_testing_question["Payload"]["ChoiceOrder"] = choise_order

    # Update all condition
    condition_mapping = {}
    condition_choises = {}
    condition_index = 1

    for condition, question_link in conditions_link_map.items():
        condition_mapping[condition] = condition_index
        new_choise_template = copy.deepcopy(CHOISE_TEMPLATE)

        new_choise_template["Display"] = new_choise_template["Display"].replace(
            AUDIO_ID_CONDITION_PLACEHOLDER, condition
        )

        new_choise_template["Display"] = new_choise_template["Display"].replace(
            AUDIO_LINK_CONDITION_PLACEHOLDER, question_link[0]
        )

        # Save condtion
        condition_choises[str(condition_index)] = new_choise_template
        condition_index += 1

    # Set new conditions
    new_testing_question["Payload"]["Choices"] = condition_choises

    # Update surveyID
    new_testing_question["SurveyID"] = surveyID

    # Update export tag
    new_testing_question["Payload"]["DataExportTag"] = export_tag

    return new_testing_question, condition_mapping


def create_dynamic_training_question(
    surveyID,
    export_tag,
    question_id,
    conditions_link_map,
) -> dict:
    """Create a new dynamic training question.
    The dynamic training questions for MUSHRA are composed of multiple audio files (conditions),
    and a small description. These questions are templates to help the survey respondents
    calibrate their scoring based on the sample. Users respond and receive feedback based
    on the answers.

    Args:
        surveyID (str): ID of the survey.
        export_tag (str): export tag.
        question_id (int): question ID. i.e QIDXX.
        conditions_link_map (dict): Conditions -> links mapping condition -> audio_link.
    Return:
        survey element (dict): survey element template
    """

    AUDIO_ID_REFERENCE_PLACEHOLDER = "AUDIO_ID_REFERENCE"
    AUDIO_LINK_REFERENCE_PLACEHOLDER = "AUDIO_LINK_REFERENCE"

    AUDIO_ID_CONDITION_PLACEHOLDER = "AUDIO_ID"
    AUDIO_LINK_CONDITION_PLACEHOLDER = "AUDIO_LINK"

    # Copy template for question
    new_dynamic_testing_question = copy.deepcopy(DYNAMIC_TRAINING_QUESTION)

    # Update question ID (primary attribute)
    new_dynamic_testing_question["PrimaryAttribute"] = question_id
    new_dynamic_testing_question["Payload"]["QuestionID"] = question_id

    # Reference audio
    reference_audio_id = "ref"
    reference_audio_link = conditions_link_map[reference_audio_id]

    # Update audio ID and audio URL
    new_dynamic_testing_question["Payload"][
        "QuestionText"
    ] = new_dynamic_testing_question["Payload"]["QuestionText"].replace(
        AUDIO_ID_REFERENCE_PLACEHOLDER,  str(uuid.uuid4())
    )

    # Update audio URL for Reference and Sample links
    new_dynamic_testing_question["Payload"][
        "QuestionText"
    ] = new_dynamic_testing_question["Payload"]["QuestionText"].replace(
        AUDIO_LINK_REFERENCE_PLACEHOLDER, reference_audio_link
    )

    # Update slider start positions
    number_of_conditions = len(conditions_link_map) + 1
    slider_start_position = {int(index): 0 for index in range(1, number_of_conditions)}
    new_dynamic_testing_question["Payload"]["Configuration"][
        "SliderStartPositions"
    ] = slider_start_position

    # Update choice order
    choise_order = list(range(1, number_of_conditions))
    new_dynamic_testing_question["Payload"]["ChoiceOrder"] = choise_order

    # Update all condition
    condition_mapping = {}
    condition_choises = {}
    condition_index = 1

    # Conditions must be added in this order for validation logic.
    for condition in ["anchor", "good", "poor", "ref"]:
        question_link = conditions_link_map[condition]

        condition_mapping[condition] = condition_index
        new_choise_template = copy.deepcopy(CHOISE_TEMPLATE)

        new_choise_template["Display"] = new_choise_template["Display"].replace(
            AUDIO_ID_CONDITION_PLACEHOLDER,  str(uuid.uuid4())
        )

        new_choise_template["Display"] = new_choise_template["Display"].replace(
            AUDIO_LINK_CONDITION_PLACEHOLDER, question_link
        )

        # Save condtion
        condition_choises[str(condition_index)] = new_choise_template
        condition_index += 1

    # Set new conditions
    new_dynamic_testing_question["Payload"]["Choices"] = condition_choises

    # Update surveyID
    new_dynamic_testing_question["SurveyID"] = surveyID

    # Update export tag
    new_dynamic_testing_question["Payload"]["DataExportTag"] = export_tag

    return new_dynamic_testing_question, condition_mapping
