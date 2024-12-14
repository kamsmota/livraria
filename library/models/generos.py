from database import db

class Generos(db.Model):
        __tablename__ = 'generos'

        id = db.Column(db.Integer, primary_key = True)
        tipo = db.Column(db.String(100), nullable=False)

        def __repr__(self):
                return f'{self.id}, {self.tipo}'
        
        def toJson(self):
                return {'id': self.id,  
                        'tipo': self.tipo}
        