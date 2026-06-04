"""
Conhecidas como expressões lambdas são funções sem nome ou seja funções anonimas



#Expressao lambda

lambda x: 3 * x + 1 #Recebe o parametros 'x' e retorna o valor do que esta 
                    # depois dos dois pontos

#E como utilizar?

calc = lambda x: 3 * x + 1 


# Pode ter mais de uma entrada

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' dannubia', '     cristina'))


#Em funções podem existir nenhuma ou varias entradas. em lambdas também

amar = lambda: 'Como não amar python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5

print(amar())
print(uma(6))
print(duas(1, 2))

#Se passarmos mais argumentos do que parametros esperados teremos typeerror

"""

#Função quadratica

#f(x) = a * x ** 2 + b * x + c

#Definindo função

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x)"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2)) #Chama a função e o lambda

