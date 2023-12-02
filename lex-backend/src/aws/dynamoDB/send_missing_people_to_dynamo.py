from src.utils.get_slot_value import get_slot_value
from src.utils.validate_cep import get_uf_by_cep
import boto3


def send_missing_people_to_dynamo(id, intent_request, compare_faces_response):
    dynamodb = boto3.client('dynamodb')
    
    cep = get_slot_value(intent_request, 'CEPdoDesaparecido')
    
    uf =get_uf_by_cep(cep)

    table = 'BOPessoasDesaparecidas'

    item = {
        'id': {'S': id},
        'UF': {'S': uf},
        'nomeDenunciante': {'S': get_slot_value(intent_request, 'NomeDenunciante')},
        'EmailDenunciante': {'S': get_slot_value(intent_request, 'EmailDenunciante')},
        'desaparecidoNome': {'S': get_slot_value(intent_request, 'NomeCompleto')},
        'desaparecidoDataNascimento': {'S': get_slot_value(intent_request, 'DataNascimento')},
        'desaparecidoCPF': {'S': get_slot_value(intent_request, 'CPF')},
        'desapareceuAntes': {'S': get_slot_value(intent_request, 'DesapareceuAntes')},
        'problemaMental': {'S': get_slot_value(intent_request, 'ProblemaMental')},
        'caracteristicasDesaparecido': {'S': get_slot_value(intent_request, 'CaracteristicasDesaparecido')},
        'cepDesaparecido': {'S': cep},
        'numeroResidenciaDesaparecido': {'S': get_slot_value(intent_request, 'NumeroResidenciaDesaparecido')},
        'complementoDesaparecido': {'S': get_slot_value(intent_request, 'ComplementoDesaparecido')},
        'descricaoOcorrencia': {'S': get_slot_value(intent_request, 'DescricaoOcorrencia')},
        'econtradoNoBancoDeImagens': {'S': compare_faces_response['foundMatch']},
        's3KeyImagemDesaparecido': {'S': compare_faces_response['targetImageKey']},
        's3KeyImagemCorrespondente': {'S': compare_faces_response['sourceImageKey']},
        'porcentagemSemelhanca': {'N': compare_faces_response['accuracy']},
    }

    dynamodb.put_item(
        TableName=table,
        Item=item
    )
