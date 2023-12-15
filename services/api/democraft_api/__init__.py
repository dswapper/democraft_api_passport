from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('democraft_api.config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import passport_views, models
