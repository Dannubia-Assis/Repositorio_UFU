"""
Metodo super se refere a super classe


"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = nome
    
    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')

class Gato(Animal):
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie) - Acessando pelos atributos da classe
        super().__init__(nome, especie) #Acessando pela super classe
        self.__raca = raca
        

felix = Gato('Felix', 'felina', 'miau')

felix.faz_som('miau')