from Database.crud_usuario import *
from Database.crud_veiculo import *
from Database.validar_database import *

def main():
    while True:
        login = ler_int("MENU DE LOGIN\n1 - USUÁRIOs\n2 - Veículos\n3 - SAIR")
        match login:
            case 1:
                while True:
                    menu_cliente = ler_int("MENU CLIENTE\n1 - CADASTRAR USUÁRIO\n2 - CONSULTAR USUÁRIOS\n3 - LISTAR USUÁRIOS\n4 - EXCLUIR USUÁRIO\n5 - ATUALIZAR USUÁRIOS\n6 - SAIR")
                    match menu_cliente:
                        case 1:
                            criar_usuario()
                        case 2:
                            consultar_usuario()
                        case 3:
                            listar_usuario()
                        case 4:
                            excluir_usuario()
                        case 5:
                            atualizar_cadastro()
                        case 6:
                            print("Saindo...")
                            break
                        case _:
                            print("Opção inválida, tente novamente.")
            case 2:
                while True:
                    menu_veiculos = ler_int("MENU VEÍCULOS\n1 - CADASTRAR VEÍCULO\n2 - BUSCAR VEÍCULOS\n3 - LISTAR VEÍCULOS\n4 - EXCLUIR VEÍCULO\n 5 - ATUALIZAR VEÍCULO\n6 - SAIR")
                    match menu_veiculos:
                        case 1:
                            cadastrar_veiculo()
                        case 2:
                            buscar_veiculo()
                        case 3:
                            listar_veiculo()
                        case 4:
                            excluir_veiculo()
                        case 5:
                            atualizar_veiculo()
                        case 6:
                            print("Saindo...")
                            break 
                        case _:
                            print("Opção inválida, tente novamente.")
            case 3:
                break
            case _:
                print("Opção inválida, tente novamente.")        





if __name__ == '__main__':
    main()