from classe_equipamentos import Equipamentos
from menu import menu_principal


def main():

    equipamentos = Equipamentos()

    equipamentos.carregar_dados()

    menu_principal(equipamentos)

if __name__ == "__main__":
    main()
