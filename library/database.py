from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # config do banco de dados
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # desativa rastreamento
    db.init_app(app) 