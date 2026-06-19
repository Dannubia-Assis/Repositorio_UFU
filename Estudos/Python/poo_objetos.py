""""
Objetos

Objetos - sao instancias da classe - Apos o mapeamento do objeto do mundo real para sua
representacao computacional, devemos poder criar quantos objetos forem necessarios. Podemos
pensar nos objetos/instancias de uma classe como variaveis do tipo definido na classe.

"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero
    
    def mostra_cliente(self):
        print(f'O cliente eh {self.__cliente._Cliente__nome}') #Acessando outra classe com atributo privado

   
class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
"""
#Instancias/Objetos
lamp1 = Lampada('branca', '110', '60')

lamp1.ligar_desligar()

cliente1 = Cliente('Dannubia', '234.656.343-96')

cc = ContaCorrente('5000', '2000', cliente1)

user1 = Usuario('Dannubia', 'Cristina', 'dannubia@gmail.com', '123345')

print(f'A lampada esta ligada? {lamp1.checa_lampada()}')
"""

cliente1 = Cliente('Dannubia', '234.656.343-96')

cc = ContaCorrente('5000', '2000', cliente1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()