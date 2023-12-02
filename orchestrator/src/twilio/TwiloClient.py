import boto3
from twilio.rest import Client
from src.env_variables import EnvConstants


class TwilioClient:
    def __init__(self):
        self.account_sid = EnvConstants.twilio_account_sid
        self.auth_token = EnvConstants.twilio_auth_token
        self.client = Client(self.account_sid, self.auth_token)

    def get_client(self):
        return self.client

    def get_credentials(self):
        return self.account_sid, self.auth_token
