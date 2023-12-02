import boto3
from src.env_constants import EnvConstants


def send_confirmation_mail(mail_slot, name_slot, intent_request, id):

    name = intent_request['sessionState']['intent']['slots'][name_slot]['value']['originalValue']
    email_destination = intent_request['sessionState']['intent']['slots'][mail_slot]['value']['originalValue']
    ses_client = boto3.client('ses', region_name='us-east-1')
    email_subject = f"Boletim de Ocorrência - AlôPolicia Chatbot"
    email_source = f"Chatbot Alô Polícia <{EnvConstants.email_sender}>"

    email_body = f"""
        <html>
        <head>
            <title>Boletim de Ocorrência - Polícia Civil SP</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #FFFFFF;
                }}
                .container {{
                    max-width: 800px;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <div style="padding: 0px; text-align: left;">
                <img src={EnvConstants.email_banner} alt="Polícia Civil SP" style="max-width: 100%;">
            </div>
            <div class="container" style="padding: 0px;">
                <h2>Boletim de Ocorrência - Polícia Civil SP</h2>
                <h3>Prezado(a) <b>{name}</b>,</h3>
                <p>Este e-mail é para confirmar o registro do seu boletim de ocorrência <b>Nº: {id}</b> junto à Polícia Civil de São Paulo. Agradecemos por entrar em contato conosco.</p>
                <div class="container" style="visibility: hidden;">
                </div>
                <div style="text-align: center; margin-top: 0px;">
                    <img src={EnvConstants.email_footer} alt="Polícia Civil SP" style="max-width: 100%;">
                </div>
                <p>Se precisar de assistência, entre em contato conosco através dos canais disponíveis.</p>
                <p>Atenciosamente,<br>AlôPolicia Chatbot</p>
            </div>
        </body>
        </html>
        """
    email_message = {
        'Source': email_source,
        'Destination': {
            'ToAddresses': [email_destination]
        },
        'Message': {
            'Subject': {
                'Data': email_subject
            },
            'Body': {
                'Html': {
                    'Data': email_body
                }
            }
        }
    }
    ses_client.send_email(**email_message)