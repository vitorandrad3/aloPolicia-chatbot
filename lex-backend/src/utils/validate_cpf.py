import re

def validate_cpf(cpf):
    cpf = re.sub(r'[^\d]', '', cpf)

    if not re.match(r'\d{11}$', cpf):
        return False

    digits = [int(digit) for digit in cpf]

    if len(set(digits)) == 1:
        return False

    sum_of_products = sum(a * b for a, b in zip(digits[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10

    if digits[9] != expected_digit:
        return False

    sum_of_products = sum(
        a * b for a, b in zip(digits[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10

    if digits[10] != expected_digit:
        return False

    return cpf