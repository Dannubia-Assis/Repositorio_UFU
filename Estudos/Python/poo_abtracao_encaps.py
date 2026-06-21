"""
Abstração e encapsulamento

O grande objetivo é encapsular nosso código dentro de um grupo 
lógico e hierárquico utilizando classes.

Name Mangling - _Classe__elemento

instancia._Pessoa_nome

instancia._Pessoa__falar()

Abstração: ato de expor apenas dados relevantes de um classe,
escondendo o que é privado

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor 
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else: 
                print('Saldo insuficiente')
        else: print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        #1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 #Taxa de transferencia paga por quem realizou a transferencia

        #2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


#Testando

conta1 = Conta('Dannubia', 150, 1500)
conta1.extrato()

conta2 = Conta('Guilherme', 400, 2000)
conta2.extrato()

conta2.transferir(100, conta1) #Conta 2 transfere para conta1 por que eh o self

conta1.extrato()
conta2.extrato()


#print(conta1.__dict__)
#conta1.depositar(150)
#print(conta1.__dict__)
#conta1.sacar(2000)
#print(conta1.__dict__)

