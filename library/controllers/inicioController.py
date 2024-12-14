from flask import *

inicioController = Blueprint('index', __name__)

@inicioController.route('/')
def index():
    return render_template ('index.html')

@inicioController.route('/books')
def books():
    return render_template('livrinhos.html')

@inicioController.route('/autores')
def authors():
    return render_template('autores.html')

@inicioController.route('/categorias')
def categorias():
    return render_template('categorias.html')
