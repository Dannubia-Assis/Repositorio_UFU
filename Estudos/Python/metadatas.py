"""
Preservado metadatas com wraps

metadados -> sao intrisecos em arquivos

wraps -> funcoes que envolvem elementos com diversas finalidades

"""

#Problema 

def ver_log(funcao):
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