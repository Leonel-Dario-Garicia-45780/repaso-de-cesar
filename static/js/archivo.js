


function agregar_categoria(){
    const categoria={
        nombre_de_categoria : texto_categoria.value 
    }
    // esta es la url de la funcion del bakend
    // la accion como tal, no la vista
    const url = "/funcion_agregar_Categorias"
    fetch(url, {
        method:"POST",
        body: JSON.stringify(categoria),
        headers:{
            "Content-Type":"application/json",
        }
    })
    .then(respuesta=>respuesta.json())
    .then(resultado=>{
        if(resultado.estado){
            alert("categoria agregada correctamente")
        }else{
            alert ("error al agregar la categoria")
        }
    })

}

function agregar_productos(){
    const producto={
            id_del_producto:    id_producto.value,
            nombre_del_producto: nombre_producto.value,
            precio_del_producto:  precio_producto.value,
            categoria_del_producto: categoria.value 
}
    const url="/funcion_agregar_producto"
    fetch(url,{
        method:"POST",
        body: JSON.stringify(producto),
        headers:{
            "Content-Type":"application/json",
        }
    })
    .then(respuesta=>respuesta.json())
    .then(resultado=>{
        if(resultado.estado){
            alert("producto agregado correctamente")
        }else{
            alert ("error al agregar el producto")
        }
    })

}

function editar_productos(){
    const id_producto = id_producto_editado.value;
    const producto_editado={
            id_del_producto_editado:       id_producto_editado.value,
            nombre_del_producto_editado:    nombre_producto_editado.value,
            precio_del_producto_editado:     precio_producto_editado.value,
            categoria_del_producto_editado: categoria_editado.value 
    }
    const url="/funcion_editar_producto"+id_producto
    fetch(url,{
        method:"POST",
        body: JSON.stringify(producto_editado),
        headers:{
            "Content-Type":"application/json",
        }
    })
    .then(respuesta=>respuesta.json())
    .then(resultado=>{
        if(resultado.estado){
            alert("producto editado correctamente")
        }else{
            alert ("error al editar el producto el producto")
        }
    })

}

function eliminar_productos(){}



/* function agregar_usuario(){

}
 */