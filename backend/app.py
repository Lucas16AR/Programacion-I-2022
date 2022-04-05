
#Instalar python3-venv para el manejo de entornos virtuales

#Importar librería os
import os

#Importar Flask
#from flask import Flask

#Importar DotEnv para manejo de variables de entorno
#from dotenv import load_dotenv

#Importar funcion que crear app
from main import create_app

#Cargar variables de entorno de archivo .env
#load_dotenv()

#Llamar a la funcion y devolver la app
app = create_app()

app.app_context().push()

#Inicializar aplicación Flask
#app = Flask(__name__)

#Verificar que el script se este ejecutando directamente
if __name__ == '__main__':
    #Correr servidor web
    #Debug: Si está activado muestra mensajes de error y se reinicia al encontrar cambios
    #Port: Puerto en el que va a correr el servicio. Obtenido de las variables de entorno
    app.run(debug = True, port = (os.getenv("PORT")))

#Listo, ya esta listo