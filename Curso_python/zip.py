""""
Zip - cria um iteravel (zip object) que agrega elemento de cada um dos iteraveis
passados como entrada em pares


#Exemplo

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1 , lista2) 

print(zip1)
print(type(zip1))

#O zip utiliza como tamanho o menor tamanho da lista que esta iteravel.

"""
#Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89,53]
alunos = ['Maria', 'Pedro', 'Carla']

#Cria um dicionario
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)