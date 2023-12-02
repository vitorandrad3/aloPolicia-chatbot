from src.utils.validate_cpf import validate_cpf

def get_lex_response_in_cpf_slot(intent_request, cpf_slot_name):
   
    cpf = intent_request['sessionState']['intent']['slots'][cpf_slot_name]['value']['interpretedValue']
    cpf_response = validate_cpf(cpf)
    
    if not cpf_response:
        intent_request["proposedNextState"]["dialogAction"]["slotToElicit"] = cpf_slot_name
        response = {'sessionState': intent_request["proposedNextState"],
                    'messages':
                        [
                            {
                                "contentType": 'PlainText',
                                "content": "CPF inválido. Por favor, revise sua mensagem e envie um CPF válido."
                            }
        ]

        }
    else:
        intent_request['sessionState']['intent']['slots'][cpf_slot_name]['value']['interpretedValue'] = cpf_response
        response = {
            'sessionState': intent_request["proposedNextState"]}

    return response