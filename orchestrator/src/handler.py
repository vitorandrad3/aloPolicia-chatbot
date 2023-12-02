from src.twilio.functions.send_message import send_message_to_user
from src.aws.lex.send_text_to_lex import send_text_to_lex
from src.twilio.functions.get_twilio_body import get_twilio_body
from src.aws.s3.put_media import put_media
from src.aws.transcribe.audio_to_text import audio_to_text


def orchestrator(event, context):
    twilio_response = get_twilio_body(event)

    num_media = int(twilio_response["NumMedia"][0])

    user_id = twilio_response["WaId"][0]
    if num_media > 0:

        messages_id = twilio_response["MessageSid"][0]
        media_url = twilio_response["MediaUrl0"][0]
        contentType = twilio_response["MediaContentType0"][0]
        if contentType == 'image/jpeg':

            key = f"{user_id}/images/{messages_id}"

            put_media(media_url, key, contentType)

            lex_response = send_text_to_lex(key, user_id)
            send_message_to_user('Imagem recebida com sucesso!', user_id)

        elif contentType == 'audio/ogg':

            key = f"{user_id}/audio/{messages_id}"

            put_media(media_url, key, contentType)

            send_message_to_user(
                'Audio recebido com sucesso! Estamos processando, aguarde.', user_id)

            text = audio_to_text(key, messages_id)
            lex_response = send_text_to_lex(text, user_id)

        else:
            send_message_to_user(
                'Infelizmente ainda não damos suporte a esse tipo de arquivo. Tente nos mandar apenas texto.')
    else:

        if 'Body' in twilio_response:

            user_input = twilio_response['Body'][0]

            lex_response = send_text_to_lex(user_input, user_id)

    if 'messages' in lex_response:
        for twilio_response in lex_response['messages']:
            if 'content' in twilio_response:
                return_message = twilio_response['content']
                print('******************************************')
                send_message_to_user(return_message, user_id)
