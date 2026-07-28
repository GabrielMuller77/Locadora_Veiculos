import classes
import sistema
import menu
lista_veiculos = []
def main():

    while True:
        usuario = int(input('Que tipo de usuário você é:\n1 - Funcionário\n2 - Cliente\n3 - Sair\nOpção: '))
        if usuario == 1:
            while True:
                opcao_locadora = menu.menu_principal()
                match opcao_locadora:
                    case '1':
                        sistema.cadastrar(lista_veiculos)
                    case '2':
                        sistema.buscar(lista_veiculos)
                    case '3':
                        sistema.listar(lista_veiculos)
                    case '4':
                        sistema.excluir(lista_veiculos)
                    case '5':
                        print('Saindo...')
                        break
                    case _:
                        print('Opção inválida, tente novamente.')
        elif usuario == 2:
            while True:
                opcao_cliente = menu.menu_cliente()
                match opcao_cliente:
                    case '1':
                        sistema.alugar(lista_veiculos)
                    case '2':
                        sistema.devolver(lista_veiculos)
                    case '3':
                        print('Agradecemos a preferência')
                        break
                    case _:
                        print('Opção inválida, tente novamente')
        elif usuario == 3:
            print('Saindo...')
            break
        else:
            print('Opção inválida, tente novamente.')


if __name__ == '__main__':
    main()