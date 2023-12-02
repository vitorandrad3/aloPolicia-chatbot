from src.twilio.TwiloClient import TwilioClient
from src.env_variables import EnvConstants

def send_message_to_user(return_message, user_number):
    twilio = TwilioClient()
    
    print('-------------------LEX RETURN MESSAGE----------------------')
    print(return_message)

    print('-------------------number----------------------')
    print(user_number)

    twilio.client.messages.create(
        from_=EnvConstants.twilio_sender,
        body=return_message,
        to=f'whatsapp:+{user_number}'
    )
