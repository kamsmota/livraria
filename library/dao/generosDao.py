from models.generos import*

class GenerosDAO:
    @staticmethod
    def get_generos(id):
        return Generos.query.get(id)

    @staticmethod
    def get_all_generos():
        return Generos.query.all()

    @staticmethod
    def add_categoria(tipo):
        categ = Generos(tipo=tipo)
        db.session.add(categ)
        db.session.commit()
        return categ

    @staticmethod
    def att_categoria(id, tipo):
        categ = GenerosDAO.get_generos(id)
        if categ:
            categ.id = id
            categ.tipo = tipo
            db.session.commit()
        return categ

    @staticmethod
    def del_categoria(id):
        categ = GenerosDAO.get_generos(id)
        if categ:
            db.session.delete(categ)
            db.session.commit()
        return categ