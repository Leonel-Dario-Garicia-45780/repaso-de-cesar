
function agregar_categoria(){
    const categoria={
        nombre_de_categoria : texto_categoria.value 
    }

    const url = "/agregar_Categorias"
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

