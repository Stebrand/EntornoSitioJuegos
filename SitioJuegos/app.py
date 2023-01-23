import os
from flask import Flask
from flask import render_template, request, redirect, session, send_file
from flask import send_from_directory
from datetime import datetime
from config import ConfigBase

app=Flask(__name__)
app.secret_key="juegosSteven"
app.config["SQLALCHEMY_DATABASE_URL"]="sqlite:\\\config//BaseJuegos.db"

#CONEXION

#PAGINA CLIENTE

@app.route('/')
def inicio():
    img=['static/imgs/intro.jpg','static/imgs/intro2.jpg']
    return render_template('cliente/index.html',img=img)

@app.route('/juegos')
def juegos():
    juegos=ConfigBase.ReadRegistroJuegos()
    return render_template('cliente/juegos.html',juegos=juegos)

@app.route('/nosotros')
def nosotros():
    img='static/imgs/nosotros.jpg'
    return render_template('cliente/nosotros.html',img=img) 

@app.route('/descarga/<torrent>')  
def descarga(torrent):
    return send_file('templates/torrents/'+ torrent, as_attachment=True)
    
@app.route('/imgames/<imagen>')
def imgames(imagen):
    return send_from_directory(os.path.join('templates/imgames/'),imagen)

##PAGINA DEL ADMINISTRADOR

@app.route('/admin')
def adminIndex():
    img='static/imgs/admin.jpg'
    return render_template('admin/index.html',img=img)

@app.route('/admin/login')
def login():
    return render_template('admin/login.html')

@app.route('/admin/login',methods=['POST'])
def admin_login():
    _usuario= (request.form['usuario'])
    _contrasena= (request.form['contrasena'])

    usuario=ConfigBase.ReadRegistroUsuarios(_usuario)
    print(usuario)
    if not usuario:
        return render_template('admin/login.html', mensaje="El Usuario es incorrecto o por favor diligencie el campo")
    else:
        if _usuario==str(usuario[0][0]) and _contrasena==str(usuario[0][1]):
            session["login"]=True
            return redirect("/admin")
        else:
            return render_template('admin/login.html', mensaje="Contraseña incorrectos")

@app.route('/admin/cerrar')
def admin_cerrar():
    session.clear()
    return redirect('/admin/login')

@app.route('/admin/juegos')
def adminjuegos():
    juegos=ConfigBase.ReadRegistroJuegos()
    return render_template('admin/juegos.html',juegos=juegos)

@app.route('/admin/juegos/guardar', methods=['POST'])
def adminjuegosguardar():
    _name =(request.form['name'])
    _imagen= (request.files['imagen'])
    _torrent= (request.files['torrent'])
    _time= datetime.now()
    horaActual = _time.strftime('%Y%H%M%S')
    if _imagen.filename!="":
        _newname=horaActual+"_"+_imagen.filename
        _imagen.save("templates/imgames/"+_newname)
    if _torrent.filename!="":
        _newnametorrent=horaActual+"_"+_torrent.filename
        _torrent.save("templates/torrents/"+_newnametorrent)        
    dato=(_name,_newname,_newnametorrent)
    ConfigBase.CreateRegistro(dato)
    return redirect('/admin/juegos')

@app.route('/admin/juegos/borrar', methods=['POST'])
def adminjuegosborrar():
    _id =(request.form['txtID'])
    dato=ConfigBase.DeleteRegistro(_id)
    if os.path.exists("templates/imgames/"+str(dato[0][0])):
        os.unlink("templates/imgames/"+str(dato[0][0]))  
    if os.path.exists("templates/torrents/"+str(dato[0][1])):
        os.unlink("templates/torrents/"+str(dato[0][1]))  
    return redirect('/admin/juegos') 

if __name__ == '__main__':
    app.run(debug=True)