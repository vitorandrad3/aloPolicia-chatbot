import boto3
from src.env_variables import EnvConstants


def get_lex_session(session_id):
    client = boto3.client('lexv2-runtime')

    session_data = client.get_session(
        botId=EnvConstants.bot_id,
        botAliasId=EnvConstants.bot_alias_id,
        localeId=EnvConstants.bot_locale_id,
        sessionId=session_id,
    )
    print('--------------------session_data--------------------')
    print(session_data)

    return session_data
