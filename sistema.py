import classes
import funcoes
import menu
import validacoes
def cadastrar(lista_veiculos):
   while True:
      tipo = validacoes.validar_int('Qual tipo de veículo deseja cadastrar: \n 1 - Carro\n 2 - Moto\n 3 - Caminhão\n 4 - Sair\n Opção: ')
      match tipo:
         case 1:
            placa, modelo, valor_diaria, disponivel = funcoes.info_veiculos()
            carro1 = classes.Carro(placa, modelo, valor_diaria, disponivel)
            lista_veiculos.append(carro1)
         case 2:
            placa, modelo, valor_diaria, disponivel = funcoes.info_veiculos()
            moto1 = classes.Moto(placa, modelo, valor_diaria, disponivel)
            lista_veiculos.append(moto1)
         case 3:
            placa, modelo, valor_diaria, disponivel = funcoes.info_veiculos()
            caminhao1 = classes.Caminhao(placa, modelo, valor_diaria, disponivel)
            lista_veiculos.append(caminhao1)
         case 4:
            print('Saindo de cadastros')
            break
         case _:
            print('Tipo inválido, tente novamente')
        


def buscar(lista_veiculos):
   placa_buscada = input('Qual a placa do veículo desejado: ')
   for veiculo in lista_veiculos:
      if veiculo.placa == placa_buscada:
        lista_um(veiculo)
        return veiculo

def lista_um(veiculo):
   print(f"Placa: {veiculo.placa}\nModelo: {veiculo.modelo}\nValor Diário: {veiculo.valor_diaria}\nStatus: {'Disponível' if veiculo.disponivel else 'Indisponível'}")
   print()
   print('-=' * 12)
   print()

def listar(lista_veiculos):
   for veiculo in lista_veiculos:
     lista_um(veiculo)


def atualizar(lista_veiculos):
   while True:
      veiculo = buscar(lista_veiculos)
      opcao = menu.menu_atualizar()
      match opcao:
         case '1':
            nova_placa = validacoes.validar_placa('Nova placa: ')
            veiculo.placa = nova_placa
         case '2':
            novo_modelo = input('Novo modelo: ')
            veiculo.modelo = novo_modelo
         case '3':
            novo_valor = validacoes.validar_int('Novo valor diário: ')
            veiculo.valor_diario = novo_valor
         case '4':
            print('Saindo do menu de atualizações...')
            break
         case _:
            print('Opção inválida, tente novamente')


def excluir(lista_veiculos):
   veiculo = buscar(lista_veiculos)
   lista_veiculos.pop(veiculo)



def alugar(lista_veiculos):
   funcoes.buscar_disponiveis(lista_veiculos)
   veiculo = buscar(lista_veiculos)
   if veiculo is None:
      print('Veículo não encontrado.')
   elif veiculo.disponivel is False:
      print('Veículo indisponível, já alugado.')
   else:
      dias = validacoes.validar_int('Por quantos dias deseja alugar o veículo: ')
      aluguel = veiculo.alugar(dias)
      return aluguel


def devolver(lista_veiculos):
   funcoes.buscar_indisponiveis(lista_veiculos)
   veiculo = buscar(lista_veiculos)
   if veiculo is None:
      print('Veículo não encontrado')
   elif veiculo.disponivel is True:
      print('Veículo já disponível')
   else:
      veiculo.devolver()
      print('Veículo devolvido com sucesso.')
