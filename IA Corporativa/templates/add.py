import sqlite3

conn = sqlite3.connect("preguntes.db")
cursor = conn.cursor()

# Exemple: afegir nova pregunta
cursor.execute("""
    INSERT INTO preguntes_respostes (paraules_clau, resposta)
    VALUES (?, ?)
""", ("llibres,material", "Els llibres de text es poden consultar a la web del centre."))

conn.commit()
conn.close()
