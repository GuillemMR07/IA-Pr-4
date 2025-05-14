from flask import Flask, request, render_template, send_from_directory
from ia_institut import respondre_pregunta
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pregunta = request.form.get("pregunta")
        resposta = respondre_pregunta(pregunta)
    return render_template("index.html", resposta=resposta)

@app.route("/descarregar/<nom_fitxer>")
def descarregar(nom_fitxer):
    ruta = os.path.join("excursions")
    return send_from_directory(ruta, nom_fitxer, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
