"""
Reversed -  

OBS: nao confunda com a funcao reverse() que estudamos nas listas, so funciona
nas listas

A funcao reversed funciona com qualquer iteravel

Sua fucao eh inverter o iteravel
A funcao retorna um iteravel chamado list reverse iterator
"""

#Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

#Podemos converter o elemento retornado para uma lista, tupla ou conjunto

#Ex list(reversed(lista))

print(list(reversed(lista)))

#Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='')

#Sem o uso do for
print('\n')
print(''.join(list(reversed('Geek University'))))