from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    r_c = db.Column(db.Integer, nullable=False)
    
    
    def __init__(self, nombre, edad, r_c):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.r_c = r_c
    
    def __str__(self):
        return "\nnombre {} edad {} r_c {}.\n".format(self.nombre, self.edad, self.r_c)
    
    def convert(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "r_c": self.r_c
        }
    
    
    
    
    