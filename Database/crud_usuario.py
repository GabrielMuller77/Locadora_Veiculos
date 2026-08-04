from database import session
from modelos import Usuario

def criar_usuario(usuario):
    session.add(usuario)
    session.commit


def consultar_usuario(usuarios):
    while True:
        print("MENU DE CONSULTA\n1 - BUSCAR TODOS\n2 - BUSCAR O PRIMEIRO\n3 - BUSCAR PELO ID\n4 - BUSCAR PELO EMAIL\n5- BUSCAR VÁRIOS REGISTROS\n6 - SAIR")
        escolha = int(input("Opção: "))
        match escolha:
            case 1:
                usuarios = session.query(Usuario).all()
            case 2:
                usuarios = session.query(Usuario).first()
            case 3:
                id_usuario = int(input("ID: "))
                usuarios = session.query(Usuario).filter_by(id=id_usuario).first()
            case 4:
                email_usuario = input("Email: ")
                usuarios = session.query(Usuario).filter_by(email=email_usuario).first()
            case 5:
                print("COLUNAS\n1 - ID\n2 - NOME\n3 - EMAIL\n4 - ATIVO")
                opcao = int(input("Qual coluna deseja filtrar: "))
                usuarios = session.query(Usuario).all()
                match opcao:
                    case 1:
                        for usuario in usuarios:
                            print(usuario.id)
                    case 2:
                        for usuario in usuarios:
                            print(usuarios.nome)
                    case 3:
                        for usuario in usuarios:
                            print(usuario.email)
                    case 4:
                        for usuario in usuarios:
                            if usuario.ativo == True:
                                print("Ativo")
                            else:
                                print("Inativo")
            case 6:
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente")


def listar_usuario():
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}\nNOME: {usuario.nome}\nEMAIL: {usuario.email}\nSTATUS: {'Ativo' if usuario.ativo else 'Inativo'}\n")
        print('-='*20)
                


