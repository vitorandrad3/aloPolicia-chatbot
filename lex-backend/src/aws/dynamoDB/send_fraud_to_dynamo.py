from src.utils.get_slot_value import get_slot_value
from src.utils.validate_cep import get_uf_by_cep
import boto3


def send_fraud_to_dynamo(id, intent_request):
    dynamodb = boto3.client('dynamodb')

    table = 'BOFraude'
    cep = get_slot_value(intent_request, 'CEP')

    uf = get_uf_by_cep(cep)

    item = {
        'id': {'S': id},
        'UF': {'S': uf},
        'nomeVitima': {'S': get_slot_value(intent_request, 'Nome')},
        'CanalFraude': {'S': get_slot_value(intent_request, 'CanalFraude')},
        'DataOcorrencia': {'S': get_slot_value(intent_request, 'DataFraude')},
        'CEP': {'S': cep},
        'NumeroResidencia': {'S': get_slot_value(intent_request, 'NumeroResidencia')},
        'ComplementoEndereco': {'S': get_slot_value(intent_request, 'ComplementoEndereco')},
        'CPFVitima': {'S': get_slot_value(intent_request, 'CPF')},
        'emailVitima': {'S': get_slot_value(intent_request, 'BoEmailFraude')},
        'telefoneVitima': {'S': get_slot_value(intent_request, 'BOtelefoneFraude')},
        'detalheOcorrencia': {'S': get_slot_value(intent_request, 'DetalheOcorrencia')},
    }

    dynamodb.put_item(
        TableName=table,
        Item=item
    )
