from abc import ABC, abstractmethod

class Veículo(ABC):

    def __init__(self, placa, modelo, valor_diaria=100, disponivel=True):
        self.placa = placa
        self.modelo = modelo
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel

    def alugar(self, dias):
        valor_total = self.calcular_valor_total(dias)
        self.disponivel = False
        return valor_total

    def devolver(self):
        self.disponivel = True
        return self.disponivel


    @abstractmethod
    def calcular_valor_total(self):
        pass


class Carro(Veículo):

    def __init__(self, placa, modelo,valor_diaria, disponivel):
        super().__init__(placa, modelo, valor_diaria, disponivel)

    def calcular_valor_total(self, dias):
        total = self.valor_diaria * dias
        return total


class Moto(Veículo):

    def __init__(self, placa, modelo, valor_diaria, disponivel):
        super().__init__(placa, modelo, valor_diaria, disponivel)

    def calcular_valor_total(self, dias):
       total = self.valor_diaria * dias
       if self.dias >= 7:
           total = total - total * 0.10
       return total

class Caminhao(Veículo):

    def __init__(self, placa, modelo, valor_diaria, disponivel):
        super().__init__(placa, modelo, valor_diaria, disponivel)

    def calcular_valor_total(self, dias):
        total = self.valor_diaria * dias
        for d in range(dias):
            total += 50
        return total