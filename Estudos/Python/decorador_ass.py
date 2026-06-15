"""
Decorators com diferentes assinaturas

Para resolver utilizamos um padrao de projeto chamado decorator pattern

A assinatura de uma funcao eh representando pelo seu retorno nome e parametros
de entrada.

*args: captura argumentos posicionais em uma lista
*kwargs: captura argumentos nomeados em um dicionario

#Utilizando decorator pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):  #Funcao utiliza dois parametros de entrada
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola eu sou a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor. '

print(saudacao('Dannubia'))

print(ordenar('Picanha', 'Batata frita'))

"""

#Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

#Testando

print(comida_favorita('pizza', 'lanche'))