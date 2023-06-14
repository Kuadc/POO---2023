from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


import hashlib

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db

from models import Preceptor,Asistencia,padre,Estudiante,Curso

@app.route('/' , methods = ['GET','POST'])
def inicio():
    if request.method == 'POST':
        if not request.form['email'] or not request.form['password']:
            return render_template('error.html', error="Por favor ingrese los datos requeridos")
        else:
            usuario_actual = Preceptor.query.filter_by(correo=request.form['email']).first()
            if usuario_actual is None:

                return render_template('error2.html', error="El usuario no está registrado")
            else:
                print("por aqui")
                clave = usuario_actual.clave
                print(clave)
                verificacion = request.form['password']
                print(verificacion)
                result = hashlib.md5(bytes(verificacion, encoding='utf-8'))
                if result.hexdigest() == clave:
                    return render_template('eleccioncurso.html', usuario=usuario_actual)
                else:
                    return render_template('error.html', error="La contraseña no es válida")
    else:
        return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tablas creadas correctamente")
        usuarios = Preceptor.query.all()
        for usuario in usuarios:
            print(f"ID: {usuario.id}, Username: {usuario.nombre}, Password: {usuario.correo}, clave: {usuario.clave}")


