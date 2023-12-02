from src.aws.ses.send_notification_mail import send_notification_mail
from src.intents.dialog_utils.get_cep_response import get_lex_response_in_cep_slot
from src.intents.dialog_utils.lex_responses import LexResponses
from src.aws.dynamoDB.send_report_to_dynamo import send_report_to_dynamo
import uuid


def handler(intent_request):

    slots = intent_request['sessionState']['intent']['slots']

    code_hook = intent_request['invocationSource']

    if code_hook == 'DialogCodeHook':
        if 'proposedNextState' in intent_request:
            current_next_slot = intent_request['proposedNextState']['dialogAction']['slotToElicit']

            if current_next_slot == 'NumeroResidencia':

                response = get_lex_response_in_cep_slot(
                    intent_request, cep_slot_name='CEP')
            else:
                response = LexResponses.delegate

        else:
            if intent_request["sessionState"]["intent"]["confirmationState"] == "Confirmed":
                id= str(uuid.uuid4())
                email_subject = "Notificação de Denúncia - AlôPolicia Chatbot"
                email_title = 'Denúncia'
                cep = intent_request['sessionState']['intent']['slots']['CEP']['value']['interpretedValue']
               
                send_notification_mail(email_subject, email_title, slots, cep)

            response = LexResponses.delegate

    return response

    ...
