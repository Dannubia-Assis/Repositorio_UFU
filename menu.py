import os
from classe_ativos import Ativos
from classe_enum import tipo_ativo, severidade, status, categoria
from classe_vulnerabilidades import Vulnerabilidades
from classe_equipamentos import Equipamentos

def escolher_enum(enum_classe, mensagem, permitir_cancelar=False):

    while True:

        print(f"\n{mensagem}\n")

        for item in enum_classe:
            print(f"{item.value} - {item.name}")

        if permitir_cancelar:
            print("0 - Cancelar")

        try:

            escolha = input("\nEscolha: ")

            if permitir_cancelar and escolha == "0":
                return "CANCELAR"

            if escolha == "":
                return None

            escolha = int(escolha)

            for item in enum_classe:
                if item.value == escolha:
                    return item

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")

def cancelar_cadastro():

    print("\nCadastro cancelado.")
    voltar_menu()

def ler_texto(mensagem, permitir_enter=False):

    while True:

        texto = input(mensagem).strip()

        # Cancelar
        if texto == "0":
            return None

        # Atualização: ENTER mantém o valor
        if permitir_enter and texto == "":
            return ""

        # Cadastro: não pode ficar vazio
        if texto == "":
            print("O campo não pode ficar vazio.")
            continue

        if len(texto) < 3:
            print("O campo deve possuir pelo menos 3 caracteres.")
            continue

        return texto

def voltar_menu():
    input("\nPressione ENTER para retornar ao menu inicial!")

    limpar_tela()
    
def limpar_tela():

    print("Limpando...")
    os.system("cls" if os.name == "nt" else "clear")

def escolher_indice(mensagem, lista):

    while True:

        try:

            escolha = int(input(mensagem))


            if escolha == 0:
                return None


            indice = escolha - 1


            if indice < 0 or indice >= len(lista):
                print("Índice inválido.")
                continue


            return indice


        except ValueError:
            print("Digite apenas números.")

