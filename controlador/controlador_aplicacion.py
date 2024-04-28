from aplicacion import app, categorias, productos, usuarios
from flask import request, render_template, jsonify
import pymongo
from bson import ObjectId 

# usar la extencion Better coments para entender mejor el codigo
# todo  todo lo relacionado a una tabla de la base de datos
# ? renderisacion de las vistas
# * funciones del crud
# !  fin de lo relacionado a la tabla 

# todo lo relacionado con categorias
    # ? vista del formulario o html
@app.route("/agregar_categoria")
def vista_categoria():
    return render_template("funciones crud/categoria.html")
    # * funcion del bakend que recibe los datos del js (fetch)
@app.route("/funcion_agregar_Categorias", methods=["GET","POST"])
def agregar_categoria():
    estado=False
    mensaje=""
    try:
        dato_categoria= request.json
        accion=categorias.insert_one(dato_categoria)
        if accion.acknowledged:
            estado=True
            mensaje="categoria añadida"
            print(mensaje)
        else:
            mensaje="no se pudo agregar pa categoria"
            estado=False
            print(mensaje)
    except pymongo.errors.PyMongoError as error:
        mensaje = f"Error de MongoDB: {error}"
        # * variables que retornan al js
        #* mejor dicho la respuesta
    retorno={ "estado":estado, "mensaje":mensaje}
    return jsonify(retorno)

# ! fin de todo lo relacionado con categorias

@app.route("/tabla_productos", methods=["GET", "POST"])
def tabla_productos():
    try:
        lis_productos = productos.find()
        li_producto = []

        for p in lis_productos:
            categoria_id = p.get('categoria')
            if categoria_id and ObjectId.is_valid(categoria_id):
                categoria = categorias.find_one({'_id': ObjectId(categoria_id)})
                if categoria:
                    p['categoria'] = categoria['nombre']
            li_producto.append(p)

    except pymongo.errors.PyMongoError as error:
        print(f"{error}")

    return render_template("tabla.html", productos=li_producto)


# todo lo relacionado con productos
    # ? vista de agragar
@app.route("/agregar_producto")
def vista_agragar_producto():
    #* las categorias se muestran en el html
    categorias_lista = categorias.find()
    return render_template("funciones crud/productos/agregar_producto.html", categorias=categorias_lista)
    # * funcion agregar
@app.route("/funcion_agregar_producto",methods=["GET","POST"])
def agregar_producto():
    estado=False
    mensaje=""
    try:
        dato_producto=request.json
        accion=productos.insert_one(dato_producto)
        if accion.acknowledged:
            estado=True
            mensaje="producto agregado correctamente"
            print(mensaje)
        else:
            estado=False
            mensaje="error al agregar el producto"
    except pymongo.errors.PyMongoError as error:
        mensaje = f"Error de MongoDB: {error}"
        #* respuesta del servidor
    retorno={"estado":estado,"mensaje":mensaje}
    return jsonify(retorno)

    # ? vista de editar

@app.route("/editar_producto/<id_producto>")
def vista_editar_producto(id_producto):
    # ? la vista
    categorias_lista = categorias.find()
    return render_template("funciones crud/productos/editar_producto.html", categorias=categorias_lista)
    # * funcion editar
@app.route("/funcion_editar_producto/<id_producto>", methods=["POST"])
def editar_producto(id_producto):
    estado = False
    mensaje = ""
    try:
        dato_producto_editado=request.json
        accion=productos.update_one({"_id": ObjectId(id_producto)},{"$set": dato_producto_editado} )
        if accion.modified_count > 0  :
            estado=True
            mensaje="producto editado correctamente"
            print(mensaje)
    except pymongo.errors.PyMongoError as error:
        mensaje = f"Error de MongoDB: {error}"
    
    retorno = {"estado": estado, "mensaje": mensaje}
    return jsonify(retorno)


    # ? vista de eliminar
@app.route("/elimiar_producto")
def vista_eliminar_producto():
    return render_template("")

@app.route("/eliminar-producto/<idProducto>", methods=["POST"])
def eliminarProducto(idProducto):
  estado = False
  mensaje = ""
  try:
    objetoFiltro = {"_id": ObjectId(idProducto)}
    accion = productos.delete_one(objetoFiltro)
    if accion.deleted_count > 0:
      estado = True
      mensaje = "Producto eliminado correctamente"
    else:
      mensaje = f"Error al eliminar el producto con ID {idProducto}"
  except pymongo.errors.PyMongoError as error:
    mensaje = f"Error de MongoDB: {error}"

  retorno = {"estado": estado, "mensaje": mensaje}
  return jsonify(retorno)




# ! fin de todo lo relacionado con productos

