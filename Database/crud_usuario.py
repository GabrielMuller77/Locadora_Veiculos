from database import session
from modelos import Usuario
from validar_database import validar_usuario

def criar_usuario(usuario):
    session.add(usuario)
    session.commit()


def consultar_usuario():
    while True:
        print("MENU DE CONSULTA\n1 - BUSCAR TODOS\n2 - BUSCAR PELO ID\n3 - BUSCAR PELO EMAIL\n4- BUSCAR COLUNAS\n5 - SAIR")
        escolha = int(input("Opção: "))
        match escolha:
            case 1:
                usuarios = session.query(Usuario).all()
                listar_usuario()
            case 2:
                while True:
                    id_usuario = int(input("ID: "))
                    usuario = session.query(Usuario).filter_by(id=id_usuario).first()
                    if validar_usuario(usuario):
                        listar_um(usuario)
                        break
                    else:
                        while True:
                            escolha = input('Tentar novamente, [S/N]? ').upper().strip()
                            if escolha[0] == 'S':
                                break
                            elif escolha[0] == 'N':
                                print('Encerrando consulta de usuarios.')
                                return
                            else:
                                print('Opção inválida, tente novamente.')
                                

               
            case 3:
                email_usuario = input("Email: ")
                usuarios = session.query(Usuario).filter_by(email=email_usuario).first()
                listar_um(usuarios)
            case 4:
                print("COLUNAS\n1 - ID\n2 - NOME\n3 - EMAIL\n4 - ATIVO")
                opcao = int(input("Qual coluna deseja filtrar: "))
                usuarios = session.query(Usuario).all()
                match opcao:
                    case 1:
                        for usuario in usuarios:
                            print(usuario.id)
                    case 2:
                        for usuario in usuarios:
                            print(usuario.nome)
                    case 3:
                        for usuario in usuarios:
                            print(usuario.email)
                    case 4:
                        for usuario in usuarios:
                            if usuario.ativo:
                                print("Ativo")
                            else:
                                print("Inativo")
            case 5:
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
    listar_usuario()
    id_exclusao = input('Informe o ID do usuário que deseja excluir: ')
    usuarios = session.query(Usuario).filter_by(id=id_exclusao).first()
    while True:
        verificador = input(f'Tem certeza que deseja excluir o usuario {id_exclusao}, [S/N]: ').upper().strip()
        if verificador[0] == 'S':
            if usuarios.id:
                session.delete(usuarios)
                session.commit()
                print('Usuário excluído, encerradno sistema de exclusão.')
                break
            else:
                print('Usuário não encontrado.\nEncerrando o sistema de exclusão.')
                break

        elif verificador[0] == 'N':
            print('Exclusão cancelada, encerrando sistema de exclusão.')
            break
        else:
            print('Opção inválida, tente novamente')
