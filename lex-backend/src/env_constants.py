from dotenv import load_dotenv
from os import getenv as env

load_dotenv()


class EnvConstants:
    email_banner = env('EMAIL_BANNER')
    email_footer = env('EMAIL_FOOTER')
    email_sender = env('EMAIL_SENDER')
