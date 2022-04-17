from pydantic import BaseModel
from typing import Optional, List



class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    minha_vendas: List[Pedido]
    meus_pedidos: List[Pedido]
    meus_produtos: List[Produto]    
    
class Produto(BaseModel):
    id: Optional[str] = None
    user: User
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False


class Pedido(BaseModel):
    id: Optional[str] = None
    user : User
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    obersevacoes: Optional[str] = "Sem observações"    

