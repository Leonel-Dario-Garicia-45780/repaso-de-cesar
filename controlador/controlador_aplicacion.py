from aplicacion import app, categorias
from flask import request, render_template, jsonify
import pymongo

@app.route("/agregar_Categorias", methods=["GET","POST"])
def agregar_categoria():
    estado=False
    mensaje=""
    try:
        dato_categoria= request.json
        nombre_categoria= dato_categoria.get("nombre_de_categoria")

        if nombre_categoria:
            categoria={"nombre de categoria":dato_categoria}
            categorias.insert_one(categoria)
            mensaje="categoria añadida"
            estado=True
            print(mensaje)
        else:
            mensaje="no se pudo agregar pa categoria"
            estado=False
            print(mensaje)

    except pymongo.errors.PyMongoError as error:
        mensaje = f"Error de MongoDB: {error}"
        # variablees que retornan al js
    
    retorno={ "estado":estado, "mensaje":mensaje}

    return jsonify(retorno)

