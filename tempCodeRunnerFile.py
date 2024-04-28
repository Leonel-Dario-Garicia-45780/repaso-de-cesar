from flask import Flask, render_template, request
import pymongo


app = Flask(__name__)

miConexion = pymongo.MongoClient("mongodb://localhost:27017/")

basedeDatos=miConexion['Repaso']

categorias=basedeDatos['categorias']
productos=basedeDatos['productos']
usuarios=basedeDatos['usuarios']

@app.route("/", methods=["GET","POST"])
def inicio():
    return render_template("inicio.html")

# enviar correo
from controlador.correo import *
from controlador.controlador_aplicacion import *

if __name__ == "__main__":
    app.run(port=3000, debug=True)