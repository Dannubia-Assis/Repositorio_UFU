"""
Heranca (Inheritance)

A ideia de heranca eh a de reaproveitar codigos e tambem extender nossas 
classes.

OBS: Com a heranca a partir de uma classe existente, nos extendemos outra classe que passa
a herdar atributos e metodos de classe herdada.

Cliente
    -nome;
    -sobrenome;
    -cpf;
    -renda;

Funcionario
    -nome;
    -sobrenome;
    -cpf:
    -matricula;

OBS: quando uma classe herda de outra classe ela herda todos os atributos e 
metodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada eh conhecida por:
[Pessoa]
- Super classe,
- classe pai
- classe mae
- base
- classe generica

Quando uma classe herda de outra classe, ela eh chamada:
[Cliente, Funcionario]
- Sub classe
- classe filha
- classe especifica
"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome    
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa): #Heranca - cliente herda da classe Pessoa
    
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa. __init__(self, nome, sobrenome, cpf) #Da acesso a super classe/Forma nao comum de acessar a super classe
        self.__renda = renda

class Funcionario(Pessoa): #Heranca - funcionario herda da classe Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super(). __init__(nome, sobrenome, cpf) #Da acesso a super classe/Forma comum de acessar a super classe
        self.__matricula = matricula
    
    def nome_completo(self): #Sobre escrita de metodos (Overrinding)
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'

    

cliente1 = Cliente('Dannubia', 'de Assis', '758.098.739-98', 5000)

funcionario1 = Funcionario('Guilherme', 'Silva', '233.345.739-00', 10000)

#print(cliente1.nome_completo())

#print(funcionario1.nome_completo())

#print(cliente1.__dict__)

#print(funcionario1.__dict__)

print(cliente1.nome_completo())

funcionario1.nome_completo()