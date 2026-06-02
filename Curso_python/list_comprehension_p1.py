""""
List comprehension

- Utilizando nos podemos gerar novas listas com dados processados a partir de outro iteravel

#Sintaxe 

[dado for dado in iteravel]

#Exemplo

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

Para entender melhor o que esta acontecendo devemos dividir a expressao em duas
partes:

- A primeira parte: for numero in numeros
- Segunda parte: numero * 10

# List  comprehension versus Loop

#Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero *2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

#List comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

nome = 'Dannubia Cristina'
print([letra.upper() for letra in nome])

"""

"""
Parte 2

Podemmos adicionar estruturas condicionais logicas nas lists comprehesion

"""

#Exemplo 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

#Refatorar

#Qualquer numero par modulo de 2 eh 0 (resto zero) e 0 em python e False. not False = True
pares = [numero for numero in numeros if not numero % 2]

#Qualquer numero impar modulo de 2 eh 1 e 1 em python eh True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)