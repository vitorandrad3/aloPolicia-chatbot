import re

def validate_phone(telefone):
    only_number = re.sub(r'[-.()\s]', '', telefone)

    if len(only_number) == 11:
        ddd = only_number[:2]
        if 11 <= int(ddd) <= 99:
            return only_number
        else:
            return False
    else:
        return False