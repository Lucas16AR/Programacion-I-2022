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
    
    api.add_resource(resources.PoemsResource, '/poems')
    api.add_resource(resources.PoemResource, '/poem/<id>')

    api.add_resource(resources.UsersResource, '/users')
    api.add_resource(resources.UserResource, '/user/<id>')

    api.add_resource(resources.MarksResource, '/marks')
    api.add_resource(resources.MarkResource, '/mark/<id>')

    api.init_app(app)

    return app