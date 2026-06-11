"""
Iterator - um objeto que pode ser iteravel
        - retorna uma dado, sendo um elemento por vez quando uma
        funcao next() é chamada
Itarable - Um objeto que irá retornar um iterator quando a funcao iter()
            for chamada

nome = 'nome' # é um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5,6] # é um iterable mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

#Criando sua propria versao de loop
# Faz o que o loop for faz

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Dannubia')

"""

#Iterador customizado

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

for n in Contador(1, 61): #Faz a mesma coisa que que a função range()
    print(n)

