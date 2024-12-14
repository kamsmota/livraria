from models.autor import db, Autores

class AutorDAO:
    @staticmethod
    def get_autor(id):
        return Autores.query.get(id)

    @staticmethod
    def get_all_autor():
        return Autores.query.all()

    @staticmethod
    def add_autor(nome, data_nasci, nacionalidade):
        autor = Autores(nome=nome, data_nasci=data_nasci, nacionalidade=nacionalidade)
        db.session.add(autor)
        db.session.commit()
        return autor

    @staticmethod
    def att_autor(id, nome, data_nasci, nacionalidade):
        autor = AutorDAO.get_autor(id)
        if autor:
            autor.nome = nome
            autor.data_nasci = data_nasci
            autor.nacionalidade = nacionalidade
            db.session.commit()
        return autor

    @staticmethod
    def del_autor(id):
        autor = AutorDAO.get_autor(id)
        if autor:
            db.session.delete(autor)
            db.session.commit()
        return autor
