from database import Base
from sqlalchemy import Integer, String, Boolean, ForeignKey, Column

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean, default=True)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    modelo = Column("modelo", String)
    placa = Column("placa", String, unique=True, nullable=False)
    valor_diario = Column("valor_diario", Integer, nullable=False)
    status = Column("status", Boolean, default=True)
    locatario = Column("locatario", Integer, ForeignKey("usuarios.id"))

    def __init__(self, modelo, placa, valor_diario, status=True):
        self.modelo = modelo
        self.placa = placa
        self.valor_diario = valor_diario
        self.status = status