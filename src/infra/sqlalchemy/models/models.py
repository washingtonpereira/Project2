from sqlalchemy import Column, Float, column , Integer, String,Float ,Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto():
    __tablename__ = 'Produto'
    id = Column(Integer,primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
