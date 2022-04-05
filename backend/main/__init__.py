import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

api = Api()

#Metodo que iniciara todos los modulos y devolvera la aplicacion
def create_app():
    app = Flask(__name__)
    load_dotenv()
    
    api.add_resource(resources.PoemasResource, '/Poemas')
    api.add_resource(resources.PoemaResource, '/Poema/<id>')

    api.add_resource(resources.UsuariosResource, '/Usuarios')
    api.add_resource(resources.UsuarioResource, '/Usuario/<id>')

    api.add_resource(resources.CalificacionesResource, '/Calificaciones')
    api.add_resource(resources.CalificacionResource, '/Calificacion/<id>')

    api.init_app(app)

    return app