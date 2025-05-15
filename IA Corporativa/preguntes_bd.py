import sqlite3


conn = sqlite3.connect("preguntes.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS preguntes_respostes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paraules_clau TEXT NOT NULL,
        resposta TEXT NOT NULL
    )
""")

# Paràmetres de les dades que es crearan juntament amb la taula
dades = [
    ("horari,consergeria", "L'horari de consergeria és de 8:30 a 22:00 de dilluns a divendres."),
    ("horari,secretaria", "L'horari de secretaria és: <br> De l'1 d'octubre al 31 de maig <br> De dilluns a divendres de 9:00 a 13:00h <br> De dilluns a dijous de 16:00 a 17:30 h"),
    ("contacte", "Aquí et deixo un mica d'informació de contacte del centre i la seva direcció: <br> Carrer Jacint Barrau,1 <br> 43201-Reus <br> Telèfon: 977310953 <br> Fax: 977314721 <br> e-mail: e3002594@xtec.cat"),
    ("telèfon", "El número de telèfon del centre es 977310953."),
    ("qui,junta,directiva", "Els membres de la junta directiva son: <br> Director: Josep G. Lluís <br> Cap d'Estudis ESO-BAT: Magda Abelló <br> Sotsdirector: Ferran Borrell <br> Cap d'Estudis FP: Daniel Andreu <br> Coordinador Pedagògic: Miquel Arcas <br> Secretària: Glòria Baldó <br> Administradora: Pilar Sanchez. "),
    ("qui,director", "L'actual director del centre es el Sr Josep G. Lluís. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Josep_Lluis_2.jpg"),
    ("qui,sotsdirector", "L'actual sotsdirector del centre es el Sr. Ferran Borrell. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Ferran_Borrell_2.jpeg"),
    ("qui,cap,estudis,fp", "L'actual Cap d'Estudis d'FP es el Sr. Daniel Andreu. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Daniel_Andreu_2.jpeg"),
    ("qui,cap,estudis,eso", "L'actual Cap d'Estudis d'ESO es la Sra. Magda Abelló. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Magda_Abello_2b.jpeg"),
    ("qui,cap,estudis,batxillerat", "L'actual Cap d'Estudis de Batxillerat es la Sra. Magda Abelló. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Magda_Abello_2b.jpeg"),
    ("qui,coordinador,pedagogic", "L'actual Coordinador Pedagògic del centre es el Sr. Miquel Arcas. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Miquel_Arcas_2.jpeg "),
    ("qui,administradora", "L'actual Administradora del centre es la Sra. Pilar Sánchez. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Pilar_Sanchez_2.jpeg"),
    ("qui,secretaria", "L'actual Secretària del centre es la Sra. Glòria Baldó. <br> https://www.insbaixcamp.org/images/Curs_21-22/Equip_Directiu/Gloria_Baldo_2.jpeg"),
    ("calendari,curs", "Aquí et deixo l'enllç per a accedir al calendari del curs: <br> https://docs.google.com/document/d/19Q0G9aO6BrnAapVsRBB3uSwI1p44WcyM6ovO0eTTiZg/edit?usp=sharing"),
    ("calendari,extraordinaria", "Aquí et deixo l'enllaç per a accedir al calendari dels exàmens d'extraordinària: <br> https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link"),
    ("calendari,ordinaria", "Aquí et deixo l'enllaç per a accedir al calendari dels exàmens d'ordinària: <br> https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link"),
    ("calendari,repassos", "Aquí et deixo l'enllaç per a accedir al calendari dels repassos: <br> https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link"),
    ("calendari,fi,curs", "Aquí et deixo l'enllaç per a accedir al calendari dels exàmens i repassos de fí de curs: <br> https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link"),
]


cursor.executemany("INSERT INTO preguntes_respostes (paraules_clau, resposta) VALUES (?, ?)", dades)

conn.commit()
conn.close()

print("Base de dades creada amb èxit.")
