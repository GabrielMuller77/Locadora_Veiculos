from abc import ABC, abstractmethod

class Veículo(ABC):

    def __init__(self, placa, modelo, dias, valor_diaria=100, disponivel=True):
        self.placa = placa
        self.modelo = modelo
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel
        self.dias = dias

    def alugar(self):
        self.disponivel = False
        return self.disponivel

    def devolver(self):
        self.disponivel = True
        return self.disponivel


    @abstractmethod
    def valor_total(self):
        pass


class Carro(Veículo):

    def __init__(self, placa, modelo, dias, valor_diaria, disponivel):
        super().__init__(placa, modelo, dias, valor_diaria, disponivel)

    def valor_total(self):
        total = self.valor_diaria * self.dias
        return total


class Moto(Veículo):

    def __init__(self, placa, modelo, dias, valor_diaria, disponivel):
        super().__init__(placa, modelo, dias, valor_diaria, disponivel)

    def valor_total(self):
       total = self.valor_diaria * self.dias
       if self.dias >= 7:
           total = total - total * 0.10
       return total

class Caminhao(Veículo):

    def __init__(self, placa, modelo, dias, valor_diaria, disponivel):
        super().__init__(placa, modelo, dias, valor_diaria, disponivel)

    def valor_total(self):
        total = self.valor_diaria * self.dias
        for dias in range(dias):
            total += 50
        return total