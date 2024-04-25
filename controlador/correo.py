from aplicacion import app
from flask import request, render_template
import yagmail

# enviar correo  ///////////////////////////////////////////
@app.route("/correo", methods=["GET","POST"])
def enviarcorreo():
    mensaje_respuesta=""
    if request.method == "POST":
        try:
            destinatario= request.form["para"]
            remitente= request.form["de"]
            asunto= request.form["asunto"]
            mensaje= request.form["mensaje"]
                                #correo y contraseña
            email= yagmail.SMTP("gun45780@gmail.com" , "qnwviudvxwmgcpfv")  

            email.send( to=destinatario,
                        subject=asunto,
                        contents=mensaje
                        )

            mensaje_respuesta = " correo enviado correctamente"

            return render_template("respuesta.html",mensaje=mensaje_respuesta)

        except Exception as error:
            mensaje_respuesta=f" error al enviar el correo: {error}"

    return render_template("archivo.html",mensaje=mensaje_respuesta)
# fin enviar correo  ///////////////////////////////////////////
