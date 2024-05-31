
#1 importar fastApi
from fastapi import FastAPI
#4 importar pydantic para usarlo como validador
from pydantic import BaseModel
#6 Si queremos que alguno de los atributos de la clase sea opcional importamos typing
from typing import Optional

#5 se crea el modelo que queremos que tenga nuestra API como una clase
class Libro(BaseModel):
    titulo:str
    autor:str
    paginas:int
    editorial:Optional[str] #de esta forma definimos que va a ser opcional el dato editorial


#2 Usar FastAPI
app = FastAPI()

#http://127.0.0.1:8000/ (ruta)

#3 Crear la URI de raíz con un decorador para que cuando se haga un get a la raíz devuelva un "hola, mundo"
@app.get("/")
def index():
    return {
        "message":"Hola tonotos", #Fast api ya se encarga de convertirlo a JSON
    }

#Ya tenemos nuestra API creada
################################# 
#para crear más URIS se puede hacer con el principio de fstring "{}" con las llaves
@app.get('/libros/{id}')
def mostrar_libro(id:int): #Podemos modificar el argumento de la función para que sea un int 
    return {"data":id}

#6 creamos una función post que valla con base al modelo
@app.post('/libros')
def insertar_libro(libro:Libro):
    return {
        "message":f"libro {libro.titulo} insertado"
    }