import base64
import urllib.parse


def get_twilio_body(event):

    encoded_body = event['body']
    decoded_body = base64.b64decode(encoded_body)
    decoded_body = urllib.parse.unquote(decoded_body)

    message = urllib.parse.parse_qs(decoded_body)
    
    print("############################ Twilio Response ####################")
    print(f"{message}")

    return message

