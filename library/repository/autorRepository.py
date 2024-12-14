from dao.autorDao import AutorDAO

class AutorRepository:
    def __init__(self) -> None:
        self.autorDao = AutorDAO()

    def get_autor(self, id):
        return self.autorDao.get_autor(id)

    def get_all_autor(self):
        return self.autorDao.get_all_autor()

    def criar_autor(self, nome, data_nasci, nacionalidade):
        return self.autorDao.add_autor(nome, data_nasci, nacionalidade)

    def atualizar_autor(self, id, nome, data_nasci, nacionalidade):
        return self.autorDao.att_autor(id, nome, data_nasci, nacionalidade)

    def deletar_autor(self, id):
        return self.autorDao.del_autor(id)
