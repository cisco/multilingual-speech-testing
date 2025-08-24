"""
Cisco Systems, Inc. and its affiliates
"""
"""
Qualtrics survey flow utilities.
"""
from qualtrics_utils.survey_components import get_survey_component_index_map


def get_current_number_of_flow_ids(survey_data, component_index_survey_map):
    """ Get current number of flow ids on the survey data.

    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        component_index_survey_map (dict): mapping between the survey component and the index in the json structure. 
    Return:
        (int) Current number of flow ids in the survey. 
    """

    return survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]][
        "Payload"
    ]["Properties"]["Count"]


def update_survey_number_of_flow_ids(survey_data, number_of_flow_ids):
    """ Update current number of flow ids on the survey data.

    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        component_index_survey_map (dict): mapping between the survey component and the index in the json structure. 
        number_of_questions(int): new number of flow IDs of the survey.
    Return:
        (int) Current number of flow ids in the survey. 
    """

    # get component index survey map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]]["Payload"][
        "Properties"
    ]["Count"] = int(number_of_flow_ids)
    return survey_data


def get_survey_flow_index_map(survey_data):
    """Get the mapping between components and indexes in the survey data.
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        
    Return:
        flow_index_survey_map (dict): mapping between the survey flowID and the index in the json structure `Survey Flow`. 
    """

    # get component index survey map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    flow_index_survey_map = {}

    for i in range(
        0,
        len(
            survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]][
                "Payload"
            ]["Flow"]
        ),
    ):
        flow_index_survey_map[
            survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]][
                "Payload"
            ]["Flow"][i]["FlowID"]
        ] = i

    return flow_index_survey_map


def get_survey_flow_index_by_block_id(survey_data, block_id):
    """Get the flow index by block_id, the flow index containing the block_id
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        block_id(str): Block ID.
    Return:
        flow_index (int): index of the  flow in the `SurveyElements.Payload.Flow` 
    """

    # get component index survey map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    for i in range(
        0,
        len(
            survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]][
                "Payload"
            ]["Flow"]
        ),
    ):
        flow_block = survey_data["SurveyElements"][
            component_index_survey_map["Survey Flow"]
        ]["Payload"]["Flow"][i]

        if "Flow" in flow_block:
            for item in flow_block["Flow"]:
                if "ID" in item.keys():
                    if block_id == item["ID"]:
                        return i


def update_flow_by_payload_index(survey_data, survey_payload_flow_index, flow_template):
    """Update flow by survey flow payload index. 
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        survey_flow_index(int): index of the of the payload in the `Survey Flow` on the survey.
        flow_template(dict): new flow template.
    Return 
        survey_data(dict): updated survey data.
    """

    # get component index survey map
    component_index_survey_map = get_survey_component_index_map(survey_data=survey_data)

    # update survey data
    survey_data["SurveyElements"][component_index_survey_map["Survey Flow"]]["Payload"][
        "Flow"
    ][survey_payload_flow_index] = flow_template
    return survey_data


def get_survey_embedded_data_field_index_map(survey_data):
    """Get embedded data field survey 
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file. 
    
    Return:
        index_embedded_data(dict): Field -> index mapping of the Survey Flow Embedded data
    """

    survey_component_index_map = get_survey_component_index_map(survey_data)

    index_embedded_data = {}

    for index in range(
        0,
        len(
            survey_data["SurveyElements"][survey_component_index_map["Survey Flow"]][
                "Payload"
            ]["Flow"][0]["EmbeddedData"]
        ),
    ):
        index_embedded_data[
            survey_data["SurveyElements"][survey_component_index_map["Survey Flow"]][
                "Payload"
            ]["Flow"][0]["EmbeddedData"][index]["Field"]
        ] = index

    return index_embedded_data


def get_survey_embedded_data_fields(survey_data, embedded_data_field):
    """Get survey embedded data field. This is the embedded data field presented in the 
    survey flow. 
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        embedded_data_field (string): name of the embedded data field in qualtrics.
    
    Return:
        embedded_field(string)
    """

    survey_component_index_map = get_survey_component_index_map(survey_data)

    index_embedded_data = get_survey_embedded_data_field_index_map(survey_data)

    assert embedded_data_field in index_embedded_data.keys()

    embedded_field = survey_data["SurveyElements"][
        survey_component_index_map["Survey Flow"]
    ]["Payload"]["Flow"][0]["EmbeddedData"][index_embedded_data[embedded_data_field]]

    return embedded_field["Value"]


def update_survey_embedded_data_fields(survey_data, embedded_data_dict):
    """Update embedded data fields using the embedded_data_dict.
    
    Args:
        survey_data(dict): JSON input QSF qualtrics file.
        embedded_data_dict (dict): embedded_data_key -> value dictionary.
        
    Rerturns:
        survey_data(dict): Updated version of the survey_data JSON file.
    """

    for embedded_data_field, embedded_data_value in embedded_data_dict.items():

        survey_component_index_map = get_survey_component_index_map(survey_data)

        index_embedded_data = get_survey_embedded_data_field_index_map(survey_data)

        assert embedded_data_field in index_embedded_data.keys()

        embedded_field = survey_data["SurveyElements"][
            survey_component_index_map["Survey Flow"]
        ]["Payload"]["Flow"][0]["EmbeddedData"][
            index_embedded_data[embedded_data_field]
        ]
        embedded_field["Value"] = str(embedded_data_value)

        survey_data["SurveyElements"][survey_component_index_map["Survey Flow"]][
            "Payload"
        ]["Flow"][0]["EmbeddedData"][
            index_embedded_data[embedded_data_field]
        ] = embedded_field

    return survey_data
