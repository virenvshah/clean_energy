from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)