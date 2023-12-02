from src.aws.ses.send_confirmation_mail import send_confirmation_mail
from src.intents.dialog_utils.get_cpf_response import get_lex_response_in_cpf_slot
from src.intents.dialog_utils.get_cep_response import get_lex_response_in_cep_slot
from src.intents.dialog_utils.lex_responses import LexResponses
from src.aws.rekognition.compare_faces import compare_faces
from src.aws.dynamoDB.send_missing_people_to_dynamo import send_missing_people_to_dynamo
import uuid

def handler(intent_request):

    code_hook = intent_request['invocationSource']

    if code_hook == 'DialogCodeHook':
        if 'proposedNextState' in intent_request:
            current_next_slot = intent_request['proposedNextState']['dialogAction']['slotToElicit']

            if current_next_slot == 'ProblemaMental':
                response = get_lex_response_in_cpf_slot(
                    intent_request, cpf_slot_name='CPF')

            elif current_next_slot == 'NumeroResidenciaDesaparecido':
                response = get_lex_response_in_cep_slot(
                    intent_request, cep_slot_name='CEPdoDesaparecido')

            else:
                response = LexResponses.delegate

        else:
            if intent_request["sessionState"]["intent"]["confirmationState"] == "Confirmed":
                id = str(uuid.uuid4())
                
                send_confirmation_mail(
                     mail_slot='EmailDenunciante', name_slot='NomeDenunciante',intent_request=intent_request, id=id)

                image_key = intent_request['sessionState']['intent']['slots'][
                    'FotoPessoaDesaparecida']['value']['originalValue']
                
                compare_face_response = compare_faces(image_key)
                
                send_missing_people_to_dynamo(id,intent_request,compare_face_response)
                
            response = LexResponses.delegate

    print('######################### response #####################')
    print(response)

    return response

