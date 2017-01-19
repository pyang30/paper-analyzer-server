from flask import Flask
from config import config
from flask import request

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
from model import db
db.init_app(app)