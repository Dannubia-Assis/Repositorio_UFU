"""
Trabalho 2 - uma aplicação que cadastra equipamentos e vulnerabilidades, associando a estes equipamentos cadastrados as vulnerabilidades
também cadastradas. Os requisitos do trabalho anterior se preservam. Todavia, neste trabalho, são
tragas duas novidades:
1) você tem que reescrever seu programa todo no paradigma de orientação a objetos,
trabalhando com classes e objetos e seus recursos associados (herança, polimorfismos, etc).
2) Deixar sua aplicação em orientação a objetos executando em um container Docker.
"""
from enum import Enum
import os

#Uso do Enum para classificar a cada ativos cadastrado
class tipo_ativo(Enum):
    Notebook = 10 
    Impressora = 20
    Roteador = 30
    Software = 40

#Enum para a categoria
class categoria(Enum):
    Autenticação = 1 
    Controle_de_acesso = 2
    Software_desatualizado = 3
    Rede= 4
    Banco_de_dados = 5
    Configuração_incorreta = 6

#Enum para a severidade
class severidade(Enum):
    Baixa = 1 
    Media = 2
    Alta = 3

#Enum para o status    
class status(Enum):
    Aberta = 1 
    Em_tratamento = 2
    Risco_aceito = 3
    Corrigida = 4

class Ativos():

    contator = 0
    #Criando o objeto ativo
    def __init__(self, tipo, nome, responsavel, setor):

        Ativos.contator += 1
        self.__id = Ativos.contator 
        self.__tipo = tipo
        self.__nome = nome
        self.__responsavel = responsavel
        self.__setor = setor
        self.vulnerabilidades = [] #Lista de vulnerabilidades vinculado ao número de ID do ativo

    def cadastro_vulnerabilidade(self, vulnerabilidade):
        self.vulnerabilidades.append(vulnerabilidade)

    def buscar_vulnerabilidade(self, id):

        for vulnerabilidade in self.vulnerabilidades: #Percorre a lista
             
             if vulnerabilidade.id == id: #Encontra o ID correspondente
                return vulnerabilidade #Dessa forma ele retorna o contato e da para usar a busca em outros metodos

        return None
     
    def atualizar_vulnerabilidade(self, id):

        vulnerabilidade = self.buscar_vulnerabilidade(id)

        if vulnerabilidade is None:
            print("ID nao encontrado.")
            return
            
        while True:

            try:
                nova_descricao = input("Nova descrição: ")
                vulnerabilidade.descricao = nova_descricao
                break

            except "":
                print("A descrição não pode ficar vazia.")
        
        while True:

            try: 
                nova_categoria = input("Nova categoria: ")
                vulnerabilidade.categoria = nova_categoria
                break

            except ValueError:
                print("Digite uma categoria válida!")
       
        while True:

            try:
                nova_severidade = input("Nova severidade: ")
                vulnerabilidade.severidade = nova_severidade
                break

            except ValueError:
                print("Digite uma severidade válida!")

        return vulnerabilidade
    
    def remover_vulnerabilidade(self, id):

        vulnerabilidade = self.buscar_vulnerabilidade(id)

        if vulnerabilidade is None:
            print("ID nao encontrado.")
            return
        
        self.vulnerabilidade.remove(vulnerabilidade)

        return True
    
    def imprimir_ativo(self):

        print('______________________________')
        print(f'ID:{self.__id}')
        print(f'Tipo:{self.__tipo}')
        print(f'Nome:{self.__nome}')
        print(f'Responsável:{self.__responsavel}')


    #Criando as propertys e setters para que a classe equipamentos manipule os atributos
    #da classe ativos
    
    @property
    def id(self):
        return self.__id
    
    #Como o ID é um informação do ativo que não pode ser alterada ela contém apenas
    #A classe equipamentos apenas vai ter acesso de fazer o uso do atributo sem alterar 
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, novo_tipo):
        if len(str(novo_tipo)) < 3: #Ainda tem que ajustar essa validação
            raise ValueError
        
        self.__tipo = novo_tipo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if len(str(novo_nome)) < 3: #Ainda tem que ajustar essa validação
            raise ValueError
        
        self.__nome = novo_nome
    
    @property
    def responsavel(self):
        return self.__responsavel
    
    @responsavel.setter
    def responsavel(self, novo_responsavel):
        if len(str(novo_responsavel)) < 3: #Ainda tem que ajustar essa validação
            raise ValueError
        
        self.__responsavel = novo_responsavel
    
    @property
    def setor(self):
        return self.__setor
    
    @setor.setter
    def setor(self, novo_setor):
        if len(str(novo_setor)) < 3: #Ainda tem que ajustar essa validação
            raise ValueError
        
        self.__setor = novo_setor

class Vulnerabilidades():

    def __init__(self, descricao, categoria, severidade, status):

        self.__descricao = descricao
        self.__categoria = categoria
        self.__severidade = severidade
        self.__status = status

    def imprimir_vulnerabilidades(self):

        print('______________________________')
        print(f'ID:{self.__id}')
        print(f'Descrição:{self.__descricao}')
        print(f'Categoria:{self.__categoria}')
        print(f'Severidade:{self.__severidade}')
        print(f'Status:{self.__status}')
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_descricao):
        if len(str(nova_descricao)) < 3: 
            raise ValueError
        
        self.__descricao = nova_descricao
        
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nova_categoria):
        
        if not isinstance(nova_categoria, categoria): 
            raise TypeError("Valor inválido.") #Mais uma camada de proteção que garante que 
                                                #a opção escolhida esteja no enum
        self.__categoria = nova_categoria
        
    @property
    def severidade(self):
        return self.__severidade
    
    @severidade.setter
    def severidade(self, nova_severidade):

        if not isinstance(nova_severidade, severidade):
            raise TypeError("Valor inválido.")

        self.__severidade = nova_severidade

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):

        if not isinstance(novo_status, status):
            raise TypeError("Valor inválido.")

        self.__status = novo_status
        
    def imprimir_vulnerabilidades(self):

        print('______________________________')
        print(f'ID:{self.__id}')
        print(f'Descrição:{self.__descricao}')
        print(f'Categoria:{self.__categoria}')
        print(f'Severidade:{self.__severidade}')
        print(f'Status:{self.__status}')

