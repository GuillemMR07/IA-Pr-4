from flask import Flask, request, render_template, send_from_directory, session, redirect, url_for
from ia_insti import respondre_pregunta
import os

app = Flask(__name__)
app.secret_key = "una_clau_secreta"  

@app.route("/", methods=["GET", "POST"])
def index():
    if "historial" not in session:
        session["historial"] = []

    if request.method == "POST":

        pregunta = request.form.get("pregunta")
        resposta = respondre_pregunta(pregunta)

        # Afegim a l'historial
        session["historial"].append({"pregunta": pregunta, "resposta": resposta})
        session.modified = True  

        return redirect(url_for("index"))  

    return render_template("index.html", historial=session["historial"])

@app.route("/descarregar/<nom_fitxer>")
def descarregar(nom_fitxer):
    ruta = os.path.join("excursions")
    return send_from_directory(ruta, nom_fitxer, as_attachment=True)

@app.route("/esborrar", methods=["POST"])
def esborrar():
    session["historial"] = []
    session.modified = True
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
