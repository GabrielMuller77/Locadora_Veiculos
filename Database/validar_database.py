from crud_usuario import Usuario

def validar_usuario(usuario):
    if usuario is None:
        print('Usuário não encontrado.')
    return usuario