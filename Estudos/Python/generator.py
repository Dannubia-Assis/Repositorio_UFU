"""
Generators

Em aulas anterioress estudamos:

List comprehension
Dictionary comprehension
Set comprehension

Nao vimos tuples comprehension.... porque elas se chamam generators

#Utilizando generators com any

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

#List comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#Generator
#Utiliza parenteses, utiliza menos memoria, mais perfomatico
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

#getsizeof() - retorna a quantidade de bytes em memoria do elemento passado 
#como parametro

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof('9'))
print(getsizeof('91'))
print(getsizeof('903789834759384'))
print(getsizeof('True'))

from sys import getsizeof

#Gerando uma lista de numeros com list comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])

#Gerando uma lista de numeros com set comprehension

set_comp = getsizeof({x * 10 for x in range(1000)})

#Gerando uma lista de numeros com dictionary comprehension

dic_comp = getsizeof([{x: x * 10 for x in range(1000)}])

#Gerando uma lista de numeros com generation

gen = getsizeof(x * 10 for x in range(1000))

print(f'List {list_comp}')
print(f'List {set_comp}')
print(f'List {dic_comp}')
print(f'List {gen}')

"""

# Eu posso iterar no generator expression? Sim

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)