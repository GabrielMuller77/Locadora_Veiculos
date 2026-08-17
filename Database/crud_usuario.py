from database import session
from modelos import Usuario
from validar_database import validar_usuario, ler_int
from utilidades import perguntar_novamente, validar_sn


def criar_usuario(usuario):
    session.add(usuario)
    session.commit()


def consultar_usuario():
    while True:
        print("MENU DE CONSULTA\n1 - BUSCAR TODOS\n2 - BUSCAR PELO ID\n3 - BUSCAR PELO EMAIL\n4 - SAIR")
        escolha = ler_int("Opção: ")
        match escolha:
            case 1:
                listar_usuario()
            case 2:
                while True:
                    id_usuario = ler_int("ID: ")
                    usuario = session.query(Usuario).filter_by(id=id_usuario).first()
                    if validar_usuario(usuario):
                        listar_um(usuario)
                        break
                    else:
                        if perguntar_novamente():
                            continue 
                        else:
                            print("Encerrando a consulta por ID.")
                            break           
            case 3:
                while True:
                    email_usuario = input("Email: ")
                    usuario = session.query(Usuario).filter_by(email=email_usuario).first()
                    if validar_usuario(usuario):
                        listar_um(usuario)
                        break
                    else:
                        if perguntar_novamente():
                            continue
                        else:
                            print("Encerrando consulta por Email.")                
            case 4:
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente")


def listar_usuario():
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}\nNOME: {usuario.nome}\nEMAIL: {usuario.email}\nSTATUS: {'Ativo' if usuario.ativo else 'Inativo'}\n")
        print('-='*20)


def listar_um(usuario):
        print(f"ID: {usuario.id}\nNOME: {usuario.nome}\nEMAIL: {usuario.email}\nSTATUS: {'Ativo' if usuario.ativo else 'Inativo'}\n")



def excluir_usuario():
    while True:
        listar_usuario()
        id_exclusao = ler_int('Informe o ID do usuário que deseja excluir, 0 para cancelar: ')
        if id_exclusao == 0:
            print('Operação cancelada')
            return
        usuario = session.query(Usuario).filter_by(id=id_exclusao).first()
        if validar_usuario(usuario):
            while True:
                verificador = input(f'Tem certeza que deseja excluir o usuario {id_exclusao}, [S/N]: ').upper().strip()
                if verificador and verificador[0] == 'S':
                    session.delete(usuario)
                    session.commit()
                    print('Usuário excluído, encerrando sistema de exclusão.')
                    return
                elif verificador and verificador[0] == 'N':
                    print('Exclusão cancelada, encerrando sistema de exclusão.')
                    return
                else:
                    print('Opção inválida, tente novamente')
        else:
            print("Usuário não encontrado, tente novamente")


def atualizar_cadastro():
    while True:
        listar_usuario()
        print('MENU DE ATUALIZAÇÕES DE USUÁRIO\n1 - ATUALIZAR TUDO\n 2 - ATUALIZAR NOME\n 3 - ATUALIZAR EMAIL\n4 - ATUALIZAR STATUS\n5 - SAIR')
        opcao = ler_int('Opção: ')
        match opcao:
            case 1:
                novo_nome = input("Novo nome: ")
                novo_email = input("Novo email: ")
                id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                if validar_usuario(usuario):
                    usuario.nome = novo_nome
                    usuario.email = novo_email
                    status = validar_sn("Deseja alterar o status? [S/N]: ")
                    if status:
                        usuario.ativo = not usuario.ativo
                        print(f'Nome, Email e Status do usuário {usuario.id} alterados com sucesso.')
                    else:
                        print(f'Nome e Email do usuário {usuario.id} alterados com sucesso.')
                    session.commit()
                else:
                    print("Usuário não encontrado.")
            case 2:
                novo_nome = input("Novo nome: ")
                id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                if validar_usuario(usuario):
                    usuario.nome = novo_nome
                    session.commit()
                    print(f'Nome do usuário {usuario.id} alterado com sucesso.')
                else:
                    print('Usuário não encontrado.')
            case 3:
                novo_email = input("Novo email: ")
                id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                if validar_usuario(usuario):
                    usuario.email = novo_email
                    session.commit()
                    print(f'Email do usuário {usuario.id} alterado com sucesso.')
                else:
                    print("Usuário não encontrado.")
            case 4:
                id_atualizar = ler_int("Qual o ID do usuário que deseja atualizar: ")
                usuario = session.query(Usuario).filter_by(id=id_atualizar).first()
                if validar_usuario(usuario):
                    usuario.ativo = not usuario.ativo
                    session.commit()
                    print(f'Status do usuário {usuario.id} alterado com sucesso.')
                else:
                    print("Usuário não encontrado.")
            case 5:
                print("Encerrando programa de atualização.")
                break
            case _:
                print("Opção inválida, tente novamente.")

