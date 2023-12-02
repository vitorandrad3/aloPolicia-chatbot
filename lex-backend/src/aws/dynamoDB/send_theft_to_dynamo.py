from src.utils.get_slot_value import get_slot_value
from src.utils.validate_cep import get_uf_by_cep
import boto3


def send_theft_to_dynamo(id, intent_request):
    dynamodb = boto3.client('dynamodb')

    cep = get_slot_value(intent_request, 'CPF')

    uf = get_uf_by_cep(cep)

    table = 'BORouboFurto'

    item = {
        'id': {'S': id},
        'UF': {'S': uf},
        'numeroResidencia': {'S': get_slot_value(intent_request, 'NumeroResidencia')},
        'complementoEndereco': {'S': get_slot_value(intent_request, 'ComplementoDeclarante')},
        'nomeDeclarante': {'S': get_slot_value(intent_request, 'NomeDeclarante')},
        'EmailDenunciante': {'S': get_slot_value(intent_request, 'EmailDenunciante')},
        'cpfVitima': {'S': get_slot_value(intent_request, 'CPFVitimaSlot')},
        'cepVitima': {'S': cep},
        'telfoneVitima': {'S': get_slot_value(intent_request, 'BOTelfone')},
        'emailVitima': {'S': get_slot_value(intent_request, 'BOEmailVitima')},
        'itemSubtraido': {'S': get_slot_value(intent_request, 'ItemRoubado')},
        'dataOcorridoSlot': {'S': get_slot_value(intent_request, 'BODataOcorridoSlot')},
        'descricaoOcorrido': {'S': get_slot_value(intent_request, 'BODescricaoOcorrido')},

    }

    dynamodb.put_item(
        TableName=table,
        Item=item
    )
