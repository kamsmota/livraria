from flask import Flask
from database import init_db, db  # importa a funcao e instancia do databse
from controllers.inicioController import inicioController
from controllers.livrosController import livrinhosController
from controllers.autorController import autoresController
from controllers.generosController import generosController

app = Flask(__name__)
app.secret_key='kamaleoesbicolores'

init_db(app)

app.register_blueprint(inicioController)
app.register_blueprint(livrinhosController)
app.register_blueprint(autoresController)
app.register_blueprint(generosController)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # cria as tabelas definidas nos models
    app.run(debug=True)