from brazilcep import get_address_from_cep, WebService


def get_cep_informations(cep):
    try:
        endereco = get_address_from_cep(cep, webservice=WebService.VIACEP)

        return True, endereco
    except Exception as err:
        print(f'ERRO AO BUSCAR CEP: {str(err)}')
        return False
    
    
def get_uf_by_cep(cep):
    is_valid, cep_informations = get_cep_informations(cep)
    uf = cep_informations['uf']
    
    return uf
