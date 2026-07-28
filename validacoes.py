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

#Adicionar verificação de placa vazia
def validar_placa_duplicada(msg, lista_veiculos):
    while True:
        placa_escolhida = input(msg)
        duplicada = False
        for veiculos in lista_veiculos:
            if veiculos.placa == placa_escolhida:
               duplicada = True
        if duplicada:
            print('Placa duplicada')
        else:
            print('Placa aprovada')
            return placa_escolhida