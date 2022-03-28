from turtle import title
from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
app = FastAPI(
    title= "Api para BDD con Mongo",
    description = "Esta api es para un practica de la materia de BDD",
    version = "1.5",
    openapi_tags = tags_metadata
)

@app.get('/')
def get_raiz():
    return {"Hola aquí no hay nada, dirigete a /docs"}

app.include_router(user)

