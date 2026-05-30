"""
Tuplas (tuple)
São bastante parecidas com as listas.

Existem basicamente duas diferenças básicas:
1- As tuplas são representadas por parênteses () e as listas por colchetes []
2- As tuplas são imutáveis, ou seja, não podem ser alteradas. Já as listas são mutáveis, ou seja, podem ser alteradas.

#As tuplas são representadas por parênteses (), mas:
tupla1 = (1,2,3)
print(tupla1)

print(type(tupla1))

#Tuplas com um elemento

tupla2 = (1) #Não é uma tupla 
print(tupla2)
print(type(tupla2))

tupla3 = (1,) #É uma tupla
print(tupla3)
print(type(tupla3))

#Tuplas são definidas pela vírgula e não pelo uso dos parênteses

tupla4 = 4,
print(tupla4)

#Gerando tupla com range
tupla = tuple(range(11))
print(tupla)

#Desempacotamento de tuplas

tupla = ('Universidade', 'Uberlândia')

escola, cidade = tupla #Alocando cada item da tupla a uma váriavel
print(escola)
print(cidade)

#Gera ValueError se colocarmos um número diferente de elementos para desempacotar

#Métodos para adição e remoção de tuplas não existem

#Pode somar tuplas mas não é possível modificar elas

#São imutáveis mas é possível sobrescrever seus valores, colocar
#mas na outra

#Para saber se um elemento está em uma tupla: retorna True ou False

tupla = (1, 2, 3)

print(3 in tupla)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
    """

#Contas elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a','b')

print(tupla.count('a'))

#Dicas de utilizadade de tuplas

#Devemos utilizar tuplas sempre que não precisamos modificar
# os dados contidos em uma coleção

