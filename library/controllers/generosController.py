from flask import *
from models.generos import *
from dao.generosDao import*
from repository.generosRepository import*

generosController = Blueprint('generos', __name__)
repository = GenerosRepository()

@generosController.route('/get-generos', methods=['GET', 'POST'])
def genero_porid():
    if request.method == 'POST':
        id = request.form.get('id')
        genero = repository.get_generos(id)  # procura o genero pelo id
        if genero:
            flash(f'gênero encontrado: id: {genero.id}, gênero: {genero.tipo}')
        else:
            flash('desculpe, não encontramos nenhum gênero com esse id... mas você pode cadastrar um novo abaixo, se quiser!')
    return render_template('categorias.html')

@generosController.route('/get-all-generos', methods=['GET', 'POST'])
def get_all_generos():
    all_generos = None
    if request.method == 'POST':
        all_generos = repository.get_all_generos()
    return render_template('categorias.html', all_generos=all_generos)

@generosController.route('/criar-genero', methods=['GET', 'POST'])
def criar_genero():
    gener = None
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        gener = repository.criar_generos(tipo)
    return render_template('categorias.html', gener=gener)

@generosController.route('/editar_categoria/<int:id>', methods=['POST'])
def editar_categoria(id):
    gener = request.form.get('gener')
    repository.atualizar_generos(id, gener)
    flash('gênero literário atualizado com sucesso!')
    return redirect(url_for('generos.get_all_generos'))

@generosController.route('/excluir_categoria/<int:id>', methods=['POST'])
def excluir_categoria(id):
    repository.deletar_generos(id)
    flash('gênero literário excluído com sucesso!')
    return redirect(url_for('generos.get_all_generos'))
