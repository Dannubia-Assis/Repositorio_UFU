"""
Herança multipla

Possibilidade de uma classe herdar de multiplas classes, fazendo com que
a classe filha herde todos os atributos e metodos de todas as classes herdadas.

Pode ser feita de duas maneiras:
- Por multiderivacao direta
- Por multiderivacao indireta

"""
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimetar(self):
        return f'Eu sou {self.__nome}'
    
class Aquatico:
    def __init__(self, nome):
        self.__nome = nome

    def nadar(self):
        return f'{self.__nome} esta nadando'