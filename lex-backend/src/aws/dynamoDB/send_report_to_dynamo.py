import boto3
from src.utils.get_slot_value import get_slot_value


def send_report_to_dynamo(id, event):
    dynamodb = boto3.client('dynamodb')

    table = 'denuncia'

    item = {
        'id': {'S': id},
        'categoriaCrime': {'S': event['intent']['name']},
        'UF': {'S': 'UF'},
        'CEP': {'S': get_slot_value(event, 'CEP')},
        'numeroResidencia': {'S': get_slot_value(event, 'numeroResidencia')},
        'complementoEndereco': {'S': get_slot_value(event, 'complementoEndereco')},
        'motivoChamado': {'S': get_slot_value(event, 'motivoChamado')},
        's3ImageKey': {'S': get_slot_value(event, 'imagem')},


    }

    dynamodb.put_item(
        TableName=table,
        Item=item
    )

