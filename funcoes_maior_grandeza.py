"""
Funcoes de maior grandeza - Higher Order Functions - HOF

- Quando uma linguagem de programacao suporta HOF indica que podemos ter funcoes
que retornam outras funcoes como resultado ou menos que podemos passar outras funcoes
como argumento para outras funcoes e ate mesmo criar variaveis do tipo de funcoes
nos nossos programas.

OBS: Na secao de funcoes, nos utlizamos  isso.

Em python as funcoes sao cidados de primeira classe, First Class Citizen

#Exemplo - Definindo funcoes

def somar(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funcoes

print(calcular(4, 3, somar))

print(calcular(4, 3, sub))

print(calcular(4, 3, mult))

print(calcular(4, 3, div))

# Nested Function - Funcoes Aninhadas

#Em python podemos ter tambem funcoes dentro de funcoes, que sao conhecidas como Nested
#Function ou Inner Functions (Funcoes internas)

from random import choice

#Choice() - Seleciona uma opcao aleatoriamente

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))
    return humor() + pessoa

#Testando

print(cumprimento('Angelina'))

print(cumprimento('Dannubia'))

# Retornando funcoes de outras funcoes

from random import choice

def faz_me_rir():
    def rir():
        return choice(('haha', 'kkkkk', 'yayaya'))
    return rir

#Testando

rindo = faz_me_rir()

print(rindo())   
"""

# Inner function (funcoes internas) podem acessar o escopo de funcoes mais externas

from random import choice

def faz_me_rir(nome):
    def dando_risada():
        risada = choice(('haha', 'Sai daqui!', 'Nao sinto nada!'))
        return f' {risada} {nome}'
    return dando_risada

#Testando
print("Quer saber o meu humor?\n")

nome = input("Digite seu nome: ")

rindo = faz_me_rir(nome)

print(rindo())
