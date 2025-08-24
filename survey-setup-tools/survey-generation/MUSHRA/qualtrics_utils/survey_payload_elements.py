"""
Cisco Systems, Inc. and its affiliates
"""
# coding: utf-8

from qualtrics_utils.survey_components import get_survey_component_index_map

def get_survey_block_element_payload_map(survey_data):
    """Get survey block -> index mapping.
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
    
    Return:
        block_index_map(dict): block -> index mapping. 
    """

    component_index_survey_map = get_survey_component_index_map(survey_data)
    
    block_index_map = {}
    for index, row in survey_data['SurveyElements'][component_index_survey_map['Survey Blocks']]['Payload'].items():
        block_description_id = str(row['Description']).strip()
        block_index_map[block_description_id] = index
        
    return block_index_map


def get_last_survey_block_element_payload(survey_data):
    """Get the last payload ID from the blocks in the surveyElement list of the survey.
    Every block has a payload ID on the blocks of the survey element list `data['surveyElements'][survey_blocks_index]['Payload']`. 
    All the blocks (qualtrics blocks) are referenced in this Payload list. 
    
    Args:
        block_index_map(dict): survey block -> index mapping
    Return 
        last_payload_block
    """
    block_index_map  = get_survey_block_element_payload_map(survey_data)
    
    return str(max([int(item) for item in block_index_map.values()]))



def add_new_survey_block_element_payload(survey_data, block_template):
    """ Add new survey block element payload.
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        block_template (dict): Block template
    
    Return:
        survey_data (dict): updated survey data
    """
    
    
    last_survey_block_element = get_last_survey_block_element_payload(survey_data)
    next_survey_block_element = str(int(last_survey_block_element + 1))
    
    component_index_survey_map = get_survey_block_element_payload_map(survey_data)
    
    survey_data['SurveyElements'][component_index_survey_map['Survey Blocks']]['Payload'][next_survey_block_element] = block_template
    
    return survey_data
    

def insert_new_survey_block_element_payload(survey_data, survey_block_id ,block_template):
    """ Add new survey block element payload on the survey_block_id position.
    Add a new one if the survey_block_id doesn't exist.
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        survey_block_id(str): survey block element payload index.
        block_template(dict): new block template 
    
    Return:
        survey_data (dict): updated survey data
    """
    
    component_index_survey_map = get_survey_component_index_map(survey_data)

    # block ID already exists, replace.
    if(survey_block_id in survey_data['SurveyElements'][component_index_survey_map['Survey Blocks']]['Payload'].keys()):
        survey_data['SurveyElements'][component_index_survey_map['Survey Blocks']]['Payload'][survey_block_id] = block_template
    else:        
        last_survey_block_element = get_last_survey_block_element_payload(survey_data)
        next_survey_block_element = str(int(last_survey_block_element) + 1)
        
        survey_data['SurveyElements'][component_index_survey_map['Survey Blocks']]['Payload'][next_survey_block_element] = block_template
        
    return survey_data