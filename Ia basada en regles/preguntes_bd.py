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
    ("horari,consergeria", "L'horari de consergeria és de 8:30 a 22:00 de dilluns a divendres."),
    ("horari,secretaria", "L'horari de secretaria és: <br> De l'1 d'octubre al 31 de maig <br> De dilluns a divendres de 9:00 a 13:00h <br> De dilluns a dijous de 16:00 a 17:30 h"),
    ("contacte,telèfon,mail,fax,direcció", "Aquí et deixo un mica d'informació de contacte del centre i la seva direcció: <br> Carrer Jacint Barrau,1 <br> 43201-Reus <br> Telèfon: 977310953 <br> Fax: 977314721 <br> e-mail: e3002594@xtec.cat"),
    
    ("director,directora", "La directora actual de l'institut és la Sra. Maria Soler."),
    ("reunió,famílies", "Les reunions es comuniquen per correu o app amb antelació."),
    ("menjador,dinar", "El servei de menjador està disponible de 14:30 a 16:00."),
    ("festiu,vacances", "Els festius són Nadal, Setmana Santa i estiu. Consulta el calendari al web."),
]

# Inserir dades
cursor.executemany("INSERT INTO preguntes_respostes (paraules_clau, resposta) VALUES (?, ?)", dades)

# Guardar i tancar
conn.commit()
conn.close()

print("Base de dades creada amb èxit.")
