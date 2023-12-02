from src.utils.validate_cep import get_cep_informations


def get_lex_response_in_cep_slot(intent_request, cep_slot_name):

    cep = intent_request['sessionState']['intent']['slots'][cep_slot_name]['value']['interpretedValue']
    is_cep_valid = get_cep_informations(cep)
  
    if is_cep_valid:
        response = {
            'sessionState': intent_request["proposedNextState"]}
    else:
        intent_request["proposedNextState"]["dialogAction"]["slotToElicit"] = cep_slot_name
        response = {'sessionState': intent_request["proposedNextState"],
                    'messages':
                        [
                            {
                                "contentType": 'PlainText',
                                "content": "CEP inválido. Por favor, revise sua mensagem e envie um CEP válido."
                            }
        ]

        }

    return response
