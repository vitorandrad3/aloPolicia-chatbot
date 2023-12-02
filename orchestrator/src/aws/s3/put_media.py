import boto3
import requests
from src.twilio.TwiloClient import TwilioClient
from src.env_variables import EnvConstants


def put_media(image_url, key, contentType):
    twilio_client = TwilioClient()
    account_sid, auth_token = twilio_client.get_credentials()

    print(EnvConstants.s3_media_bucket)
    s3 = boto3.client('s3')

    image_data = requests.get(image_url, auth=(
        account_sid, auth_token)).content
    s3.put_object(Body=image_data, Bucket=EnvConstants.s3_media_bucket,
                  Key=key, ContentType=contentType)
