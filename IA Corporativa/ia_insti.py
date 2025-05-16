import sqlite3
import os
import glob
import unicodedata

def eliminar_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def respondre_pregunta(pregunta: str) -> str:
    pregunta = pregunta.lower()
    pregunta = eliminar_accents(pregunta)

    # Aquesta es una resposta especial en cas de que es pregunti per excursions, sortides o altres activitats
    if any(paraula in pregunta for paraula in ["excursions", "sortides", "activitats"]):
        pdf_path = buscar_pdf_excursions()
        if pdf_path:
            nom_fitxer = os.path.basename(pdf_path)
            return f"Podeu descarregar el document amb les pròximes activitats aquí: <a href='/descarregar/{nom_fitxer}'>Descarregar PDF</a> <br> O també fer clic al següent enllaç: <br> <a href='https://insbaixcamp.org/index.php/alumnat-i-families/agenda-setmanal'>Agenda Setmanal</a>"
        else:
            return "Encara no hi ha un PDF disponible amb les excursions programades."

    # La resta de preguntes serán solicitades a la base de dades
    conn = sqlite3.connect("preguntes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT paraules_clau, resposta FROM preguntes_respostes")
    resultats = cursor.fetchall()

    millor_puntuacio = 0
    millor_match = ""

    for paraules_clau, resposta in resultats:
        claus = [eliminar_accents(clau.strip().lower()) for clau in paraules_clau.split(",")]
        puntuacio = sum(1 for clau in claus if clau in pregunta)
        if puntuacio > millor_puntuacio:
            millor_puntuacio = puntuacio
            millor_match = resposta

    conn.close()

    if millor_puntuacio > 0:
        return millor_match
    else:
        return "Ho sento, no tinc informació sobre això. Contacta amb l'institut per més detalls. O prova d'escriure-ho d'una altra manera."

def buscar_pdf_excursions():
    carpeta = "excursions"
    coincidencies = glob.glob(os.path.join(carpeta, "Activitats*.pdf"))
    if coincidencies:
        return coincidencies[0]
    return None
