from flask import *
from repository.livrosRepository import*

livrinhosController = Blueprint('livrinhos', __name__)
repository = LivrosRepository()


@livrinhosController.route('/books')
def livros():
    return render_template("livrinhos.html")


@livrinhosController.route('/get-all-livros', methods=['GET', 'POST'])
def get_all_livros():
    all_livros = None
    if request.method == 'POST':
        all_livros = repository.get_all_livros()
    return render_template('livrinhos.html', all_livros=all_livros)


@livrinhosController.route('/criarlivro', methods=['GET', 'POST'])
def criar_livro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        isbn = request.form.get('isbn')
        num_pag = request.form.get('num_pag')
        autor_id = request.form.get('autor_id')
        genero_id = request.form.get('genero_id')
        livro = repository.criar_livros(titulo, isbn, num_pag, autor_id, genero_id)
        flash('Livro criado com sucesso!')
        return redirect(url_for('livrinhos.get_all_livros'))
    
    return render_template('criar.html')


@livrinhosController.route('/editar_livro/<int:id>', methods=['GET', 'POST'])
def editar_livro(id):
    livro = repository.get_livro(id)
    
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        isbn = request.form.get('isbn')
        num_pag = request.form.get('num_pag')
        autor_id = request.form.get('autor_id')
        genero_id = request.form.get('genero_id')
        repository.atualizar_Livros(id, titulo, isbn, num_pag, autor_id, genero_id)
        flash('livro atualizado')
        return redirect(url_for('livrinhos.get_all_livros'))
    
    return render_template('editar.html', livro=livro)


@livrinhosController.route('/excluir_livro/<int:id>', methods=['POST'])
def excluir_livro(id):
    repository.deletar_Livros(id)
    flash('livro excluído')
    return redirect(url_for('livrinhos.get_all_livros'))
