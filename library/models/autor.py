from database import db

class Autores(db.Model):
        __tablename__ = 'authors'

        id = db.Column(db.Integer, primary_key = True)
        nome = db.Column(db.String(120), nullable=False)
        data_nasci = db.Column(db.Date, nullable = False) #sem nullable porque nem sempre se tem a data
        nacionalidade = db.Column(db.String(80)) # mesmo caso acima

        def __repr__(self):
                return f'{self.id}, {self.nome}'
        
        def toJson(self):
                return {'id': self.id, 
                        'nome': self.nome, 
                        'data de nascimento': self.data_nasci,
                        'nacionalidade': self.nacionalidade}
        