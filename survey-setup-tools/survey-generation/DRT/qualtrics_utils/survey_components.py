"""
Cisco Systems, Inc. and its affiliates
"""
"""
Qualtrics survey components utilities.
"""


def get_survey_component_index_map(survey_data):
    """Get the mapping between components and indexes in the survey data.
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        
    Return:
        component_index_survey_map (dict): mapping between the survey component and the index in the json structure. 
    """

    # survey components to index map
    component_index_survey_map = {}

    for i in range(0, len(survey_data["SurveyElements"])):
        component_index_survey_map[
            survey_data["SurveyElements"][i]["PrimaryAttribute"]
        ] = i

    return component_index_survey_map


def get_number_of_survey_components(survey_data):
    """Get current number of survey components.
    
    Args: 
        survey_data(dict): JSON input QSF qualtrics file.
        
    Return:
        survey_number_components (int): number of components of the survey
    """

    return len(survey_data["SurveyElements"])
