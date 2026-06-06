"""
Filter

filter() - filtrar dados de uma determinada colecao

#Biblioteca para trabalhar com dados estatisticos
import statistics

#Dados coletados por algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a media utilizando a funcao mean()
media = statistics.mean(dados)

#obs: assim como a funcao map a filter recebe dois parametros sendo 
# uma funcao e um iteravel
res = filter(lambda valor: valor > media, dados)

print(list(res))
print(media)

print(f'Novamente: {list(res)}')

#OBS: assim como na funcao map apos ser utilizada os dados de filter
#eles sao excluidos da memoria

paises = ['', 'Argentina', '', 'Brasil', 'Chile']

print(paises)

res = filter(None, paises)

print(list(res))

#Diferenca entre map e filter: retorna um objeto mapeando cada
#elemento do iteravel. O filter retorna apenas um objeto filtrando apenas os
#elementos de acordo com a funcao

#Exemplo mais complexo

usuarios = [ 
    {"usarname": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"usarname": "Carla", "tweets": ["Eu amo meu gato"]},
    {"usarname": "Jeff", "tweets": []},
    {"usarname": "bob123", "tweets": []},
    {"usarname": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"usarname": "gal", "tweets": []}
]

print(usuarios)

#Filtrar os usuarios que estao inativos no twitter

#Forma 1
#inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

#Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

"""
#Combinar filter e map

nomes = ['Vanessa', 'Ana', 'Maria']

#Devemos criar  uma lista contendo 'Sua instrutora eh' + nome, desde que cada
#nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora eh {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

