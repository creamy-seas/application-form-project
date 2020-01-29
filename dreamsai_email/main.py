from send_mail import SendEmail
from flask_cors import CORS
from flask import Flask, render_template
from flask_restful import Resource, Api
import os

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

@app.route('/')
def index():
    return render_template("index.html")
api = Api(app)
CORS(app)

api.add_resource(SendEmail, '/send_mail')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
