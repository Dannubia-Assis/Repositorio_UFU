"""
Modulos collections - High performance Conteiner Datetypes

-> Counter (Contador)

Recebe um interavel como parametro e cria um objeto do tipo
colletions counter que eh parecido com um dicionario, contendo chave
como chave o elemento da lista passada com parametro e como valor
a quantidade de ocorrencia desse elemento.

#Utilizando o Counter

from collections import Counter

#Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

#Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

#Counter({3: 4, 1: 3, 2: 3, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})
#Para cada elemento da lista o counter criou criou uma chave e colocou
#como valor a quatidade de ocorrências

#Tambem funciona com strings
# Utilizando o split() eh possivel verificar com o counter quantas ocorrencias
#de um texto aparecem

"""
"""
Modulo Collections - Default Dict

Ao criar um dicionarios nos informamos um valor default
podendo utilizar um lambda para isso
Esse valor será utilizado sempre que não houver um valor 
definido. Caso tentamos acessar uma chave que não existe, essa
chave será criada e o valor default será atribuido

OBS: lambdas são funções sem nome que podem ou não receber
parametros de entrada e retornar valores
"""
#Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])

