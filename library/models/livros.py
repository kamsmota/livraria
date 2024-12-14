from database import db

class Livros(db.Model):
        __tablename__ = 'books'

        id = db.Column(db.Integer, primary_key = True)
        titulo = db.Column(db.String(100), nullable=False)
        isbn = db.Column(db.Integer, nullable=False)
        data_publi = db.Column(db.Date, nullable = False)
        num_pag = db.Column(db.Integer, nullable = False)
        autor_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
        genero_id = db.Column(db.String(50), db.ForeignKey('generos.id'))

        def __repr__(self):
                return f'{self.titulo}, {self.isbn}'
        
        def toJson(self):
                return {'id': self.id, 
                        'titulo': self.titulo, 
                        'isbn': self.isbn, 
                        'data de publicação': self.data_publi,
                         'número de páginas':self.num_pag,
                         'id do autor': self.autor_id,
                         'id do genero': self.genero_id}
books = []