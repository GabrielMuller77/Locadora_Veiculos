def validar_int(msg):
    while True:
        valor = input(msg) 
        try:
            valor_int = int(valor)
            if valor_int > 0:
                return valor_int
            else:
                print('Valor recusado')
                continue
        except ValueError:
            print('Valor inválido')

def validar_placa(msg, lista_veiculos):
    while True:
        placa_escolhida = input(msg)
        duplicada = False
        if len(placa_escolhida) < 6:
            print('A placa deve conter no mínimo 6 caracteres, tente novamente.')
            continue
        else:
            for veiculos in lista_veiculos:
                if veiculos.placa == placa_escolhida:
                    duplicada = True
            if duplicada:
                print('Placa duplicada, tente novamente.')
                continue
            else:
                print('Placa aprovada')
                return placa_escolhida  