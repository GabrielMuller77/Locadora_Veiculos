import validacoes
def info_veiculos():
    placa = validacoes.validar_placa_duplicada('Placa do veículo: ')
    modelo = input('Modelo do veículo: ')
    valor_diaria = validacoes.validar_int('Valor da diária: ')
    disponivel = True
    return placa, modelo, valor_diaria, disponivel


def buscar_disponiveis(lista_veiculos):
    for veiculo in lista_veiculos:
        if veiculo.disponivel == True:
            print(f"Placa: {veiculo.placa}\nModelo: {veiculo.modelo}\nValor Diário: {veiculo.valor_diaria}\nStatus: {'Disponível' if veiculo.disponivel else 'Indisponível'}")
            print()
            print('-=' * 12)
            print()



def buscar_indisponiveis(lista_veiculos):
    for veiculo in lista_veiculos:
        if veiculo.disponivel == False:
            print(f"Placa: {veiculo.placa}\nModelo: {veiculo.modelo}\nValor Diário: {veiculo.valor_diaria}\nStatus: {'Disponível' if veiculo.disponivel else 'Indisponível'}")
            print()
            print('-=' * 12)
            print()