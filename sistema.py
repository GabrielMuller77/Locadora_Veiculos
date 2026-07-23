import classes
import funcoes
def cadastrar(lista_veiculos):
   while True:
      tipo = int(input('Qual tipo de veículo deseja cadastrar: \n 1 - Carro\n 2 - Moto\n 3 - Caminhão\n 4 - Sair'))
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
        
      