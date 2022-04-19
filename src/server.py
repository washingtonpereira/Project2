from fastapi import FastAPI

app = FastAPI()


def listar_Produtos():
    return {"msg":"Listagem de produtos"}