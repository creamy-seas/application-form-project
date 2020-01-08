from send_mail import SendEmail
from flask_cors import CORS
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(SendEmail, '/send_mail')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)