import sqlite3 as sql
import os

db_path = "/home/stebrand/Documentos/Lenguaje_Python/EntornoSitioJuegos/SitioJuegos/config/BaseJuegos.db"

def CrearBD():
    miConexion=sql.connect(db_path)
    miCursor=miConexion.cursor()
    miCursor.execute('''
        CREATE TABLE JUEGOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_JUEGO VARCHAR(50),
        NOMBRE_IMAGEN VARCHAR (200),
        NOMBRE_TORRENT VARCHAR (200))
    ''')
    miCursor.execute('''
        CREATE TABLE USUARIOS (
        USER VARCHAR (50),
        PASSWORD VARCHAR (50),
        ROLL VARCHAR (50))
    ''')
    miConexion.commit()
    miConexion.close()

def CreateRegistro(dato):
    miConexion=sql.connect(db_path)
    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO JUEGOS VALUES(NULL,?,?,?)",(dato))
    miConexion.commit()
    miConexion.close()

def ReadRegistroJuegos()    :
    miConexion=sql.connect(db_path)
    miCursor=miConexion.cursor() 
    miCursor.execute("SELECT * FROM 'JUEGOS'")  
    juegos=miCursor.fetchall()
    miConexion.commit()
    miConexion.close()     
    return juegos

def ReadRegistroUsuarios(dato)    :
    miConexion=sql.connect(db_path)
    miCursor=miConexion.cursor() 
    miCursor.execute("SELECT USER, PASSWORD FROM USUARIOS WHERE USER="+"'"+ dato +"'")  
    usuario=miCursor.fetchall()
    miConexion.commit()
    miConexion.close()     
    return usuario   

def UpdateRegistro(dato):
    miConexion=sql.connect(db_path)
    miCursor=miConexion.cursor()
    #miCursor.execute("UPDATE JUEGOS SET NOMBRE_JUEGO=?,NOMBRE_IMAGEN=? WHERE ID=)
    miConexion.commit()
    miConexion.close()

def DeleteRegistro(dato):
    miConexion=sql.connect(db_path)
    miCursor=miConexion.cursor()       
    miCursor.execute("SELECT NOMBRE_IMAGEN, NOMBRE_TORRENT FROM JUEGOS WHERE ID="+ dato) 
    juegos=miCursor.fetchall()
    miCursor.execute("DELETE FROM JUEGOS WHERE ID="+ dato)
    # print(juegos)
    miConexion.commit()
    miConexion.close()
    return juegos
     
    
if __name__ == "__main__":
    print("hola")
#    CrearBD()
