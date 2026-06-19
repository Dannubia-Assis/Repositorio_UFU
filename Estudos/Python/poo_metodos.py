"""
Métodos 

Métodos (funções) -> Representam os comportamentos do objeto. 
Ou seja, as ações que este objeto pode realizar no seu sistema.

Métodos são divididos em dois grupos:
- Métodos de instância
- Métodos de classe
- Metodos privados
- Metodos estaticos

Metodo __init__ - construtor da classe

Métodos sao escritos com letras minusculas

Nao eh aconselhado criar funcoes proprias utilizando o dunder


class Lampada:
    def __init__ (self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):  #isso é um método criado dentro de uma classe
        Retorna o valor do produto com o desconto
        return (self.__valor * (100 - porcentagem)) / 100


p1 = Produto('Playstation', 'Videogame', '2300')

print(p1.desconto(50)) #é um metodo de intancia porque precisa
                        #de uma instancia do objeto para funcionar

print(Produto.desconto(p1, 40)) #self, desconto - precisa do self para funcionar

"""

#Criando uma senha critografada para um usuario

from passlib.hash import pbkdf2_sha256 as cryp 
#importa uma biblioteca que cryptografa numeros

class Usuario:

    contador = 0

    @classmethod #Metodo de classe - decorador - nao acessa atributos do objeto
    def contas_usuario(cls): #cls - parametro recebido é a própria classe
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod #Metodo estatico - decorador - nao tem acesso a classe nem a instancia
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16) 
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')


    def nome_completo(self): #retorna o nome completo
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha): #Metodo que verifica se a senha digitada esta correta
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    #Metodos privados
    def __gera_usuario(self):
        return self.__email.split('@')[0]

"""
user1 = Usuario('Dannubia', 'De Assis', 'dannubia77@gmail.com', '123456')
user2 = Usuario('Guilherme', 'Silva', 'guigui77@gmail.com', '098765')

print(user1.nome_completo()) #Esta chamando o metodo nome_completo() pelo metodo de intancia
                                #tem acesso aos atributos privados da classe

print(Usuario.nome_completo(user1)) #Executando pela classe user1 eh o self (objeto)

print(f'Senha User1: {user1._Usuario__senha}') #Acesso de forma errada de um atributo de classe

print(f'Usuario gerado: {user1._Usuario__gera_usuario()}') #Acesso de forma errada de um metodo privado

#Metodos privados so sao acessados de dentro da classe, nesse se precisar de algum retorno
#desse metodo tem que fazer de dentro da classe
"""
#Metodo estatico

print(Usuario.contador)

print(Usuario.definicao())

user2 = Usuario('Guilherme', 'Silva', 'guigui77@gmail.com', '098765')

print(user2.contador)

print(user2.definicao())
