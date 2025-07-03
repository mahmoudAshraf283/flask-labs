from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import routes, models