def menu_principal(equipamento):

    while True:

        print("""              
Bem vindo(a) ao sistema de gerenciamento de ativos
              
===========MENU 1 - INICIAL===============

Escolha uma opcao para iniciar:
              
1 - Cadastrar ativo
2 - Cadastrar vulnerabilidade do ativo
3 - Buscar ativo pelo ID              
4 - Atualizar cadastro  
5 - Remover cadastro 
6 - Sair

==========================================
""")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":
                print("============CADASTRO DE ATIVO============\n")
                #Escolher o tipo atraves do ENUM
                tipo = escolher_enum(tipo_ativo, "Tipos")

                if tipo is None:
                    cancelar_cadastro()
                    continue
                
                nome = ler_texto("Digite o nome do equipamento: ")

                if nome is None:
                    cancelar_cadastro()
                    continue

                responsavel = ler_texto("Digite o responsável: ")

                if responsavel is None:
                    cancelar_cadastro()
                    continue

                setor = ler_texto("Digite o setor: ")

                if setor is None:
                    cancelar_cadastro()
                    continue
             
                novo_ativo = Ativos(tipo, nome, responsavel, setor)
                equipamento.cadastrar_ativo(novo_ativo)
                equipamento.salvar_dados()

                print(f'\nAtivo cadastrado com sucesso no ID: {novo_ativo.id}!')

                voltar_menu()

            case "2":
                print("============CADASTRO DE VULNERABILIDADES============\n")
                while True:
                    try:
                        id_procurado = int(input("\nDigite o ID do ativo: "))
                        
                        if id_procurado == 0:
                            voltar_menu()
                            continue 
                        break

                    except ValueError:
                        print("\nDigite apenas números!")

                #Continua o cadastro de vulnerabilidade

                ativo = equipamento.buscar_cadastro_ativo(id_procurado)

                if ativo is None:
                    print("\nAtivo não encontrado.")
                    voltar_menu()
                    continue

                print("\nAtivo encontrado:")
                ativo.imprimir_ativo()  

                print("\nVulnerabilidades do ativo:")

                ativo.imprimir_vulnerabilidades()

                while True:
                    descricao = input("Descreva a vulnerabilidade: ").strip()

                    if descricao:
                        break

                    print("\nA descrição não pode ficar vazia!")

                categoria_escolhida = escolher_enum(categoria, "Categorias",
    permitir_cancelar=True)

                if categoria_escolhida == "CANCELAR":
                    cancelar_cadastro()
                    continue
                severidade_escolhida = escolher_enum(severidade, "Severidades",
    permitir_cancelar=True)

                if severidade_escolhida == "CANCELAR":
                    cancelar_cadastro()
                    continue
                status_escolhido = escolher_enum(status, "Status",
    permitir_cancelar=True)

                if status_escolhido == "CANCELAR":
                    cancelar_cadastro()
                    continue
                
                #Criando o objeto de vulnerabilidades
                nova_vulnerabilidade = Vulnerabilidades(
                    descricao=descricao,
                    categoria=categoria_escolhida,
                    severidade=severidade_escolhida,
                    status=status_escolhido)    

                ativo.adicionar_vulnerabilidade(nova_vulnerabilidade)

                equipamento.salvar_dados()

                print("\nVulnerabilidade cadastrada com sucesso!\n")

                nova_vulnerabilidade.imprimir()

                voltar_menu()

            case "3":
                print("============BUSCAR CADASTRO============\n")
                
                id_procurado = int(input("Digite o ID: "))
                ativo = equipamento.buscar_cadastro_ativo(id_procurado)
                print('\nAqui está o resultado da sua pesquisa: ')

                if ativo: 
                    ativo.imprimir_ativo()

                    print("\nVulnerabilidades do ativo:")

                    ativo.imprimir_vulnerabilidades()
                else:
                    print("\nNenhum ativo cadastrado nesse ID.\n")
               
                voltar_menu()

            case "4":
                while True:

                        print("""                           
============ATUALIZAR CADASTRO============

Escolha a opcao para atualizar:
              
1 - Atualizar cadastro de ativo
2 - Atualizar cadastro de vulnerabilidade 
    do ativo
0 - Cancelar

=========================================
""")
                        opcao = input("\nEscolha: ")
                        match opcao:
                    
                            case "1":
                
                                id_procurado = int(input("Digite o ID: "))
                                ativo = equipamento.buscar_cadastro_ativo(id_procurado)

                                if ativo is None:
                                    print("\nNenhum ativo cadastrado nesse ID.")
                                    voltar_menu()
                                    continue

                                print("\nAqui está o resultado da sua pesquisa:\n")
                                ativo.imprimir_ativo()

                                print("\nVulnerabilidades do ativo:\n")
                                ativo.imprimir_vulnerabilidades()

                                print(
                                "\nENTER - Manter o que nao deseja alterar\n"
                                "0 - Cancelar")

                                #Atualiza o cadastro de os ativos
                                novo_tipo = escolher_enum(tipo_ativo, "Novo tipo")

                                if novo_tipo == "CANCELAR":
                                    print("Operação cancelada.")
                                    break

                                novo_nome = ler_texto(f"Novo nome (Enter para manter '{ativo.nome}'): ",
                                permitir_enter=True)

                                novo_responsavel = ler_texto(f"Novo responsável (Enter para manter '{ativo.responsavel}'): ",
                                permitir_enter=True)

                                novo_setor = ler_texto(f"Novo setor (Enter para manter '{ativo.setor}'): ",
                                permitir_enter=True)

                                try:

                                    equipamento.atualizar_ativo(
                                        id_procurado,
                                        novo_tipo,
                                        novo_nome,
                                        novo_responsavel,
                                        novo_setor)
                    
                                    equipamento.salvar_dados()
                                    print("\nCadastro de ativo atualizado com sucesso!")

                                except ValueError as erro:
                                    print(erro)

                                voltar_menu()
                                break

                            case "2":

                                id_procurado = int(input("Digite o ID: "))
                                ativo = equipamento.buscar_cadastro_ativo(id_procurado)

                                if ativo is None:
                                    print("\nNenhum ativo cadastrado nesse ID.")
                                    voltar_menu()
                                    continue

                                print("\nAqui está o resultado da sua pesquisa:\n")
                                ativo.imprimir_ativo()

                                print("\nVulnerabilidades do ativo:\n")
                                ativo.imprimir_vulnerabilidades()

                                print(
                                "\nENTER - Manter o que nao deseja alterar\n"
                                "0 - Cancelar")
                                
                                #Atualiza o cadastro de vulneravilidades

                                if not ativo.vulnerabilidades:
                                    print("\nNenhuma vulnerabilidade cadastrada para este ativo.")
                                    voltar_menu()
                                    break
                                
                                indice = escolher_indice("\nQual vulnerabilidade deseja atualizar? ",
                                ativo.vulnerabilidades)

                                if indice is None:
                                    print("\nOperação cancelada.")
                                    voltar_menu()
                                    break

                                nova_descricao = ler_texto("Nova descrição (Enter para manter): ",
                                permitir_enter=True)

                                nova_categoria = escolher_enum(categoria, "Nova categoria")

                                nova_severidade = escolher_enum(severidade, "Nova severidade")

                                novo_status = escolher_enum(status, "Novo status")

                                try:

                                    ativo.atualizar_vulnerabilidade(
                                        indice,
                                        nova_descricao,
                                        nova_categoria,
                                        nova_severidade,
                                        novo_status)
                    
                                    equipamento.salvar_dados()
                                    print("\nCadastro de vulnerabilidade atualizado com sucesso!")

                                except ValueError as erro:
                                    print(erro)

                                voltar_menu()
                                break

                            case "0":
                                print("\nOperação cancelada.")
                                voltar_menu()
                                break

                            case _:
                                print("Opção inválida")

            case "5":

                    while True:

                        print("""                           
============REMOVER CADASTRO============

Escolha a opcao para remover:
              
1 - Remover cadastro de ativo
2 - Remover cadastro de vulnerabilidade 
    do ativo
0 - Cancelar

=========================================
""")
                        opcao = input("\nEscolha: ")
                        match opcao:
                    
                            case "1":
                
                                id_procurado = int(input("Digite o ID: "))
                                print()
                                ativo = equipamento.excluir_cadastro(id_procurado)
                                
                                if ativo:
                                    equipamento.salvar_dados()
                                    print("\nCadastro de ativo excluído com sucesso!\n") 
                           
                                else: 
                                    print(f'Confirme se o ID:{id_procurado} está cadastrado!')

                                voltar_menu()
                                break

                            case "2":
                                    
                                    id_procurado = int(input("Digite o ID do ativo: "))

                                    ativo = equipamento.buscar_cadastro_ativo(id_procurado)

                                    if ativo is None:
                                        print("\nNenhum ativo encontrado nesse ID.")
                                        voltar_menu()
                                        continue


                                    ativo.imprimir_vulnerabilidades()


                                    indice = int(
                                    input("\nQual vulnerabilidade deseja remover? ")) - 1


                                    try:
                                        ativo.remover_vulnerabilidade(indice)

                                        equipamento.salvar_dados()

                                        print("\nVulnerabilidade removida com sucesso!")

                                    except ValueError as erro:
                                        print(erro)

                                    voltar_menu()
                                    break
                            case _:
                                print("Opção inválida")

            case "6":
                print("Saindo... Até logo!")
                break

            case _:
                print("Digite uma opção válida!")


