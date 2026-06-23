"""
Propriedades

Em linguagem de programacao como o java, ao declararmos atributos privados nas classes,
costumamos a criar metodos publicos para manipulacao desses atributos. Esses metodos sao
conhecidos como getters e setters, onde os getters retornam o valor dos atributos e os
setters alteram o valor dos mesmos


    def get_numero(self): #Metodos gets - retorna o valor do atributo
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite): #Metodos set - altera o valor do atributo
        self.__limite = limite
    
"""

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property #Decorator equivalente ao get
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter #Decorator equivalente ao set
    def limite(self, novo_limite):
        self.__limite = novo_limite
    
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property #Metodo sendo utilziado como um propriedade
    def valor_total(self):
        return self.__saldo + self.__limite
  

conta1 = Conta('Dannubia', 400, 1500)
conta2 = Conta('Guilherme', 500, 2000)

print(conta1.extrato())

print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas eh {soma}')

print(conta1.__dict__)
conta1.limite = 7890
print(conta1.__dict__)

print(conta1.valor_total)
print(conta2.valor_total)

