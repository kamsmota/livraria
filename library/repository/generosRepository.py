from dao.generosDao import GenerosDAO

class GenerosRepository:
    def __init__(self) -> None:
        self.generosDao = GenerosDAO()

    def get_generos(self, id):
        return self.generosDao.get_generos(id)

    def get_all_generos(self):
        return self.generosDao.get_all_generos()

    def criar_generos(self, tipo):
        return self.generosDao.add_categoria(tipo)

    def atualizar_generos(self, id,tipo):
        return self.generosDao.att_categoria(id,tipo)

    def deletar_generos(self, id):
        return self.generosDao.del_categoria(id)