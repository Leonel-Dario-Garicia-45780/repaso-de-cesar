from flask import Flask, render_template, request

# enviar correo
""" from werkzeug.utils import secure_filename """
import yagmail
""" import os """

app = Flask(__name__)

# enviar correo
app.config

@app.route("/", methods=["GET","POST"])
def inicio():
    return render_template("archivo.html")

# enviar correo  ///////////////////////////////////////////
@app.route("/correo", methods=["GET","POST"])
def enviarcorreo():
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

        except Exception as error:
            mensaje_respuesta=f" error al enviar el correo: {error}"

        return render_template("respuesta.html",mensaje=mensaje_respuesta)
# fin enviar correo  ///////////////////////////////////////////

if __name__ == "__main__":
    app.run(port=3000, debug=True)