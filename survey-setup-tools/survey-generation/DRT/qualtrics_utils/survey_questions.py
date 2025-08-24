"""
Cisco Systems, Inc. and its affiliates
"""
"""
Qualtrics survey questions utilities.
"""


def get_current_number_of_questions(survey_data, component_index_survey_map):
    """ Get current number of questions on the survey data.

    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        component_index_survey_map (dict): mapping between the survey component and the index in the json structure. 
    Return:
        (int) Current number of questions in the survey. 
    """

    return int(
        survey_data["SurveyElements"][
            component_index_survey_map["Survey Question Count"]
        ]["SecondaryAttribute"]
    )


def update_survey_number_of_questions(
    survey_data, component_index_survey_map, number_of_questions
):
    """Update the number of questions in the survey
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        component_index_survey_map (dict): mapping between the survey component and the index in the json structure. 
        number_of_questions(int): new number of questions of the survey
    Return:
        survey_data (dict): updated survey data
    """

    survey_data["SurveyElements"][component_index_survey_map["Survey Question Count"]][
        "SecondaryAttribute"
    ] = str(number_of_questions)
    return survey_data


def insert_question_referecences_on_block(survey_data, QID_list, payload_index):
    """Insert question references inside a block (located inside the SurveyElements component).
    Insert the question references and the randomization options.
    
    Args: 
        QID_list(list): list of questions IDs.
        payload_index(str): string number indicating the index payload index in the SurveyElements component (training block index, or testing block index). 
        survey_data(dict): JSON input QSF qualtrics file.
    Return:
        survey_data (dict): updated survey data
    """

    page_break = {"Type": "Page Break"}

    new_question_ref_list = []
    for qid in QID_list:
        current_question_ref = {"Type": "Question", "QuestionID": str(qid)}
        new_question_ref_list.append(current_question_ref)
        new_question_ref_list.append(page_break)

    # remove last element (page break)
    new_question_ref_list = new_question_ref_list[0:-1]

    # add question refereces to the block (payload_index) 'BlockElements'
    survey_data["SurveyElements"][0]["Payload"][payload_index][
        "BlockElements"
    ] = new_question_ref_list

    # add question references to the Options of the blokc, Randomization
    survey_data["SurveyElements"][0]["Payload"][payload_index]["Options"][
        "BlockVisibility"
    ] = "Collapsed"

    randomized_list = ["{~Randomized~}" for item in QID_list]
    question_id_list = [question_id for question_id in QID_list]
    survey_data["SurveyElements"][0]["Payload"][payload_index]["Options"][
        "Randomization"
    ]["Advanced"]["FixedOrder"] = randomized_list
    survey_data["SurveyElements"][0]["Payload"][payload_index]["Options"][
        "Randomization"
    ]["Advanced"]["RandomizeAll"] = question_id_list

    return survey_data
