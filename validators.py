import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    digito1 = calcular_digito(cpf[:9], peso1)
    digito2 = calcular_digito(cpf[:9] + str(digito1), peso2)

    return cpf[-2:] == f"{digito1}{digito2}"

def validar_rg(rg):
    rg = re.sub(r'\D', '', rg)
    return len(rg) == 9 and rg.isdigit()