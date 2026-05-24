"""
Definindo funções

Pequenos trechos de códigos que realizam tarefas esepcíficas
Já utilizamos várias funções desde de que iniciamos esse curso
Pode ou não receber entradas de dados e retornar uma saída de dados
Muito úteis para executar procedimentos similares por repetidas vezes

#Exemplo de utilização de funções

cores = ['verde', 'amarelo', 'azul', 'branco']

#Utilizando funções integrada (Built-in) do python print()

cores.append('roxo')

print(cores)

cores.clear()
print(cores)

Em python a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

Nome da função: sempre com letras minúsculas e se for nome composto
separado por underline;
parametros de entrada: opcionais onde tendo mais de um cada um separado por vírgula
bloco da função: processamento da função acontece, pode ter ou não retorno da função.

 
#Definindo a primeira funcao

def diz_oi():
    print('oi!')

#Chamada de execucao

diz_oi() #Atencao: nunca esqueca de utilizar o parenteses ao executar uma funcao


from time import sleep

def cantar_parabens():
    print('Parabens para voce')
    sleep(3)
    print('Nessa data querida')

cantar_parabens()    

#Em python, podemos inclusive criar variàveis do tipo de uma funcao
#atraves da variavel 

canta = cantar_parabens

canta()

Funcoes com retorno

OBS: Quando uma funcao nao retorna nenhum valor o retorno è None
OBS: Funcao retorna valores utilizando a palavra reservada return
OBS: Nao precisa criar uma variavel para receber o valor do retorno
de uma funcao

A palavra return finaliza a funcao 
Podemos ter mais de uma funcao mas com diferentes return
Podemos em uma funcao retornar qualquer tipo de dado e ate mesmo
multiplos valores

Apos o return nada e executado

#Funcao que retorna valor

def quadrado_de_7():
    return 7*7

print(f'Retorno: {quadrado_de_7()}')

#Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

"""
#Vamos criar uma funcao para jogar a moeda

from random import random

def joga_moeda():
    #Gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(f'Seu resultado e: {joga_moeda()}')