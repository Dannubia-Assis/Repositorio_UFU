"""
Preservado metadatas com wraps

metadados -> sao intrisecos em arquivos

wraps -> funcoes que envolvem elementos com diversas finalidades

Problema: Se for fazer a pesquisa por nome e documentacao a função decoradora
retorna o valor da funcao errada
"""

#Resolvendo o Problema 
from functools import wraps #é um decorador nativo do python

def ver_log(funcao):
    @wraps(funcao) #Decorator
    def logar(*args, **kwargs):
        """ Eu sou uma funcao dentro da outra""" #Isso eh uma documentacao
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui esta a documentacao {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """ Soma dois numeros"""
    return a + b

print(soma(10, 30))

print(soma.__name__) #Soma - nome da função
print(soma.__doc__) #Soma dois números - documentação da função