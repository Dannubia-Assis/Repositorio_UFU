"""
Map

com o map fazemos mapeamento de valores para função:



import math

def are(r):
    Calcula a area de um circulo com raio r
    return math.pi * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]

#forma comum
areas = []
for r in raios:
    areas.append(are(r))

print(areas)

#forma 2 - Map

#Map é uma função que recebe dois parâmetros: o primeiro a função e o segundo
# um iterável. Retorna um map object
areas = []
areas = map(are, raios)
print(list(areas))


#forma 3 - Map com lambda

print(list(map(lambda r:math.pi * (r ** 2), raios)))

#Apos utilizar a função map depois da primeira utilização do resultado ele zera

"""

