"""
Sorted

Nao confundir com sort(), sort() so funciona em listas

Podemos utilizar o sorted() com qualquer iteravel

sorted() serve para ordenar

OBS: o sorted() sempre retorna uma lista com os elementos do interavel ordenado

#Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

#cria uma nova lista com os itens ordenados
print(sorted(numeros)) #ordenar do menor para o maior
print(numeros)

numeros = [6, 1, 8, 2]

#adicionando parametros ao sorted()

print(sorted(numeros, reverse=True)) #Ordena do maior para o menor

#Podemos utilizar para coisas mais complexas

usuarios = [ 
    {"usarname": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"usarname": "carla", "tweets": ["Eu amo meu gato"]},
    {"usarname": "jeff", "tweets": []},
    {"usarname": "bob123", "tweets": []},
    {"usarname": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"usarname": "gal", "tweets": []}
]
#Ordenando por username - Ordem alfabetica
print(sorted(usuarios, key = lambda usuario: usuario["usarname"]))

#Ordenando por tweets - Quantidade de tweets
print(sorted(usuarios, key = lambda usuario: len(usuario["tweets"])))

"""
#Ultimo exemplo

musicas = [
        {'Titulo': 'Abc', 'Tocou': 3},
        {'Titulo': 'kiju', 'Tocou': 19},
        {'Titulo': 'gasf', 'Tocou': 10}
]

#Ordena da menos tocada  para a mais tocada
print(sorted(musicas, key = lambda musica: musica["Tocou"]))

#Ordena da mais tocada para a menos tocada
print(sorted(musicas, key = lambda musica: musica["Tocou"], reverse=True))