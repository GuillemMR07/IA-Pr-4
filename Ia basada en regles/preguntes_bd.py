import sqlite3

# Connexió i creació de la base de dades
conn = sqlite3.connect("preguntes.db")
cursor = conn.cursor()

# Crear taula
cursor.execute("""
    CREATE TABLE IF NOT EXISTS preguntes_respostes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paraules_clau TEXT NOT NULL,
        resposta TEXT NOT NULL
    )
""")

# Dades inicials
dades = [
    ("horari,classes", "L'horari lectiu és de dilluns a divendres de 8:00 a 14:30."),
    ("menjador,dinar", "El servei de menjador està disponible de 14:30 a 16:00."),
    ("festiu,vacances", "Els festius són Nadal, Setmana Santa i estiu. Consulta el calendari al web."),
    ("contacte,telèfon", "Pots trucar al 93 123 45 67 o escriure a institut@exemple.cat."),
    ("director,directora", "La directora actual de l'institut és la Sra. Maria Soler."),
    ("reunió,famílies", "Les reunions es comuniquen per correu o app amb antelació."),
]

# Inserir dades
cursor.executemany("INSERT INTO preguntes_respostes (paraules_clau, resposta) VALUES (?, ?)", dades)

# Guardar i tancar
conn.commit()
conn.close()

print("Base de dades creada amb èxit.")
