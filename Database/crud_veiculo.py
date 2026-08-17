from database import session
from modelos import Veiculo
from validar_database import ler_int, validar_veiculo
from utilidades import perguntar_novamente

def cadastrar_veiculo(veiculo):
    session.add(veiculo)
    session.commit()


def buscar_veiculo():
     while True:
        print("MENU DE BUSCA\n1 - BUSCAR TODOS\n2 - BUSCAR POR ID\n3 - BUSCAR POR MODELO\n4 - BUSCAR POR PLACA\n 5 - BUSCAR POR STATUS\n6 - BUSCAR POR LOCATÁRIO\n 7 - SAIR")
        escolha = ler_int("Sua opção: ")
        match escolha:
            case 1:
                print('oi')
                #listar_veiculos
            case 2:
                while True:
                    id_veiculo = ler_int("ID: ")
                    veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                    if validar_veiculo(veiculo):
                        #lista_um(veiculo):
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando a busca por ID.")
                            break
            case 3:
                while True:
                    modelo_veiculo = input("Modelo do veículo: ")
                    veiculo = session.query(Veiculo).filter_by(modelo=modelo_veiculo).first()
                    if validar_veiculo(veiculo):
                        #lista_um(veiculo)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando a busca por Modelo.")
                            break
            case 4:
                while True:
                    placa_veiculo = input("Placa do veículo: ")
                    veiculo = session.query(Veiculo).filter_by(placa=placa_veiculo).first
                    if validar_veiculo(veiculo):
                        #lista_um(veiculo)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando a buscar por Placa.")
                            break
            case 5:
                while True:
                    status_veiculo = ler_int("1 - Ativo\n2 - Inativo")
                    if status_veiculo ==  1:
                        veiculo = session.query(Veiculo).filter_by(status=True).all()
                        break
                    elif status_veiculo == 2:
                        veiculo = session.query(Veiculo).filter_by(status=False).all()
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando busca por Status.")
                            break
            case 6:
                while True:
                    id_locatario = ler_int("ID do locatário: ")
                    veiculo = session.query(Veiculo).filter_by(locatario=id_locatario).first()
                    if perguntar_novamente():
                        continue
                    else:
                        print("Encerrando busca por Locatário.")
            case 7:
                print("Encerrando menu de busca...")
                break
            case _:
                print("Opção inválida, tente novamente.")
                
                    

