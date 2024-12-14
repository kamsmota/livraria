from dao.livrosDao import*

class LivrosRepository:
    def __init__(self) -> None:
        self.livrosDao = LivrosDAO()

    def get_livro(self, id):
        return self.livrosDao.get_livros(id)

    def get_all_livros(self):
        return self.livrosDao.get_all_livros()

    def criar_livros(self, titulo, isbn, num_pag, autor_id, genero_id):
        return self.livrosDao.add_livro(titulo, isbn, num_pag, autor_id, genero_id)

    def atualizar_Livros(self, id, titulo, isbn, num_pag, autor_id, genero_id):
        return self.livrosDao.att_livro(id, titulo, isbn, num_pag, autor_id, genero_id)

    def deletar_Livros(self, id):
        return self.livrosDao.del_livro(id)
