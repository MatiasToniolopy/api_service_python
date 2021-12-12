
from flask import Flask, jsonify, request, render_template
from models import db, Persona
import traceback
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///personas.db"
db.init_app(app)



#ruta principal para agregar por formulario
@app.route('/')

def home():
    return render_template ("index.html")

#ruta principal para eliminar por formulario   
@app.route('/eliminar', methods=['GET'])

def formul():
    return render_template('eliminar.html')


#ruta principal para busqueda por formulario
@app.route('/buscarpersona', methods=['GET'])

def buscarpersona():
    return render_template("buscarpersona.html")


#objetos personas mostrado como json
@app.route('/personas', methods=['GET'])

def visualisar():
    try:
        person = Persona.query.all()
        retorno = [x.convert() for x in person]
        return jsonify (retorno)
        
    except: 
        return jsonify({'trace': traceback.format_exc()})
    
    
#buscar una persona desde la url
@app.route('/personas/nombre', methods=['GET'])

def buscar():
    try:
        dicc = {}
        if "nombre" in request.args:
            dicc["nombre"] = request.args["nombre"]
        if "edad" in request.args:
            dicc["edad"] = request.args["edad"]
        if "r_c" in request.args:
            dicc["r_c"] = request.args["r_c"]
            
        persona = Persona.query.filter_by(**dicc).first()
        if not persona:
            return jsonify({"mensaje": "la persona no existe"})
        else:
            return jsonify (persona.convert())      
    except:
        return({'trace': traceback.format_exc()})
    
    
#agregar una persona por formulario input    
@app.route('/personas/agregar', methods=['POST'])

def agregar():
    try:
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        r_c = request.form["r_c"]
        
        nueva_persona = Persona(nombre, int(edad), int(r_c))
        db.session.add(nueva_persona)
        db.session.commit()
        
        return jsonify(nueva_persona.convert())
    
    except Exception:
        exception("\n[SERVER]: error en la ruta /personas/agregar. Log: \n")
        return jsonify({'mensaje': 'algo salio mal'})
    

#buscar una persona por formulario input
@app.route('/personas/buscarpersona', methods=['POST'])

def buscarform():
    try:
        nombre_pers = request.form["nombre"]
        persona = Persona.query.filter(Persona.nombre.like(f"%{nombre_pers}%")).first()
        if not persona:
            return jsonify({'mensaje': 'esta persona no esta en la base de datos'})
        else:
            return jsonify(persona.convert())
        
    except:
        return jsonify({'trace': traceback.format_exc()})
    
    

#ruta para eliminar a una persona por formulario
@app.route('/personas/eliminar', methods=['POST'])

def eliminar():
    nom = request.form["nombre"]
    per = Persona.query.filter_by(nombre=nom).first()
    if not per:
        return jsonify({'mensaje': 'esta persona no esta en la base de datos'})
    else:
        db.session.delete(per)
        db.session.commit()
        return jsonify ({'mensaje': 'persona eliminada'})
    



    
    

if __name__ == '__main__':
    
    app.run(debug=True, port=4000)