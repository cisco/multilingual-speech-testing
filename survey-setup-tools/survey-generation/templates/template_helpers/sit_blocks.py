"""
Cisco Systems, Inc. and its affiliates
"""
"""
Template helper utilities for blocks in the survey.
"""

import copy
import random, string

from templates.templates.block_templates import (
    BLOCK_TEMPLATE,
    FLOW_BLOCK_TEMPLATE,
    HEARING_TEST_TEMPLATE,
)


def create_new_testing_block(block_id, block_name):
    """Create new testing qualtrics block. 
    This is a new testing block (qualtrics block)
    
    Args:
        block_id(str): block id. Generated with `generate_qualtrics_block_id()`
        block_name(str): block desriptive name.
        
    Return:
        new block template.
    """

    description_placeholder = "DESCRIPTION_ID_PLACEHOLDER"
    block_id_plaholder = "DESCRIPTION_ID_PLACEHOLDER"

    block_template = copy.deepcopy(BLOCK_TEMPLATE)

    block_template["ID"] = block_id
    block_template["Description"] = block_name
    block_template["BlockElements"] = []

    return block_template


def create_new_flow_block(flow_id, block_id_index_map, current_max_flow_id):
    """Create a new block flow with a list of block items.
    The flow block is standard for the testing block. It is BlockRandomizer and it references
    all the testing blocks. The ID of the block is needed with the payload index that is used to indicate create a FlowID.
    {block_id:'N'}. i.e:
    
    {'Type': 'Standard',
     'ID': 'block_id',
     'FlowID': 'FL_N',
     'Autofill': []
     }
     
    Each question is randomized 
    Args:
        flow_id (str): Flow ID in the survey data.
        block_id_index_map(dict): Mapping of block_id->payload index mapping dictionary.
        current_max_flow_id(int): current max flow index (not already existing)
    """

    flow_block_template = copy.deepcopy(FLOW_BLOCK_TEMPLATE)

    # reference flow template
    reference_template = {
        "Type": "Standard",
        "ID": "BL_cCLEwGT3FbfZOJw",
        "FlowID": "FL_11",
        "Autofill": [],
    }

    reference_template["FlowID"] = flow_id

    # generate the list of references
    reference_block_list = []
    for block_id, block_index in block_id_index_map.items():
        current_template_item = copy.deepcopy(reference_template)

        current_template_item["ID"] = block_id
        current_flow_id = "FL_" + str(current_max_flow_id)
        current_template_item["FlowID"] = current_flow_id

        reference_block_list.append(current_template_item)

        current_max_flow_id += 1

    # assign reference list to flow template
    flow_block_template["Flow"] = reference_block_list

    return flow_block_template


def generate_qualtrics_block_id():
    """Generate block ID
    """
    BLOCK_ID_BASE = "BL_"
    return BLOCK_ID_BASE + "".join(
        random.choices(string.ascii_letters + string.digits, k=15)
    )


def create_hearing_test_block(hearing_test_options):
    """create a new survey hearing test block.
    Update the audio links for the hearing test based on the hearing_test_options 
    Args:
        survey_data (JSON): Survey QSF data.
        hearing_test_options(dict): {option: link, digits}. 
    Return:
        survey_data (JSON): Updated Survey.
    """
    # load hearing test template
    hearing_test_template = copy.deepcopy(HEARING_TEST_TEMPLATE)

    # change hearing options on default language
    for key in hearing_test_options.keys():
        hearing_test_template["Payload"]["Answers"][key][
            "Display"
        ] = hearing_test_template["Payload"]["Answers"][key]["Display"].replace(
            "AUDIO_LINK_PLACEHOLDER", hearing_test_options[key][0]
        )

    # change hearing options for all the available languages
    available_languages = hearing_test_template["Payload"]["Language"].keys()

    for language in available_languages:
        current_language_answers = hearing_test_template["Payload"]["Language"][
            language
        ]["Answers"]

        for key, value in current_language_answers.items():
            hearing_test_template["Payload"]["Language"][language]["Answers"][key][
                "Display"
            ] = hearing_test_template["Payload"]["Language"][language]["Answers"][key][
                "Display"
            ].replace(
                "AUDIO_LINK_PLACEHOLDER", hearing_test_options[key][0]
            )

    return hearing_test_template
