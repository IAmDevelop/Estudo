'''
Roberto Santos da Silva - RA = 1901617
Marcos Castelli - RA: 1901605
'''

import salario_funcionario


def teste1_desenvolvedor():
    try:
        lista = []
        lista = ["Marcílio dos Santos", "marcilio@email.com", 3000.00,
                 "DESENVOLVEDOR"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 2400.0
        print("Teste deu Certo")
    except AssertionError:
        print("Teste deu errado")


def teste2_desenvolvedor():
    try:
        lista = []
        lista = ["Marcílio dos Santos", "marcilio@email.com", 2999.00,
                 "DESENVOLVEDOR"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 2699.1
        print("Teste deu Certo")
    except AssertionError:
        print("Teste deu Errado")


def teste1_analista():
    try:
        lista = []
        lista = ["Marcílio dos Santos", "marcilio@email.com", 2000.00,
                 "ANALISTA"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 1500.0
        print("Teste deu Certo")
    except AssertionError:
        print("Teste deu Errado")


def teste2_analista():
    try:
        lista = []
        lista = ["Marcílio dos Santos", "marcilio@email.com", 1999.00,
                 "ANALISTA"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 1699.1499999999999
        print("Teste deu Certo")
    except AssertionError:
        print("Teste deu Errado")


def teste1_gerente():
    try:
        lista = []
        lista = ["Marcílio dos Santos", "marcilio@email.com", 5000.00,
                 "GERENTE"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 3500.0
        print("Teste deu Certo")
    except AssertionError:
        print("Teste deu Errado")


def teste2_gerente():
    try:
        lista = []
        lista = ["Marcílio dos Santos", "marcilio@email.com", 4999.00,
                 "GERENTE"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 3999.2000000000003
        print("Teste deu Certo")
    except AssertionError:
        print("Teste deu Errado")


def teste_outro_cargo():
    try:
        lista = []
        lista = ["Marcílio dos Santos", "marcilio@email.com", 4999.00,
                 "Cozinheiro"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario > 0
        print("Teste deu Certo")
    except TypeError:
        print("Teste deu Errado")


teste1_desenvolvedor()
teste2_desenvolvedor()
teste1_analista()
teste2_analista()
teste1_gerente()
teste2_gerente()
teste_outro_cargo()
