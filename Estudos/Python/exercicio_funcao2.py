"""
Faca um programa que tenha uma funcao que  receba uma lista de inteiros 
e retorne o maior valor
"""

def maior_numero(lista_inteiros):
    """maior = lista_inteiros[0]
    #For percorre toda a lista considerando o valor maior como o primeiro
    for numero in lista_inteiros:
        if numero > maior:
            maior = numero"""
    
    #Usando a funcao max()
    maior = max(lista_inteiros)

    return f'O maior numero da lista eh: {maior}!'


lista_inteiros = []

lista_inteiros = (input('Digite os inteiros separados por virgula: ')).split(',')

res = maior_numero(lista_inteiros)

print(res)