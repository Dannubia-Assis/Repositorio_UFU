
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
          
Tipos de ativo:
""" )
    
    for tipo in tipo_ativo:
        print(f"{tipo.value} - {tipo.name}") 

    print("0 - Para retornar ao menu principal")

    while True:

        try:
            codigo_ativo = int(input("\nEscolha o tipo de ativo: "))

            if codigo_ativo == 0:
                voltar_menu()
                return

            tipo_escolhido = tipo_ativo(codigo_ativo)
            break

        except ValueError:
            print("Opção inválida.")
    
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

    while True:
        try:
            id_busca = int(input("Digite o ID do ativo (0 para voltar): "))
            
            if id_busca == 0:
                voltar_menu()
                return
            break

        except ValueError:
            print("Digite apenas números!")

    if id_busca not in ativos:
        print("\nAtivo nao encontrado.")
        voltar_menu()
        return
    
    if ativos[id_busca]["vulnerabilidades"]:
        print(
        "\nEste ativo já possui uma vulnerabilidade cadastrada."
        "\nPara modificar os dados ja cadastrados va em ""4 - ATUALIZAR"" no Menu Inicial.")
        voltar_menu()
        return

    #Continua o cadastro de vulnerabilidade
    while True:
         descricao = input("Descreva a vulnerabilidade: ").strip()

         if descricao:
            break

    print("A descrição não pode ficar vazia!")
   
    print("\nCategorias da vulnerabilidade:")
    for tipo in categoria:
        print(f"{tipo.value} - {tipo.name}") 

    while True:
        try:
            codigo_categoria = int(input("\nEscolha a categoria: "))
            categoria_escolhida = categoria(codigo_categoria)
            break

        except ValueError:
            print("Categoria inválida.")

    print("\nSeveridades da vulnerabilidade:")
    for tipo in severidade:
        print(f"{tipo.value} - {tipo.name}") 

    while True:
        try:
            codigo_severidade = int(input("\nEscolha a severidade: "))
            severidade_escolhida = severidade(codigo_severidade)
            break

        except ValueError:
            print("Severidade inválida.")
    
    print("\nStatus da vulnerabilidade:")
    for tipo in status:
        print(f"{tipo.value} - {tipo.name}") 

    while True:
        try:
            codigo_status = int(input("\nEscolha o status: "))
            status_escolhido = status(codigo_status)
            break

        except ValueError:
            print("Status inválido.")

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
0 - Para retornar ao menu principal

""")      
    
    while True:

        try:
            opcao = int(input("Escolha qual tipo de dado deseja atualizar: "))

            if opcao == 0:
                voltar_menu()
                return
            break

        except ValueError:
            print("Opção inválida.")

    match opcao:

        case 1: 
            atualizar_ativo()

        case 2: 
            atualizar_vulnerabilidade()

        case _:
            print("Opcao invalida!")

def atualizar_ativo():
    
    while True:
        try:
            id_busca = int(input("Digite o ID do ativo (0 para voltar): "))

            if id_busca == 0:
                voltar_menu()
            break

        except ValueError:
            print("Digite apenas números.")
        

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
    while True:
        try:
            id_busca = int(input("Digite o ID do ativo (0 para voltar): "))

            if id_busca == 0:
                voltar_menu()
            break

        except ValueError:
            print("Digite apenas números.")

    if id_busca not in ativos:
        print("\nO ativo nao foi encontrado!")
        return
    
    vulnerabilidade = ativos[id_busca]["vulnerabilidades"]

    if not vulnerabilidade:
        print("Este ativo nao possui vulnerabilidades.")
        return

    v = vulnerabilidade[0]

    #Atualizar descricao
    descricao = input(
        f"Descrição ({v['descricao']}) (ENTER para manter): ")

    #Atualizar categoria
    
    print("\nCategorias disponiveis:")
    for item in categoria:
        print(f"{item.value} - {item.name}")

    codigo_categoria = input(f"Categoria atual ({v['categoria']}) (ENTER para manter): ")

    #Atualizar severidade
    print("\nSeveridades disponiveis:")
    for item in severidade:
        print(f"{item.value} - {item.name}")

    codigo_severidade = input(f"Severidade atual ({v['severidade']}) (ENTER para manter): ")

    #Atualizar status
    print("\nStatus disponiveis:")
    for item in status:
        print(f"{item.value} - {item.name}")

    codigo_status = input(f"Status atual ({v['status']}) (ENTER para manter): ")


    if descricao:
        v["descricao"] = descricao
        
    if codigo_categoria:
        try:
            v["categoria"] = categoria(int(codigo_categoria)).name

        except ValueError:
            print("Categoria invalida.")
    
    if codigo_severidade:
        try:
            v["severidade"] = severidade(int(codigo_severidade)).name
        
        except ValueError:
            print("Severidade invalida.")
        

    if codigo_status:
        try:
            v["status"] = status(int(codigo_status)).name

        except ValueError:
            print("Status invalido.")

    print("\nVulnerabilidade atualizada com sucesso!\n\n")

    salvar_dados()
    voltar_menu()

def excluir_cadastro():

#Menu de exclusao de cadastros
    print("""  
====MENU 5 - EXCLUIR CADASTRO====
""" )
    global id_ativo

    while True:
        try:
            id_busca = int(input("Digite o ID do ativo (0 para voltar): "))

            if id_busca == 0:
                voltar_menu()
            break

        except ValueError:
            print("Digite apenas números.")

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
              
===========MENU 1 - INICIAL===============

Escolha uma opcao para iniciar:
              
1 - Cadastrar
2 - Cadastrar vulnerabilidades 
3 - Consultar 
4 - Atualizar 
5 - Excluir
6 - Sair

==========================================
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

