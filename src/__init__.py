
from flask import Flask
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:R00t*quantum@0.0.0.0/quantumknn_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jshwifhjwieoajhf5847f5ae4eaws"
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
db = SQLAlchemy(app)
ckeditor = CKEditor(app)
login_manager = LoginManager(app)
login_manager.login_view = "loginPage"
login_manager.login_message_category = "info"

from src.source.model import models

# Create database if it does not exist
if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    create_database(app.config["SQLALCHEMY_DATABASE_URI"])
    with app.app_context():
        db.create_all()
else:
    with app.app_context():
        db.create_all()


from src.source.classificazioneDataset import ClassifyControl
from src.source.preprocessingDataset import PreprocessingControl
from src.source.validazioneDataset import ValidazioneControl
from src.source.gestione import GestioneControl
from src.source.utente import UtenteControl
from src import routes
