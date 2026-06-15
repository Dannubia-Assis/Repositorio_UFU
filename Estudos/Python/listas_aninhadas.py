"""
Listas aninhadas (Nested lists)

Algumas linguagens de programacao possuem uma estrutura de dados chamados arrays:
- unidimensionais (Arrays/Vetores)
- multidimensionais (matrizes)

Em python existem listas

#Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #matriz 3 x 3

print(listas)

#Como fazemos para acessar os dados?

print(listas[0][1]) #acesso ao numero 2
print(listas[2][1]) #acesso ao numero 8

#Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

#List Comprehension

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #matriz 3 x 3

[[print(valor) for valor in lista] for lista in listas]

"""
#Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

#Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1,4)]
print(velha)

