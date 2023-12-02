from src.env_constants import EnvConstants
from src.utils.validate_cep import get_cep_informations
import boto3


def send_notification_mail(email_subject, title, slots, cep):
    ses_client = boto3.client('ses', region_name='us-east-1')
    endereco = get_cep_informations(cep)
    email_body = f"""
                    <html>
                        <head>
                            <title> {title} - Polícia Civil SP</title>
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
                                <h2>Confirmação de {title} - Polícia Civil SP</h2>
                                <h2>E-MAIL INTERNO</h2>
                                <p><strong>Rua:</strong> {endereco[1]['street']}</p>
                                <p><strong>Número:</strong> {slots['NumeroResidencia']['value']['interpretedValue']}</p>
                                <p><strong>Complemento:</strong> {slots['Complemento']['value']['interpretedValue']}</p>
                                <p><strong>Bairro:</strong> {endereco[1]['district']}</p>
                                <p><strong>Cidade:</strong> {endereco[1]['city']}</p>
                                <p><strong>UF:</strong> {endereco[1]['uf']}</p>
                                <p><strong>CEP:</strong> {endereco[1]['cep']}</p>
                                <p><strong>Motivo do Chamado:</strong> {slots['MotivoChamado']['value']['interpretedValue']}</p>

                                <p>Este e-mail é para confirmar o chamado de ocorrência realizado no AlôPolicia Chatbot junto à Polícia Civil de São Paulo.</p>
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
        'Source': EnvConstants.email_sender,
        'Destination': {
            'ToAddresses': [EnvConstants.email_sender]
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