from src.utils.get_slot_value import get_slot_value
from src.utils.validate_cep import get_uf_by_cep
import boto3


def send_domestic_violence_to_dynamo(id, intent_request):
    dynamodb = boto3.client('dynamodb')

    table = 'BoViolenciaDomestica'
    cep = get_slot_value(intent_request, 'BOcep')

    uf = get_uf_by_cep(cep)

    item = {
        'id': {'S': id},
        'UF': {'S': uf},
        'nomeVitima': {'S': get_slot_value(intent_request, 'BONomeVitimaSlot')},
        'temFilhos': {'S': get_slot_value(intent_request, 'BOTemFilhosSlot')},
        'cpfVitima': {'S': get_slot_value(intent_request, 'BOCPFVitimaSlot')},
        'vitimaCep': {'S': cep},
        'dataNascVitima': {'S': get_slot_value(intent_request, 'BODataNascVitimaSlot')},
        'emailVitima': {'S': get_slot_value(intent_request, 'BOEmailVitimaSlot')},
        'telefoneVitima': {'S': get_slot_value(intent_request, 'BOTelVitimaSlot')},
        'grauRelacionamento': {'S': get_slot_value(intent_request, 'BOGrauRelacionamentoSlot')},
        'nomeAgressor': {'S': get_slot_value(intent_request, 'BONomeAgressorSlot')},
        'cpfAgressorSlot': {'S': get_slot_value(intent_request, 'BOCPFAgressorSlot')},
        'descricaoOcorrencia': {'S': get_slot_value(intent_request, 'BODescricaoOcorrenciaSlot')},
    }

    dynamodb.put_item(
        TableName=table,
        Item=item
    )