class Equipamentos():

    def __init__(equipamento):
         
        equipamento.ativos = [] #Armazena os dados do ativo em uma lista

    #Criando os módulos para manipular as propriedades da classe ativo
    def cadastrar_ativo(self, ativo):
        equipamento.ativos.append(ativo) #Adiciona o ativo na lista de ativos da classe equipamentos
                                    #como um dicionário
        print()
        print('Ativo cadastrado com sucesso!')

    def buscar_cadastro_ativo(self, id):

        for ativo in equipamento.ativos: #Percorre a lista
             
             if ativo.id == id: #Encontra o ID correspondente
                return ativo #Dessa forma ele retorna o contato e da para usar a busca em outros metodos

        return None
    
    def atualizar_ativo(self, id):

        ativo = self.buscar_cadastro_ativo(id)

        if ativo is None:
            print("ID nao encontrado.")
            return
            
        while True:

            try:
                novo_tipo = input("Novo tipo: ")
                ativo.tipo = novo_tipo
                break

            except ValueError:
                print("Digite um tipo válido!")
        
        while True:

            try: 
                novo_nome = input("Novo nome: ")
                ativo.nome = novo_nome
                break

            except ValueError:
                print("Digite um nome válido!")
       
        while True:

            try:
                novo_responsavel = input("Novo responsavel: ")
                ativo.responsavel = novo_responsavel
                break

            except ValueError:
                print("Digite um responsavel válido!")

        return ativo
    
    def excluir_cadastro(self,id):

        ativo = self.buscar_cadastro_ativo(id)

        if ativo is None:
            print("ID nao encontrado.")
            return
        
        self.ativo.remove(ativo)

        return True
        

equipamento = Equipamentos() #Criando o objeto equipamento

def voltar_menu():
    input("\nPressione ENTER para retornar ao menu inicial!")

    #Limpar tela
    os.system("cls") 

def menu():

    while True:

        print("""              
Bem vindo(a) ao sistema de gerenciamento de ativos
              
===========MENU 1 - INICIAL===============

Escolha uma opcao para iniciar:
              
1 - Cadastrar ativo
2 - Cadastrar vulnerabilidade do ativo
3 - Buscar ativo pelo ID              
4 - Atualizar cadastro do ativo 
5 - Atualizar cadastro de vulnerabilidades
6 - Remover cadastro de ativo
7 - Sair

==========================================
""")

        opcao = input("Escolha: ")

        match opcao:

            case "1":

                for tipo in tipo_ativo:
                    print(f"{tipo.value} - {tipo.name}") 

                print("0 - Para retornar ao menu principal")
                 
                while True:

                    try:
                        codigo_ativo = int(input("\nEscolha o tipo de ativo: "))

                        if codigo_ativo == 0:
                            voltar_menu()
                            return

                        tipo = tipo_ativo(codigo_ativo)
                        break

                    except ValueError:
                        print("Opção inválida.")

                print()

                nome = input("Digite o nome: ")
                responsavel = input("Digite o responsavel: ")
                setor = input("Digite o setor: ")

                novo_ativo = Ativos(tipo, nome, responsavel, setor)
                equipamento.cadastrar_ativo(novo_ativo)

                input("\nPressione Enter para voltar ao menu...")

            case "2":


                id_procurado = int(input("Digite o ID: "))
                print()
                ativo = Ativos.cadastro_vulnerabilidade(id_procurado)
                print()

                if ativo:
                    print("A vulnerabilidade do ativo foi atualizado com sucesso!") 
                    ativo.imprimir_vulnerabilidades()
                    print()

                else: 
                    print('Contato não encontrado')

                input("\nPressione Enter para voltar ao menu...")


            case "3":

                print()
                id_procurado = int(input("Digite o ID: "))
                print()
                ativo = equipamento.buscar_cadastro_ativo(id_procurado)
                print('Aqui está o resultado da sua pesquisa: ')

                if ativo: 
                    ativo.imprimir_ativo()
                    print()
        
                else: 
                    print('ID não encontrado')

                input("\nPressione Enter para voltar ao menu...")

            case "3":
                
                id_procurado = int(input("Digite o ID: "))
                print()
                ativo = agenda.atualizar_contato(id_procurado)
                print()

                if contato:
                    print("Contato atualizado com sucesso!") 
                    contato.imprimir_()
                    print()
        
                else: 
                    print('Contato não encontrado')

                input("\nPressione Enter para voltar ao menu...")

            case "4":
                agenda.imprimir_agenda()

                input("\nPressione Enter para voltar ao menu...")

            case "5":

                pass
                
            case "6":

                id_procurado = int(input("Digite o ID: "))
                print()
                ativo = equipamento.excluir_cadastro(id_procurado)
                print()

                if ativo:
                    print("Cadastro de ativo excluído com sucesso!") 
                    print()

                else: 
                    print('Contato não encontrado')

                input("\nPressione Enter para voltar ao menu...")

            case "7":
                print("Saindo... Até logo!")
                break
            case _:
                print("Digite uma opção válida!")

menu()

