from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.autor import*
from dao.autorDao import*
from repository.autorRepository import AutorRepository

autoresController = Blueprint('autores', __name__)
repository = AutorRepository()

# Rota para buscar autor por ID
@autoresController.route('/get-autores', methods=['GET', 'POST'])
def autor_porid():
    if request.method == 'POST':
        id = request.form.get('id')
        autor = repository.get_autor(id)
        if autor:
            flash(f'Autor encontrado: {autor.nome}')
        else:
            flash('Autor não encontrado. Tente novamente!')
    return render_template('autores.html')

# Rota para listar todos os autores
@autoresController.route('/get-all-autores', methods=['GET', 'POST'])
def get_all_autores():
    all_autores = None
    if request.method == 'POST':
        all_autores = repository.get_all_autor()
    return render_template('autores.html', all_autores=all_autores)

# Rota para criar um novo autor
@autoresController.route('/criar-autor', methods=['GET', 'POST'])
def criar_autor():
    autor = None
    if request.method == 'POST':
        nome = request.form.get('nome')
        data_nasci = request.form.get('data_nasci')
        nacionalidade = request.form.get('nacionalidade')
        autor = repository.criar_autor(nome, data_nasci, nacionalidade)
    return render_template('autores.html', autor=autor)

# Rota para editar autor
@autoresController.route('/editar_autor/<int:id>', methods=['POST'])
def editar_autor(id):
    nome = request.form.get('nome')
    data_nasci = request.form.get('data_nasci')
    nacionalidade = request.form.get('nacionalidade')
    repository.atualizar_autor(id, nome, data_nasci, nacionalidade)
    flash('Autor atualizado com sucesso!')
    return redirect(url_for('autores.get_all_autores'))

# Rota para excluir autor
@autoresController.route('/excluir_autor/<int:id>', methods=['POST'])
def excluir_autor(id):
    repository.deletar_autor(id)
    flash('Autor excluído com sucesso!')
    return redirect(url_for('autores.get_all_autores'))
