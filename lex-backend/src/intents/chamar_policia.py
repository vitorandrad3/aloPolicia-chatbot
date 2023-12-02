from src.aws.ses.send_notification_mail import send_notification_mail
from src.intents.dialog_utils.lex_responses import LexResponses
from src.intents.dialog_utils.get_cep_response import get_lex_response_in_cep_slot
from src.utils.get_slot_value import get_slot_value


def handler(intent_request):
    slots = intent_request['sessionState']['intent']['slots']
    code_hook = intent_request['invocationSource']
    email_subject = f"Chamado de Ocorrência - AlôPolicia Chatbot"

    if code_hook == 'DialogCodeHook':

        if 'proposedNextState' in intent_request:
            current_next_slot = intent_request['proposedNextState']['dialogAction']['slotToElicit']

            if current_next_slot == 'NumeroResidencia':
                response = get_lex_response_in_cep_slot(
                    intent_request, cep_slot_name='CEP')
            else:
                response= LexResponses.delegate
        else:

            if intent_request["sessionState"]["intent"]["confirmationState"] == "Confirmed":
                cep = get_slot_value(intent_request, 'CEP')
                email_subject = "Chamado de Ocorrência - AlôPolicia Chatbot"
                email_title = 'Chamado de Ocorrência'
                send_notification_mail(email_subject, email_title, slots, cep)

            response = LexResponses.delegate
            
    return response
