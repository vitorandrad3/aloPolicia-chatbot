from src.intents import denuncia_foragido
from src.intents import chamar_policia
from src.intents import bo_violencia_domestica
from src.intents import bo_pessoas_desaparecidas
from src.intents import denuncia_vandalismo
from src.intents import denuncia_desmanche
from src.intents import denuncia_outros
from src.intents import bo_fraude
from src.intents import bo_outros
from src.intents import bo_roubo_furto

import time
import os


def dispatch(intent_request):

    intent_name = intent_request['sessionState']['intent']['name']

    if intent_name == 'ChamarPoliciaIntent':
        next_state = chamar_policia.handler(intent_request)

    if intent_name == 'BOViolenciaDomesticaIntent':
        next_state = bo_violencia_domestica.handler(intent_request)

    if intent_name == 'BOPessoasDesaparecidasIntent':
        next_state = bo_pessoas_desaparecidas.handler(intent_request)
        
    if intent_name == 'DenunciaForagidoIntent':
        next_state = denuncia_foragido.handler(intent_request)
    
    if intent_name == 'DenunciaVandalismoIntent':
        next_state = denuncia_vandalismo.handler(intent_request)
    
    if intent_name == 'DenunciaDesmancheIntent':
        next_state = denuncia_desmanche.handler(intent_request)
    
    if intent_name == 'DenunciaOutrosIntent':
        next_state = denuncia_outros.handler(intent_request)

    if intent_name == 'BORouboFurtoIntent':
        next_state = bo_roubo_furto.handler(intent_request)

    if intent_name == 'BOOutrosIntent':
        next_state = bo_outros.handler(intent_request)

    if intent_name == 'BOFraudeIntent':
        next_state = bo_fraude.handler(intent_request)

    return next_state


def lambda_handler(event, context):

    os.environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()
    print(event)
    return dispatch(event)
