"""
Cisco Systems, Inc. and its affiliates
"""
# coding: utf-8

import random, string

def get_survey_id(survey_data):
    """Get the SurveyID of the qualtrics QSF file.
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        
    Returns:
        SurveyID (str): qualtrics survey ID.
    """
    
    SURVEY_ID = survey_data['SurveyElements'][0]['SurveyID']
    return SURVEY_ID
    

def generate_qualtrics_block_id():
    """Generate block ID
    """
    BLOCK_ID_BASE = "BL_" 
    return BLOCK_ID_BASE + ''.join(random.choices(string.ascii_letters + string.digits, k=15))