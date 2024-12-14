from models.livros import Livros, db

class LivrosDAO:
    @staticmethod
    def get_livros(id):
        return Livros.query.get(id)

    @staticmethod
    def get_all_livros():
        return Livros.query.all()

    @staticmethod
    def add_livro(titulo, isbn, num_pag, autor_id, genero_id):
        livro = Livros(titulo=titulo, isbn=isbn, num_pag=num_pag, autor_id=autor_id, genero_id=genero_id)
        db.session.add(livro)
        db.session.commit()
        return livro

    @staticmethod
    def att_livro(id, titulo, isbn, num_pag, autor_id, genero_id):
        livro = LivrosDAO.get_livros(id)
        if livro:
            livro.titulo = titulo
            livro.isbn = isbn
            livro.num_pag = num_pag 
            livro.autor_id = autor_id
            livro.genero_id = genero_id
            db.session.commit()
        return livro

    @staticmethod
    def del_livro(id):
        livro = LivrosDAO.get_livros(id)
        if livro:
            db.session.delete(livro)
            db.session.commit()
        return livro
