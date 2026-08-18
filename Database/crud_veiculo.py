from database import session
from modelos import Veiculo
from validar_database import ler_int, validar_veiculo
from utilidades import perguntar_novamente, validar_sn

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
                listar_veiculo()
            case 2:
                while True:
                    id_veiculo = ler_int("ID: ")
                    veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                    if validar_veiculo(veiculo):
                        lista_um(veiculo)
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
                        lista_um(veiculo)
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
                        lista_um(veiculo)
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
                        for v in veiculo:
                            lista_um(v)
                        break
                    elif status_veiculo == 2:
                        veiculo = session.query(Veiculo).filter_by(status=False).all()
                        for v in veiculo:
                            lista_um(v)
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


def lista_um(veiculo):
    print(f"ID: {veiculo.id}\nMODELO: {veiculo.modelo}\nPLACA: {veiculo.placa}\nVALOR DIÁRIO: {veiculo.valor_diario}\nSTATUS: {'Alugado' if veiculo.status else 'Disponível'}\nID DO LOCATÁRIO: {veiculo.locatario if veiculo.status else 'Veículo Alugado'}")


def listar_veiculo():
    veiculos = session.query(Veiculo).all()
    for veiculo in veiculos:
        print(f"ID: {veiculo.id}\nMODELO: {veiculo.modelo}\nPLACA: {veiculo.placa}\nVALOR DIÁRIO: {veiculo.valor_diario}\nSTATUS: {'Alugado' if veiculo.status else 'Disponível'}\nID DO LOCATÁRIO: {veiculo.locatario if veiculo.status else 'Veículo Alugado'}")

def excluir_veiculo():
    while True:
        listar_veiculo()
        id_exclusao = ler_int("ID do veículo que deseja excluir: ")
        if id_exclusao == 0:
            print('Operação cancelada')
            return
        veiculo = session.query(Veiculo).filter_by(id=id_exclusao).first()
        if validar_veiculo(veiculo):
            verificador = validar_sn(f'Tem certeza que deseja excluir o usuario {id_exclusao}, [S/N]: ').upper().strip()
            if verificador and verificador[0] == 'S':
                session.delete(veiculo)
                session.commit()
                print('Usuário excluído, encerrando sistema de exclusão.')
                return
            else:
                print('Exclusão cancelada, encerrando sistema de exclusão.')
        else:
            print('Veículo não encontrado, tente novamente.')


def atualizar_veiculo():
    while True:
        print("MENU ATUALIZAR\n 1 - ATUALIZAR TUDO\n2 - ATUALIZAR MODELO\n3 - ATUALIZAR PLACA\n4 - ATUALIZAR VALOR DIÁRIO\n5 - ATUALIZAR STATUS\n6 - ATUALIZAR LOCATÁRIO\n7 - SAIR")
        opcao = ler_int("Opção: ")
        match opcao:
            case 1:
                id_veiculo = ler_int("ID do veículo: ")
                novo_modelo = input("Novo modelo: ")
                nova_placa = input("Nova placa: ") #necessário inserir o validar placa.
                novo_valor = ler_int("Novo valor diário: ")
                novo_locatario = ler_int("Novo locatário: ")
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_sn(veiculo):
                    veiculo.modelo = novo_modelo
                    veiculo.placa = nova_placa
                    veiculo.valor_diario = novo_valor
                    veiculo.locatario = novo_locatario
                    status = validar_sn("Deseja alterar o status? [S/N]: ")
                    if status:
                        veiculo.status = not veiculo.status
                        print("Modelo, Placa, Valor Diário, Locatário e Status alterados com sucesso.")
                    else:
                        print("Modelo, Placa, Valor Diário e Locatário alterados com sucesso.")
                    session.commit()
            case 2:
                id_veiculo = ler_int("ID do veículo: ")
                novo_modelo = input("Novo modelo: ")
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo):
                    veiculo.modelo = novo_modelo
                    session.commit()
            case 3:
                id_veiculo = ler_int("ID do veículo: ")
                nova_placa = input("Nova placa: ")
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo):
                    veiculo.placa = nova_placa
                    session.commit()
            case 4:
                id_veiculo = ler_int("ID do veículo: ")
                novo_valor = ler_int("Novo valor: ")
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo):
                    veiculo.valor_diario = novo_valor
                    session.commit()
            case 5:
                id_veiculo = ler_int("ID do veículo: ")
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo):
                    veiculo.status = not veiculo.status
                    session.commit()
            case 6:
                id_veiculo = ler_int("ID do veículo: ")
                novo_locatario = ler_int("ID do locatário: ")
                veiculo = session.query(Veiculo).filter_by(id=id_veiculo).first()
                if validar_veiculo(veiculo) and novo_locatario in Veiculo.locatario:
                    veiculo.locatario = novo_locatario
                    session.commit()
            case 7:
                print("Encerrando o sistema de atualização.")
                break
            case _:
                print("Opção inválida, tente novamente.")
