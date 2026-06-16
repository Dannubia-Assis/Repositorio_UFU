"""
Classes

São modelos dos objetos do mundo real sendo representados computacionalmente

Classes podem conter:
- Atributos -> representa as caracteristicas dos objetos.
Pelos atributos conseguimos representar computacionalmente os 
estados de um objeto
- Metodos -> funçoes que representam os comportamentos do objeto
ações que pode realizar no sistema

Para definir uma classe utilizamos a palavra reservada class

As classes devem ser nomeadas com a letra inicial em maiuscula,
se composto todas as palavras devem estar maiusculas

Em computacao não utilizamos: acentuação, caracteres especiais,
espaços ou similares para nomes de classes, métodos, arquivos,
diretorios, etc

Quando estamos planejando um software e definimos quais classes teremos
que ter no sistema, chamamos estes objetos que serão mapeados para classe 
de entidade.
 
class Lampada:
    pass

class ContaCorrente:
    pass

Atributos

São dividos em tres grupos:
- De instância
- De classe
- Dinâmicos

#Atributos de instância: são declarados dentro do método construtor

__init__ é o construtor do objeto


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem #Atributo da classe
        self.cor = cor #Atributo da classe
        self.ligada = False #Atributo da classe


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
        

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#Atributos Públicos/Atributos Privados

#Em python todo atributo de uma classe é publico. Se quiser privar
#deve-se utilizar duplo underscore no inicio do seu nome

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)
    
    def mostra_email(self):
        print(self.email)

#OBS: Lembre-se que isso eh apenas uma convencao, ou seja, a 
#linguagem python nao vai impedir que facamos acesso aos atributos
#sinalizados como privados fora da classe

#Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

#print(user.__senha) #AttributeError

print(user._Acesso__senha) #Temos acesso. Mas nao deveriamos fazer 
                           #esse acesso (Name Mangling)

user.mostra_senha()
user.mostra_email()

#O que significa atributos de instancia: significa que ao criarmos 
#instancias de uma classe todas as instancias tera estes atributos

#Atributos de Classe

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem #Atributo da classe
        self.cor = cor #Atributo da classe
        self.ligada = False #Atributo da classe


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
        

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)
    
    def mostra_email(self):
        print(self.email)

#Atributos de classe sao atributos que sao declarados diretamente
#na classe, ou seja, fora do construtor. Geralmente ja inicializamos
#um valor, e este valor eh compartilhado entre as classes. Ou seja,
#ao inves de cada instancia da classe ter seus proprios valores como 
#eh o caso dos atributos de instancia, com os atributos de classe todas
#as instancias terao o mesmo valor para este atributo.

#Refatorar a classe Produto

class Produto:

    imposto = 1.05 #0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Playstation', 'Videogame', 2300)
p2 = Produto('Xbox', 'Videogame', 4500)

print(p1.valor) #acesso possivel mas incorreto de um atributo de classe
print(p2.valor)

#OBS: Nao precisamos criar uma instancia de uma classe para fazer
#acesso a um atributo de classe

print(Produto.imposto) #Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

"""
#Atributos dinamicos: um atributo de instancia que pode ser criado em 
#tempo de execucao 

#OBS: sera exclusivo da instancia que o criou

class Produto:

    imposto = 1.05 #0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Playstation', 'Videogame', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

#Criando um atributo dinamico em tempo de execucao

p2.peso = '5kg' #Note que na classe produto nao existe o atributo peso

print(f'Produto = {p2.nome}, Descricao: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

#print(f'Produto = {p1.nome}, Descricao: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

#Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso #remove atributo dinamicamente

print(p1.__dict__)
print(p2.__dict__)