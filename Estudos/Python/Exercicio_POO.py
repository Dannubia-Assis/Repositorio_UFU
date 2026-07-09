"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato); OK
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda. OK
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

"""

#A classe Agenda solicita a classe Contato que modifique os dados: isso eh encapsulamento.
#Os setters permitem a alteracao dos dados ja incluindo as validacoes dentro da classe contato
import os

class Contato():

    contador = 0

    def __init__(self, nome, telefone, email):
        Contato.contador += 1
        self.__id = Contato.contador
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
    
    def __str__(self):
        return f'{self.__id} - {self.__nome}'
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome): #Recebe o objeto contato e o novo telefone
        if len(str(novo_nome)) < 3:
            raise ValueError
        
        self.__nome = novo_nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone): #Recebe o objeto contato e o novo telefone
        if len(str(novo_telefone)) < 8:
            raise ValueError
        
        self.__telefone = novo_telefone

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email): #Recebe o objeto contato e o novo telefone
        if len(str(novo_email)) < 5:
            raise ValueError
        
        self.__email = novo_email
        
    def imprimir_contato(self):

        print('______________________________')
        print(f'ID:{self.__id}')
        print(f'Nome:{self.__nome}')
        print(f'Telefone:{self.__telefone}')
        print(f'E-mail:{self.__email}')
        
class Agenda():
   
    def __init__(agenda):
       agenda.contatos = []

    def cadastrar_contato(self, contato):
       self.contatos.append(contato) #Adiciona o contato a lista self.contatos[]
       print()
       print('Contato cadastrado com sucesso!')

    def buscar_contato(self, id):

        for contato in self.contatos: #Percorre a lista
             
             if contato.id == id: #Encontra o ID correspondente
                return contato #Dessa forma ele retorna o contato e da para usar a busca em outros metodos

        return None
     
    def atualizar_contato(self, id):

        contato = self.buscar_contato(id)

        if contato is None:
            print("Contato nao encontrado.")
            return
            
        while True:

            try:
                novo_nome = input("Novo nome: ")
                contato.nome = novo_nome
                break

            except ValueError:
                print("Digite um nome valido!")
        
        while True:

            try: 
                novo_telefone = input("Novo telefone: ")
                contato.telefone = novo_telefone
                break

            except ValueError:
                print("Digite um telefone valido!")
       
        while True:

            try:
                novo_email = input("Novo e-mail: ")
                contato.email = novo_email
                break

            except ValueError:
                print("Digite um email valido!")

        return contato
         
    def imprimir_agenda(self):
        print()
        print('Lista de contatos:')
        print()
        print(f'Existem {len(agenda.contatos)} salvos na sua agenda!')

        for contato in self.contatos:
            contato.imprimir_contato() #Ele retorna cada contato de acordo com a lista

    def remover_contato(self, id):

        contato = self.buscar_contato(id)

        if contato is None:
            print("Contato nao encontrado.")
            return
        
        self.contatos.remove(contato)

        return True
        
      
agenda = Agenda()

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def menu():

    while True:

        limpar()

        print("""              
Bem vindo(a) a sua agenda virtual!
              
===========MENU 1 - INICIAL===============

Escolha uma opcao para iniciar:
              
1 - Cadastrar contato
2 - Buscar contato pelo ID              
3 - Atualizar contato pelo ID
4 - Exibir toda a agenda
5 - Remover contato
6 - Sair

==========================================
""")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                print()
                novo_nome = input("Digite o nome: ")
                novo_telefone = input("Digite o numero de telefone: ")
                novo_email = input("Digite o novo email: ")

                novo_contato = Contato(novo_nome, novo_telefone, novo_email)
                agenda.cadastrar_contato(novo_contato)

                input("\nPressione Enter para voltar ao menu...")

            case "2":

                print()
                id_procurado = int(input("Digite o ID: "))
                print()
                contato = agenda.buscar_contato(id_procurado)
                print('Aqui está o resultado da sua pesquisa: ')

                if contato: 
                    contato.imprimir_contato()
                    print()
        
                else: 
                    print('Contato não encontrado')

                input("\nPressione Enter para voltar ao menu...")

            case "3":
                
                id_procurado = int(input("Digite o ID: "))
                print()
                contato = agenda.atualizar_contato(id_procurado)
                print()

                if contato:
                    print("Contato atualizado com sucesso!") 
                    contato.imprimir_contato()
                    print()
        
                else: 
                    print('Contato não encontrado')

                input("\nPressione Enter para voltar ao menu...")

            case "4":
                agenda.imprimir_agenda()

                input("\nPressione Enter para voltar ao menu...")

            case "5":

                id_procurado = int(input("Digite o ID: "))
                print()
                contato = agenda.remover_contato(id_procurado)
                print()

                if contato:
                    print("Contato removido da sua agenda com sucesso!") 
                    print()

                else: 
                    print('Contato não encontrado')

                input("\nPressione Enter para voltar ao menu...")
                
            case "6":
                print("Saindo... Até logo!")
                break

            case _:
                print("Digite uma opção válida!")

menu()



