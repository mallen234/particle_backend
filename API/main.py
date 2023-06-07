from flask import Flask, jsonify
from flask_restful import Resource, Api
import json
import subprocess


app = Flask("ParticleAPI")
api = Api(app)

class Video(Resource):

    def get(self):

        # subprocess.run(['python3', '../main.py'])

        with open('../data.json') as f:
            data = json.load(f)
        return jsonify(data)
    
    @app.route('/api/data', methods=['GET'])
    def get_json_data():

        subprocess.run(['python3', '../main.py'])


        with open('../data.json') as f:
            data = json.load(f)
        return jsonify(data)
    

api.add_resource(Video, '/')

if __name__ == '__main__':
    app.run()