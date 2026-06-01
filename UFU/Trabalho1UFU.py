
"""
Trabalho 1 -> Programa de computador que permita realizar cadastro, consulta,
atualização e remoção (CRUD) de ativos de TI e de vulnerabilidades associadas
a esses ativos
"""
from time import sleep
from enum import Enum
import os
import json

#Uso do Enum para classificar a cada ativos cadastrado
class tipo_ativo(Enum):
    Notebook = 10 
    Impressora = 20
    Roteador = 30
    Software = 40

#Enum para a categoria
class categoria(Enum):
    Autenticacao = 1 
    Controle_de_acesso = 2
    Softaware_desatualizado = 3
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

#Cria uma lista de ativos vazia
ativos = {}

#Inicializador da contagem do ID de ativos cadastrados
id_ativo = 1

#Funcoes do sistema
def cadastrar_ativo():

    global id_ativo

#Menu de cadastros
    print("""  
====MENU 2 - CADASTRO DE ATIVO====

Caso deseje voltar ao menu principal digite 0!
          
Tipos de ativo:
""" )
    
    for tipo in tipo_ativo:
        print(f"{tipo.value} - {tipo.name}") 

    codigo_ativo = int(input("\n\nEscolha o tipo de ativo: "))
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

    salvar_dados()
    voltar_menu()

def cadastrar_vulnerabilidade():

    #Menu de cadastro de vulnerabilidade
    print("""  
====MENU 2 - CADASTRO DE VULNERABILIDADES====

""" )

    id_busca = int(input("Digite o ID do ativo: "))

    if ativos[id_busca]["vulnerabilidades"]:
        print(
        "\nEste ativo já possui uma vulnerabilidade cadastrada."
        "\nPara modificar os dados ja cadastrados va em ""4 - ATUALIZAR"" no Menu Inicial."
        )
        voltar_menu()
        return

    if id_busca not in ativos:
        print("\nAtivo nao encontrado.")
        voltar_menu()
        return

         #Continua o cadastro de vulnerabilidade
    descricao = input("Descreva a vulnerabilidade: ")

    print("\nCategorias da vulnerabilidade:")
    for tipo in categoria:
        print(f"{tipo.value} - {tipo.name}") 

        codigo_categoria = int(input("\n\nEscolha a categoria: "))
        categoria_escolhida = categoria(codigo_categoria)

        print("\nSeveridades da vulnerabilidade:")
        for tipo in severidade:
            print(f"{tipo.value} - {tipo.name}") 

        codigo_severidade = int(input("\n\nEscolha a severidade: "))
        severidade_escolhida = severidade(codigo_severidade)

        print("\nStatus da vulnerabilidade:")
        for tipo in status:
            print(f"{tipo.value} - {tipo.name}") 

        codigo_status = int(input("\n\nEscolha o status: "))
        status_escolhido = status(codigo_status)


        vulnerabilidade = {
            "descricao": descricao,
            "categoria": categoria_escolhida.name,
            "severidade": severidade_escolhida.name,
            "status": status_escolhido.name

        }

        ativos[id_busca]["vulnerabilidades"].append(vulnerabilidade)

        print("\n\n\nVulnerabilidade cadastrada!")
        salvar_dados()

    voltar_menu()

def consultar_cadastro():

    #Menu de consulta de cadastro
    print("""  
====MENU 3 - CONSULTA DE CADASTRO====
""" )
    #Verifica se existe ativos cadastrados na lista
    if not ativos:

        print("\n\nNenhum ativo cadastrado!\n\n")
        voltar_menu()
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

                print(f"Descrição: {v['descricao']}")
                print(f"Categoria: {v['categoria']}")
                print(f"Severidade: {v['severidade']}")
                print(f"Status: {v['status']}")
                print("____________________________________\n")

   
    voltar_menu()

def menu_atualizar_cadastro():
    
    print("""
==========MENU 4 - ATUALIZACAO DE CADASTROS==========
          
1 - Atualizar dados do ativo
2 - Atualizar dados de vulnerabilidades     
3 - Atualizar ambos     

""")      
    opcao = int(input("Escolha qual tipo de dado deseja atualizar: "))

    match opcao:

        case 1: 
            atualizar_ativo()

        case 2: 
            atualizar_vulnerabilidade()

        case 3:
            atualizar_ativo()
            atualizar_vulnerabilidade()

        case _:
            print("Opcao invalida!")

