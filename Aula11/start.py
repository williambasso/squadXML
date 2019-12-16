#---- API
from flask import Flask
from flask_restful import Api 
from controller.squad_controller import SquadController

app = Flask(__name__)
api =  Api(app)

api.add_resource(SquadController, '/api/squads', endpoint='squads')
api.add_resource(SquadController, '/api/squads/<int:id>', endpoint='squad')

app.run(debug=True)