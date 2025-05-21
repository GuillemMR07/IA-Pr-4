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

dades = [
      # INFO ESTUDIS
    ("info,informacio", "L'INS Baix Camp imparteix els cursos de l'ESO, el Batxillerat i Cicles Formatius de Grau Mitjà i Superior. <br> El nostre centre ha mantingut en tots aquests anys una estreta relació amb la ciutat, formant part <br> del desenvolupament del municipi, primer amb la integració dels nostres professionals al món <br> laboral i també amb la formació dels/les nostres joves, preparant-los per anar a la universitat."),
    ("info,informacio,eso", "Aquí et deixo un document que et donarà una mica d'informació sobre l'ESO al nostre centre: <br> <a href='https://drive.google.com/file/d/1HPdhbQ-OClBPhBBbQIwwBQ4xigY6iy3X/view?usp=sharing'> Info ESO </a>"),
    ("info,informacio,bat,batxillerat,batxi,batxibac", "Aquí et deixo un document que et donarà una mica d'informació sobre el Batxillerat al nostre centre: <br> <a href='https://drive.google.com/file/d/1LImJALX6x_ehAV_LGbVxLc5aFf8blqg3/view?usp=share_link'> Info Batxillerat </a>"),
    ("info,informacio,cicle mitjà,cfgm,grau mitja,cicle formatiu de grau mitja", "Aquí et deixo uns document que et donaran una mica d'informació sobre la oferta formativa dels Cicles Formatius de Grau Mitjà al nostre centre: <br> <ul> <li><strong><a href='https://drive.google.com/file/d/1R33RyC4MvSt6RyxcwQCAulMulDTmwrfa/view?usp=drive_link'>CFGM Activitats Comercials</a></strong></li>  <li><strong><a href='https://drive.google.com/file/d/1qmQxu3_bztxPUget8WVhugpFusAPLcpt/view?usp=drive_link'>CFGM Cures Auxiliars d’Infermeria </a></strong></li> <li><strong><a href='https://drive.google.com/file/d/1IYS75kSFUMVCCrBqEfYoYsCsLnp2DCpe/view?usp=drive_link'>CFGM Farmàcia i Parafarmàcia</a></strong></li> <li><strong><a href='https://drive.google.com/file/d/1es7OlUMSfDJJe2g8bOdD0RtzVitRemhp/view?usp=drive_link'>CFGM Gestió Administrativa</a></strong></li> <li><strong><a href='https://drive.google.com/file/d/1uPs2OQ6svTLWc8mxY9kHHeupwG0hX0Wd/view?usp=drive_link'>CFGM Gestió Administrativa Jurídic</a></strong></li> <li><strong><a href='https://drive.google.com/file/d/1_UsaQtENoKhDgbbqX_fOcrQN67KKs-0A/view?usp=drive_link'>CFGM Sistemes Microinformàtics i Xarxes</a></strong></li>"),
    ("info,informacio,cicle superior,cfgs,grau superior,cicle formatiu de grau superior", "Aquí et deixo uns documents que et donaran una mica d'informació sobre la oferta formativa dels Cicles Formatius de Grau Superior a nostre centre: <br> <ul> <li><strong><a href='https://drive.google.com/file/d/19TvPgJLa9h4O9AVKMCphYamUW0458LqJ/view?usp=drive_link'>CFGS Administració i Finances </a></strong></li> <li><strong><a href='https://drive.google.com/file/d/1677VOQmrVoQqyIlTafaTeF1yrnwBn7PL/view?usp=drive_link'>CFGS Assistència a la Direcció </a></strong></li>  <li><strong><a href='https://drive.google.com/file/d/1S8MUqnfpJxA5SHpv-p6okZxy-H-ene33/view?usp=drive_link'>CFGS Administració de Sistemes Informàtics en Xarxa </a></strong></li> <li><strong><a href='https://drive.google.com/file/d/1VF6HWPCFE2y11eYtBUiZ6b5yOgZgUHV1/view?usp=drive_link'>CFGS Desenvolupament d’Aplicacions Web </a></strong></li> <li><strong><a href='https://drive.google.com/file/d/14jYIcOdg33fQ--Mqn1rypuXlsOvbeB2w/view?usp=sharing'>CFGS Desenvolupament d’Aplicacions Multiplataforma </a></strong></li> <li><strong><a href='https://drive.google.com/file/d/19SQTYgdbl7x6jmXFR6Km9wGzVjHGUbUL/view?usp=drive_link'>CFGS Màrqueting i Publicitat </a></strong></li> <li><strong><a href='https://drive.google.com/file/d/1ZbJwgQV-8B2BlExwPDJQbM9pklBKdETu/view?usp=drive_link'>CFGS Higiene Bucodental </a></strong></li> </ul>"),
    # PREINSCRIPCIONS
    ("preinscripcio,matricula", "Et deixo per aquí els diversos calendaris de preinscripció i matricula de les diverses modalitats del nostre centre: <br> <ul><li><strong><a href='https://docs.google.com/document/d/1GiLTX5C-UNjWr-0d4UZCnJMERmRrn9f9LUjF52nI-lw/edit?usp=sharing'>ESO</a></strong></li> <li><strong><a href='https://docs.google.com/document/d/1a2KUkKhoQrRVjdsB45hJjAn9MtvPiDl6xHS1ZemuIIU/edit?usp=sharing'>Batxillerat</a></strong></li> <li><strong><a href='https://docs.google.com/document/d/1SCzuPjPXSRfDuQ8rDvlKZV4zrByEluDGG-qI7GPlLzM/edit?usp=sharing'>Batxibac</a></strong></li> <li><strong><a href='https://docs.google.com/document/d/1r62DUcup-PeB6YD87WrkUjlVd2EL5my_X-nx4eXdicE/edit?usp=sharing'>CFGM</a></strong></li> <li><strong><a href='https://docs.google.com/document/d/1DCD_a9SnQb0_6mhy3yjn1e09FqOGeZVUKy0ZOeB1Tuw/edit?usp=sharing'>CFGS</a></strong></li></ul>"),
    ("preinscripcio,maticula,eso", "Et deixo per aquí el calendari de preinscripció i matricula de l'ESO: <br> <ul><li><strong><a href='https://docs.google.com/document/d/1GiLTX5C-UNjWr-0d4UZCnJMERmRrn9f9LUjF52nI-lw/edit?usp=sharing'>ESO</a></strong></li></ul>"),
    ("preinscripcio,matricula,batxillerat,bat,batxi", "Et deixo per aquí els calendaris de preinscripció i matricula de Batxillerat i Batxibac: <br> <ul><li><strong><a href='https://docs.google.com/document/d/1a2KUkKhoQrRVjdsB45hJjAn9MtvPiDl6xHS1ZemuIIU/edit?usp=sharing'>Batxillerat</a></strong></li> <li><strong><a href='https://docs.google.com/document/d/1SCzuPjPXSRfDuQ8rDvlKZV4zrByEluDGG-qI7GPlLzM/edit?usp=sharing'>Batxibac</a></strong></li> </ul>"),
    ("preinscripcio,matricula,batxibac,bac,baccalauréat", "Et deixo per aquí el calendari de preinscripció i matricula del Batxibac: <br> <ul><li><strong><a href='https://docs.google.com/document/d/1SCzuPjPXSRfDuQ8rDvlKZV4zrByEluDGG-qI7GPlLzM/edit?usp=sharing'>Batxibac</a></strong></li></ul>"),
    ("preinscripcio,cicles", "Et deixo per aquí els calendaris de preinscripció i matricula de Cicles Formatius: <br> <ul><li><strong><a href='https://docs.google.com/document/d/1r62DUcup-PeB6YD87WrkUjlVd2EL5my_X-nx4eXdicE/edit?usp=sharing'>CFGM</a></strong></li> <li><strong><a href='https://docs.google.com/document/d/1DCD_a9SnQb0_6mhy3yjn1e09FqOGeZVUKy0ZOeB1Tuw/edit?usp=sharing'>CFGS</a></strong></li></ul>"),
    ("preinscripcio,cicle mitjà,cfgm,grau mitja,cicle formatiu de grau mitja", "Et deixo per aquí el calendari de preinscripció i matricula de Cicles Formatius de Grau Mitjà: <br> <ul><li><strong><a href='https://docs.google.com/document/d/1r62DUcup-PeB6YD87WrkUjlVd2EL5my_X-nx4eXdicE/edit?usp=sharing'>CFGM</a></strong></li></ul>"),
    ("preinscripcio,cicle superior,cfgs,grau superior,cicle formatiu de grau superior", "Et deixo per aquí el calendari de preinscripció i matricula de Cicles Formatius de Grau Superior: <br> <ul><li><strong><a href='https://docs.google.com/document/d/1DCD_a9SnQb0_6mhy3yjn1e09FqOGeZVUKy0ZOeB1Tuw/edit?usp=sharing'>CFGS</a></strong></li> </ul>"),
    ("moodle,moodel", "Aquí et deixo l'enllaç per accedir al moodle del centre: <a href='https://www.insbaixcamp.cat/'>Moodle</a>"),
    ("xarxes socials,instagram,youtube,twitter,x,tiktok,facebook", "Aquí tens les diverses xarxes socials del noste centre: <ul><li><strong><a href='https://www.facebook.com/insbaixcampreus'>Facebook</a></strong></li> <li><strong><a href='https://www.instagram.com/insbaixcamp/'>Instagram</a></strong></li> <li><strong><a href='https://www.tiktok.com/@institutbaixcamp'>Tiktok</a></strong></li> <li><strong><a href='https://twitter.com/INSBaixCamp'>X / Twitter</a></strong></li> <li><strong><a href='https://www.youtube.com/user/INSTITUTBAIXCAMP'>YouTube</a></strong></li></ul>"),
    ("horari,consergeria", "L'horari de consergeria és de 8:30 a 22:00 de dilluns a divendres."),
    ("agenda,agendes,eso", "Et deixo per aquí l’enllaç a les agendes de l’ESO: <br> <a href='https://insbaixcamp.org/index.php/alumnat-i-families/deures-cursos-eso'> Agendes ESO </a>"),
    ("cantina,cafeteria,menjador,menu", "Et deixo aquí l’enllaç amb el menú de la cantina del dia d’avui: <br> <a href='https://docs.google.com/document/d/1gZEBbql7y23QtLILJfWiJyPGjS8MnJ1By_BobQPM-GQ/edit?tab=t.0'> Menú Cantina </a>"),
    ("fotografies,fotos,foto", "Aquí tens l’enllaç que et portarà al àlbum de fotografíes del nostre centre: <br> <a href='https://insbaixcamp.org/index.php/55-notes/728-fotos-ins-baix-camp'> Àlbum de fotos </a>"),
    ("afa,ampa,amipa", "Aquí et deixo una mica d'informació sobre el que és l'AFA: <br> Ajudem en les necessitats dels nostres fills: <br> <ul><li>Subvencionem excursions i festes.</li> <li>Participem en el Consell Escolar del centre.</li> <li>També tenim representació al consell escolar municipal per tal d'aconseguir el millor pels nostres fills i filles</li> <li>Ens encarreguem del lloguer dels armariets</li> </ul> <br> Contacte: afa@insbaixcamp.cat <br> <br> Fes-te'n soci/sòcia i tindràs avantatges. Entre tots podrem fer una associació molt més propera i si tens idees, no dubtis a compartir-les."),
    ("horari,afa,ampa,amipa", "L'horari de l'AFA és de Dimecres a Divendres de 17:30 a 19:30"),
    ("horari,secretaria", "L'horari de secretaria és: <br><strong> De l'1 d'octubre al 31 de maig </strong><br> De dilluns a divendres de 9:00 a 13:00h <br> De dilluns a dijous de 16:00 a 17:30 h <br><br><strong> De l'1 de juny al 30 de setembre </strong> <br> De dilluns a divendres de 9:00 a 13:00h <br> <strong TANCAT </strong> per vacances del 25 de jualiol al 28 d'agost."),
    ("contacte", "Aquí et deixo un mica d'informació de contacte del centre i la seva direcció: <br> Carrer Jacint Barrau,1 <br> 43201-Reus <br> Telèfon: 977310953 <br> Fax: 977314721 <br> e-mail: e3002594@xtec.cat"),
    ("telefon", "El número de telèfon del centre es 977310953."),
    ("junta,directiva", "Els membres de la junta directiva son: <br> Director: Josep G. Lluís <br> Cap d'Estudis ESO-BAT: Magda Abelló <br> Sotsdirector: Ferran Borrell <br> Cap d'Estudis FP: Daniel Andreu <br> Coordinador Pedagògic: Miquel Arcas <br> Secretària: Glòria Baldó <br> Administradora: Pilar Sanchez. "),
    ("sotsdirector", "L'actual sotsdirector del centre es el Sr. Ferran Borrell."),
    ("director", "L'actual director del centre es el Sr Josep G. Lluís."),
    ("cap d'estudis fp", "L'actual Cap d'Estudis d'FP es el Sr. Daniel Andreu. "),
    ("cap d'estudis eso", "L'actual Cap d'Estudis d'ESO es la Sra. Magda Abelló. "),
    ("cap d'estudis batxillerat", "L'actual Cap d'Estudis de Batxillerat es la Sra. Magda Abelló. "),
    ("coordinador pedagogic", "L'actual Coordinador Pedagògic del centre es el Sr. Miquel Arcas. "),
    ("administradora", "L'actual Administradora del centre es la Sra. Pilar Sánchez. "),
    ("secretaria", "L'actual Secretària del centre es la Sra. Glòria Baldó. "),
    ("calendari,curs", "Aquí et deixo l'enllç per a accedir al calendari del curs: <br> <a href='https://docs.google.com/document/d/19Q0G9aO6BrnAapVsRBB3uSwI1p44WcyM6ovO0eTTiZg/edit?usp=sharing'> Calendari del curs </a>"),
    ("calendari,extraordinaria", "Aquí et deixo l'enllaç per a accedir al calendari dels exàmens d'extraordinària: <br> <a href='https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link'> Calendari exàmens d'extraoridnària </a>"),
    ("calendari,ordinaria", "Aquí et deixo l'enllaç per a accedir al calendari dels exàmens d'ordinària: <br> <a href='https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link'> Calendari exàmens d'ordinària </a>"),
    ("calendari,repassos", "Aquí et deixo l'enllaç per a accedir al calendari dels repassos: <br> <a href='https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link'> Calendari repassos </a>"),
    ("calendari,fi,curs", "Aquí et deixo l'enllaç per a accedir al calendari dels exàmens i repassos de fí de curs: <br> <a href='https://drive.google.com/drive/folders/1e-iqAoXBSMlHsCgyvIpa2SgV1QZIfTx-?usp=drive_link'>Calendari fí de curs </a>"),
    ("calendari,proves,accés", "Aquí et deixo l'enllaç per a accedir al calendari de proves d'accés per a cicles formatius: <br> <a href='https://docs.google.com/document/d/1Ekk74Jq4O1ZjzotLHU_k9VHe8Q-IjZcoLHRvSYdyX6o/edit?tab=t.0#heading=h.abl4iitf91ks'>Calendari Proves d'Accés CF</a>"),
    ("espai,digital", "Per a poder anar al espai digital necessites sol·licitar cita prèvia, et deixo més informació al següent enllaç: <br> <a href='https://www.insbaixcamp.org/index.php/55-notes/1160-espai-digital'> Espai digital </a>"),
    ("erasmus", "Si vols obtenir més informació sobre l'Erasmus et deixo aquí un enllaç on trobarás tot el que necessites: <br> <a href='https://www.insbaixcamp.org/index.php/component/content/article/55-notes/406-projecte-erasmus-de-mobilitat-internacional-per-a-realitzar-estades-de-practiques-d-alumnat-de-cicles-formatius-en-empreses-i-entitats-estrangeres'> Erasmus+ </a>"),
  
    


]



cursor.executemany("INSERT INTO preguntes_respostes (paraules_clau, resposta) VALUES (?, ?)", dades)

conn.commit()
conn.close()
