from src.aws.lex.get_session import get_lex_session
import boto3
from src.env_variables import EnvConstants


def send_text_to_lex(user_input, session_id):
    client = boto3.client('lexv2-runtime')

    response = get_lex_response(client, session_id, user_input)

    print("########################## LEX RESPONSE ###########################")
    print(response)
    return response


def get_lex_response(client, session_id, user_input):
    try:
        session_data = get_lex_session(session_id)

        session_state = session_data['sessionState']

        response = client.recognize_text(
            botId=EnvConstants.bot_id,
            botAliasId=EnvConstants.bot_alias_id,
            localeId=EnvConstants.bot_locale_id,
            sessionId=session_id,
            text=user_input,
            sessionState=session_state
        )

    except:
        response = client.recognize_text(
            botId=EnvConstants.bot_id,
            botAliasId=EnvConstants.bot_alias_id,
            localeId=EnvConstants.bot_locale_id,
            sessionId=session_id,
            text=user_input,
        )
    return response
