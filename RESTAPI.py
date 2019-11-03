from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

        

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        string = request.form.to_dict()
        for k in string:
            print(k)
        return request.query_string



api.add_resource(Employees, '/employees') # Route_1


if __name__ == '__main__':
     app.run(port='5002')
