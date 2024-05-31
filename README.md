# Pasos a seguir para crear una API

1.-Crear un ambiente virtual 

python3 -m venv [nombre del ambiente virtual]

2.-Ingresar al ambiente virtual

source nombre/bin/activate 

3.-Instalar fastapi

pip install fastapi

4.- Instalar uvicorn

pip install uvicorn

## Levantar el server

1.- asegurarnos que tenemos mínimo alguna función dentro de nuestro main.py

uvicorn main:[nameFunction] --reload 

# Virtud de fastApi

Cuando nosotros creamos una API con sus funciones, cada una de las funciones ya estará documentada por FastAPI
ingresando al link del server/docs
en el caso actual sería 

http://127.0.0.1:8000/docs