def atualizar_ativo():
    
    id_busca = int(input("\nDigite o ID do ativo: "))

    if id_busca not in ativos:
        print("\nO ativo nao foi encontrado!\n\n")
        return

    ativo = ativos[id_busca]

    print("\nPressione ENTER para manter o valor atual.")
    
    nome = input(f"Nome ({ativo['nome']}): ")
    responsavel = input(f"Responsavel ({ativo['responsavel']}): ")
    setor = input(f"Setor ({ativo['setor']}): ")
   

    if nome:
        ativo["nome"] = nome

    if responsavel:
        ativo["responsavel"] = responsavel

    if setor:
        ativo["setor"] = setor

    print("\nO cadastro foi atualizado com sucesso!")

    salvar_dados()
    voltar_menu()

def atualizar_vulnerabilidade():

    #Verifica se o ID existe e se o ativo alocado no ID possuiu vulnerabilidade cadastrada
    id_busca = int(input("Digite o ID do ativo: \n"))

    if id_busca not in ativos:
        print("\nO ativo nao foi encontrado!")
        return
    
    vulnerabilidade = ativos[id_busca]["vulnerabilidades"]

    if not vulnerabilidade:
        print("Este ativo nao possui vulnerabilidades.")
        return

    print("\nVulnerabilidades:")

    for indice, v in enumerate(vulnerabilidade, start=1):
        print(f"{indice} - {v['descricao']}")

    escolha = int(input("\nEscolha a vulnerabilidade: ")) - 1

    v = vulnerabilidade[escolha]

    descricao = input(f"Descrição ({v['descricao']}): ")
    categoria = input(f"Categoria ({v['categoria']}): ")
    severidade = input(f"Severidade ({v['severidade']}): ")
    status = input(f"Status ({v['status']}): ")

    if descricao:
        v["descricao"] = descricao

    if categoria:
        v["categoria"] = categoria

    if severidade:
        v["severidade"] = severidade

    if status:
        v["status"] = status

    print("\nVulnerabilidade atualizada!\n\n")

    salvar_dados()
    voltar_menu()

def excluir_cadastro():

#Menu de exclusao de cadastros
    print("""  
====MENU 5 - EXCLUIR CADASTRO====
""" )
    global id_ativo

    id_busca = int(input("Digite o ID do ativo que deseja excluir: "))

    if id_busca in ativos:

        del ativos[id_busca]

        print("\nAtivo excluido com sucesso!")

    else: 
        print("\nAtivo não encontrado!")

    salvar_dados()
    voltar_menu()

def salvar_dados():

    with open("ativos.json", "w", encoding="utf-8") as arquivo:

        json.dump(
            ativos,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def carregar_dados():

    global ativos
    global id_ativo

    try:
        with open("ativos.json", "r", encoding="utf-8") as arquivo:

            ativos = json.load(arquivo)

            ativos = {
                int(chave): valor
                for chave, valor in ativos.items()
            }

        if ativos:
            id_ativo = max(ativos.keys()) + 1

        else:
            id_ativo = 1

    except FileNotFoundError:

        ativos = {}
        id_ativo = 1

def voltar_menu():
    input("\nPressione ENTER para retornar ao menu inicial!")

    #Limpar tela
    os.system("cls") 

#Menu de opções iniciais
def menu():

    while True:

        print("""              
Bem vindo ao sistema CRUD de ativos de TI!
              
======MENU 1 - INICIAL=========

Escolha uma opcao para iniciar:
              
1 - Cadastrar
2 - Cadastrar vulnerabilidades 
3 - Consultar 
4 - Atualizar 
5 - Excluir
6 - Sair

===============================
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
                menu_atualizar_cadastro()

            case "5":
                print("\n\nAguarde! Abrindo para excluir cadastro de ativo...\n\n")
                sleep(2)
                excluir_cadastro()

            case "6":
                print("Saindo... Ate logo!")
                break

            case _:
                print("Digite uma opção valida!")

#Carrega os dados ao iniciar
carregar_dados()

menu()
