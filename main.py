import classes
import sistema
import menu
lista_veiculos = []
def main():

    while True:
        opcao = menu.menu_principal()
        match opcao:
            case '1':
                sistema.cadastrar(lista_veiculos)
            case '2':
                sistema.buscar(lista_veiculos)
            case '3':
                sistema.listar(lista_veiculos)


if __name__ == '__main__':
    main()