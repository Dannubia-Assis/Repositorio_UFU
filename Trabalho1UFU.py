
"""
Trabalho 1 -> Programa de computador que permita realizar cadastro, consulta,
atualização e remoção (CRUD) de ativos de TI e de vulnerabilidades associadas
a esses ativos
"""

#Menu de opções
print(
"""=======MENU=======

Opções:
1 - Cadastrar 
2 - Consultar 
3 - Atualizar 
4 - Excluir
5 - Sair

==================
""")

while True:
    #Executa a escolha
    try:
        opcao = int(input("Escolha uma opção: "))


        if opcao == 1:
            print("Abrindo cadastro")

        elif opcao == 2:
            print("Abrindo consulta")

        elif opcao == 3:
            print("Abrindo atualização")

        elif opcao == 4:
            print("Excluir")

        elif opcao == ' ':
            print("Opção inválida")

        elif opcao == 5:
            print("Até mais!")
            break
            
        else:
            print("Opção inválida")

    except ValueError:
        print("Digite apenas números!!")