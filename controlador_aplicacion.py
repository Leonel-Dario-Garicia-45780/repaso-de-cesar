from aplicacion import app, categorias
from flask import request, render_template, jsonify
import pymongo

@app.route("/agregar_Categorias", methods=["GET","POST"])
def agregar_categoria():
    estado=False
    mensaje=""
    try:
        dato_categoria= request.json
        #nombre_categoria= dato_categoria.get("nombre_de_categoria")

        if dato_categoria:
            categoria={
                "nombre_de_categoria":dato_categoria
                }
            resultado = categorias.insert_one(dato_categoria)
            if (resultado.acknowledged):
                mensaje="categoria añadida"
                estado=True
            else:
                mensaje="problemas"
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

