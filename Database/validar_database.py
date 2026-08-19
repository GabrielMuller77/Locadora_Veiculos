from utilidades import perguntar_novamente

def validar_usuario(usuario):
    if usuario is None:
        print('Usuário não encontrado.')
    return usuario

def validar_veiculo(veiculo):
    if veiculo is None:
        print("Veículo não encontrado.")
    return veiculo


def ler_int(msg):
    while True:
        valor = input(msg) 
        try:
            valor_int = int(valor)
            if valor_int >= 0:
                return valor_int
            else:
                print("Digite um número maior ou igual a 0.")
                continue
        except ValueError:
            print('Digite um número válido.')


def validar_placa(placa):
    while True:
        if len(placa) == 6:
            return placa
        else:
            if perguntar_novamente():
                continue
            else:
                print("Encerrando verificação de placa.")
                break