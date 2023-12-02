from dotenv import load_dotenv
from os import getenv as env

load_dotenv()


class EnvConstants:
    twilio_sender = env('TWILIO_SENDER')
    bot_id = env('BOT_ID')
    bot_alias_id = env('BOT_ALIAS_ID')
    bot_locale_id = env('BOT_LOCALE_ID')
    s3_media_bucket = env('S3_MEDIA_BUCKET')
    twilio_account_sid=env('TWILIO_ACCOUNT_SID')
    twilio_auth_token=env('TWILIO_AUTH_TOKEN')
    
