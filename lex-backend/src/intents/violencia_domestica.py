from src.aws.ses.send_confirmation_mail import send_confirmation_mail
from src.intents.dialog_utils.get_cpf_response import get_lex_response_in_cpf_slot
from src.intents.dialog_utils.get_cep_response import get_lex_response_in_cep_slot
from src.intents.dialog_utils.get_phone_response import get_lex_response_in_phone_slot
from src.intents.dialog_utils.lex_responses import LexResponses
from src.aws.dynamoDB.send_domestic_violence_to_dynamo import send_domestic_violence_to_dynamo
import uuid

def handler(intent_request):

    code_hook = intent_request['invocationSource']

    if code_hook == 'DialogCodeHook':
        if 'proposedNextState' in intent_request:
            current_next_slot = intent_request['proposedNextState']['dialogAction']['slotToElicit']

            if current_next_slot == 'BODataNascVitimaSlot':
                response = get_lex_response_in_cpf_slot(
                    intent_request, cpf_slot_name='BOCPFVitimaSlot')

            elif current_next_slot == 'BOContatoPoliciaSlot':
                response = get_lex_response_in_phone_slot(
                    intent_request, phone_slot_name='BOTelVitimaSlot')

            elif current_next_slot == 'BOcep':
                response = get_lex_response_in_cpf_slot(
                    intent_request, cpf_slot_name='BOCPFAgressorSlot')

            elif current_next_slot == 'BODescricaoOcorrenciaSlot':
                response = get_lex_response_in_cep_slot(
                    intent_request, cep_slot_name='BOcep')
            else:
                response = LexResponses.delegate
        else:
            if intent_request["sessionState"]["intent"]["confirmationState"] == "Confirmed":
                id = str(uuid.uuid4())
                
                send_confirmation_mail(mail_slot='BOEmailVitimaSlot',
                                       name_slot='BONomeVitimaSlot', intent_request=intent_request, id=id)
                
                send_domestic_violence_to_dynamo(id,intent_request)
            response = LexResponses.delegate

        print('######################### response #####################')
        print(response)

    return response
