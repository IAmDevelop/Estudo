'''
Roberto Santos da Silva - RA = 1901617
Marcos Castelli - RA: 1901605
'''


def calcular_salario(funcionario):
    if funcionario[3] != "DESENVOLVEDOR" and funcionario[3] != "ANALISTA" and \
            funcionario[3] != "GERENTE":
        raise TypeError
    if funcionario[3] == "DESENVOLVEDOR":
        if funcionario[2] >= 3000:
            salario = funcionario[2] * 0.80
        else:
            salario = funcionario[2] * 0.90
    elif funcionario[3] == "ANALISTA":
        if funcionario[2] >= 2000:
            return funcionario[2] * 0.75
        else:
            return funcionario[2] * 0.85
    else:
        if funcionario[2] >= 5000:
            return funcionario[2] * 0.70
        else:
            return funcionario[2] * 0.80
    return salario
