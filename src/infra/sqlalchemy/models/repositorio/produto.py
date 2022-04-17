from sqlalchemy.orm import Session
from src .shemas import shemas
from  src.infra.sqlalchemy.models import models

class RepositorioProduto():
 
    def __init__(self, db : Session):
        self.db = db

    def criar(self, produto: shemas.Produto):
            db_produto = models.Produto(nome=produto.nome,
                                        detalhes=produto.detalhes,
                                        preco=produto.preco,
                                        disponivel=produto.disponivel)

                self.db.add(db_produto)
                self.db.commit()
                self.db.refrsh(db_produto)
                return db_produto


    def listar(self):
            shemas.Produto = self.db.query(models.Produto).all()
    
    def obter(self):
            pass

    def remover(self):
            pass
        