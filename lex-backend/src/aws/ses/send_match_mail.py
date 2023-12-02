import boto3
from src.env_constants import EnvConstants
def send_match_mail(image_source,image_target,accuracy,id):

    ses_client = boto3.client('ses', region_name='us-east-1')
    email_subject = f"Pessoas Desaparecidas - AlôPolicia Chatbot"
    
    email_source = f"Chatbot Alô Polícia <{EnvConstants.email_sender}>"

    email_body = f"""
    <html>
        <head>
            <title>Pessoas Desaparecidas - Polícia Civil SP</title>
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
                <h2>Possível pessoa desaparecida encontrada - Polícia Civil SP</h2>
                <h2>E-MAIL INTERNO</h2>
                <p>
                    <p>Encontramos uma correspondência da imagem enviada na ocorrência <b>Nº: {id}</b>.</p>
                    <b>Imagem enviada na ocorrência:</b>
                    <br>
                    {image_source}
                    <br>
                    <img src={image_source} alt="Imagem de origem">
                    <br>
                    <br>
                    <b>Imagem da base de dados:</b>
                    <br>
                    {image_target}
                    <br>
                    <img src={image_target} alt="Imagem correspondente">
                    <br>
                    <br>
                    <h3>Taxa de assertividade: {accuracy}%</h3>
                </p>

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
            'ToAddresses': [email_source]
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