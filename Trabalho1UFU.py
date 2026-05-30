
"""
Trabalho 1 -> Programa de computador que permita realizar cadastro, consulta,
atualização e remoção (CRUD) de ativos de TI e de vulnerabilidades associadas
a esses ativos
"""
from time import sleep

#Cria uma lista de ativos vazia
ativos = {}

#Inicializador da contagem do ID de ativos cadastrados
id_ativo = 1

def cadastrar_ativo():

    from enum import Enum

    global id_ativo

#Menu de cadastros
    print("""
====MENU 2 - CADASTRO====

Bem vindo ao menu de cadastro!
    
    """ )

#Uso do Enum para classificar a lista de ativos
    class tipo_ativo(Enum):
        Notebook = 10 
        Impressora = 20
        Roteador = 30
        Software = 40

    for tipo in tipo_ativo:
        print(f"{tipo.value} - {tipo.name}") 

    codigo_ativo = int(input("Escolha o tipo de ativo: "))
    tipo_escolhido = tipo_ativo(codigo_ativo)

    nome = input("Nome do ativo: ")
    responsavel = input("Responsável: ")
    setor = input("Setor: ")

    ativos[id_ativo] = {
            "tipo": tipo_escolhido.name,
            "nome": nome,
            "responsavel": responsavel,
            "setor": setor,
            "vulnerabilidades": []
    }

    print(f"\nAtivo cadastrado com ID {id_ativo}\n\n")

    id_ativo += 1

def cadastrar_vulnerabilidade():

    from enum import Enum

    id_busca = int(input("ID do ativo: "))

    #Descrição de cada categoria de vulnerabilidade

    print("""
====Vulnerabilidades====
Descricao: Descreva mais breve possivel a vulnerabilidade;
Categoria:  Autenticação 
            Controle de acesso
            Software desatualizado
            Rede
            Banco de dados
            Configuração incorreta
          
Severidade: Baixa
            Media
            Alta
          
    Status: Aberta
            Em tratamento
            Risco aceito
            Corrigida          
========================
""" )

    if id_busca in ativos:
        lista_severidades = ["baixa", "media", "alta", "critica"]
        lista_status =["aberta", "em tratamento", "corrigida", "risco aceito"]
        
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")

        while True:

            severidade = input("Severidade: ").lower()

            if severidade in lista_severidades:
                break

            print("\nSeveridade inválida")

        while True:
        
            status = input("Status: ").lower()

            if status in lista_status:
                break

            print("\nStatus inválido")


        vulnerabilidades = {
            "descricao": descricao,
            "categoria": categoria,
            "severidade": severidade,
            "status": status
        }

        ativos[id_busca]["vulnerabilidades"].append(vulnerabilidades)

        print("\n\n\nVulnerabilidade cadastrada!")

    else:
        print("\nAtivo não encontrado")


def consultar_cadastro():
    #Verifica se existe ativos cadastrados na lista
    if not ativos:

        print("\n\nNenhum ativo cadastrado!\n\n")
        return
    
    for id_atual, dados in ativos.items():

        print("____________________________________\n")
        print(f"ID: {id_atual}")
        print(f"Tipo de ativo: {dados['tipo']}")
        print(f"Nome: {dados['nome']}")
        print(f"Responsável: {dados['responsavel']}")
        print(f"Setor: {dados['setor']}")

        print("\nVulnerabilidades associadas:\n")

        if not dados["vulnerabilidades"]:
                print("\n\nNenhuma vulnerabilidade cadastrada para esse ID.\n")

        else:

            for v in dados["vulnerabilidades"]:

                print(f"Descrição: {v['descricao']}\n")
                print(f"Categoria: {v['categoria']}\n")
                print(f"Severidade: {v['severidade']}\n")
                print(f"Status: {v['status']}\n")
                print("____________________________________\n")


def atualizar_cadastro():
    pass

def excluir_cadastro():

    global id_ativo

    id_busca = int(input("Digite o ID do ativo que deseja excluir: "))

    if id_busca in ativos:

        del ativos[id_busca]

        print("\nAtivo excluido com sucesso!")

    else: 
        print("\nAtivo não encontrado!")

#Menu de opções iniciais

def menu():

    while True:

        print(
"""====MENU 1 - INICIAL====

Opções:
1 - Cadastrar
2 - Cadastrar vulnerabilidades 
3 - Consultar 
4 - Atualizar 
5 - Excluir
6 - Sair

===========================
""")

        opcao = input("Escolha: ")

        match opcao:

            case "1":
                print("Aguarde! Abrindo cadastro de ativos...")
                sleep(2)
                cadastrar_ativo()

            case "2":
                print("\n\nAguarde! Abrindo cadastro de vulnerabilidades...\n\n")
                sleep(2)
                cadastrar_vulnerabilidade()

            case "3":
                print("\n\nAguarde! Abrindo para consulta de ativos...\n\n")
                sleep(2)
                consultar_cadastro()
    
            case "4":
                print("\n\nAguarde! Abrindo para atualizar o cadastro de ativos...\n\n")
                sleep(2)
                atualizar_cadastro()

            case "5":
                print("\n\nAguarde! Abrindo para excluir cadastro de ativo...\n\n")
                sleep(2)
                excluir_cadastro()

            case "6":
                print("Saindo... Ate logo!")
                break

            case _:
                print("Opção inválida")

menu()
