from src.utils.validate_phone import validate_phone

def get_lex_response_in_phone_slot(intent_request, phone_slot_name,):
   
    phone = intent_request['sessionState']['intent']['slots'][phone_slot_name]['value']['interpretedValue']
    phone_response = validate_phone(phone)
    if not phone_response:
        intent_request["proposedNextState"]["dialogAction"]["slotToElicit"] = phone_slot_name
        response = {'sessionState': intent_request["proposedNextState"],
                    'messages':
                        [
                            {
                                "contentType": 'PlainText',
                                "content": "Telefone inválido. Por favor, revise sua mensagem e envie um Telefone válido."
                            }
        ]

        }
    else:
        intent_request['sessionState']['intent']['slots'][phone_slot_name]['value']['interpretedValue'] = phone_response
        response = {
            'sessionState': intent_request["proposedNextState"]}

    return response