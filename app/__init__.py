from config import Config
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config.from_object(Config)
db = SQLAlchemy(app)