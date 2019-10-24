from app import Triple
from app import db

db.create_all()

# Obtener informacion de un curso
db.session.add(Triple(subject='ObtenerInformacion', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasDescription',
                      object="Como preguntarias por informacion de un curso"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasKeyword', object="ObtenerInformacion-Keyword1"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasKeyword', object="ObtenerInformacion-Keyword2"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasKeyword', object="ObtenerInformacion-Keyword3"))
db.session.add(Triple(subject='ObtenerInformacion-Keyword1', predicate='hasWord', object="resumir"))
db.session.add(Triple(subject='ObtenerInformacion-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerInformacion-Keyword2', predicate='hasWord', object="mooc"))
db.session.add(Triple(subject='ObtenerInformacion-Keyword2', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerInformacion-Keyword3', predicate='hasWord', object="cursar"))
db.session.add(Triple(subject='ObtenerInformacion-Keyword3', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasSentence', object="ObtenerInformacion-Sentence-1"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasSentence', object="ObtenerInformacion-Sentence-2"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasSentence', object="ObtenerInformacion-Sentence-3"))
db.session.add(Triple(subject='ObtenerInformacion', predicate='hasSentence', object="ObtenerInformacion-Sentence-4"))
db.session.add(Triple(subject='ObtenerInformacion-Sentence-1', predicate='hasText', object="De que trata el mooc?"))
db.session.add(
    Triple(subject='ObtenerInformacion-Sentence-2', predicate='hasText', object="Muestrame un resumen del mooc?"))
db.session.add(Triple(subject='ObtenerInformacion-Sentence-3', predicate='hasText', object="Contenido del curso "))
db.session.add(
    Triple(subject='ObtenerInformacion-Sentence-4', predicate='hasText', object="Breve introducción al curso"))
# Obtener fechas importantes de un curso

db.session.add(Triple(subject='ObtenerFechas', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ObtenerFechas', predicate='hasDescription',
                      object="¿Como preguntarias por las fechas importantes de un curso?"))
db.session.add(Triple(subject='ObtenerFechas', predicate='hasKeyword', object="ObtenerFechas-Keyword1"))
db.session.add(Triple(subject='ObtenerFechas', predicate='hasKeyword', object="ObtenerFechas-Keyword2"))
db.session.add(Triple(subject='ObtenerFechas', predicate='hasKeyword', object="ObtenerFechas-Keyword3"))
db.session.add(Triple(subject='ObtenerFechas-Keyword1', predicate='hasWord', object="fechas"))
db.session.add(Triple(subject='ObtenerFechas-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerFechas-Keyword2', predicate='hasWord', object="importantes"))
db.session.add(Triple(subject='ObtenerFechas-Keyword2', predicate='hasPOS', object="ADJ"))
db.session.add(Triple(subject='ObtenerFechas-Keyword3', predicate='hasWord', object="clave"))
db.session.add(Triple(subject='ObtenerFechas-Keyword3', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerFechas', predicate='hasSentence', object="ObtenerFechas-Sentence-1"))
db.session.add(Triple(subject='ObtenerFechas', predicate='hasSentence', object="ObtenerFechas-Sentence-2"))
db.session.add(Triple(subject='ObtenerFechas', predicate='hasSentence', object="ObtenerFechas-Sentence-3"))
db.session.add(Triple(subject='ObtenerFechas-Sentence-1', predicate='hasText',
                      object="Cuales son las fechas importantes del curso?"))
db.session.add(Triple(subject='ObtenerFechas-Sentence-2', predicate='hasText', object="Fechas clave del curso"))
db.session.add(
    Triple(subject='ObtenerFechas-Sentence-3', predicate='hasText', object="Que fechas debo tomar en cuenta"))

# Obtener fechas de inicio
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasDescription',
                      object="¿Como preguntarias por las fechas de inicio de un curso?"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasKeyword', object="ObtenerFechasInicio-Keyword1"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasKeyword', object="ObtenerFechasInicio-Keyword2"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasKeyword', object="ObtenerFechasInicio-Keyword3"))
db.session.add(Triple(subject='ObtenerFechasInicio-Keyword1', predicate='hasWord', object="empezar"))
db.session.add(Triple(subject='ObtenerFechasInicio-Keyword1', predicate='hasPOS', object="VERB"))
db.session.add(Triple(subject='ObtenerFechasInicio-Keyword2', predicate='hasWord', object="fecha"))
db.session.add(Triple(subject='ObtenerFechasInicio-Keyword2', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerFechasInicio-Keyword3', predicate='hasWord', object="iniciar"))
db.session.add(Triple(subject='ObtenerFechasInicio-Keyword3', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasSentence', object="ObtenerFechasInicio-Sentence-1"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasSentence', object="ObtenerFechasInicio-Sentence-2"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasSentence', object="ObtenerFechasInicio-Sentence-3"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasSentence', object="ObtenerFechasInicio-Sentence-4"))
db.session.add(
    Triple(subject='ObtenerFechasInicio-Sentence-1', predicate='hasText', object="Cuándo empiezan los cursos ?"))
db.session.add(
    Triple(subject='ObtenerFechasInicio-Sentence-2', predicate='hasText', object="Fecha de inicio de los moocs?"))
db.session.add(
    Triple(subject='ObtenerFechasInicio-Sentence-3', predicate='hasText', object="Día de inicio de los moocs ?"))
db.session.add(
    Triple(subject='ObtenerFechasInicio-Sentence-4', predicate='hasText', object="En que fechá inician los moocs?"))

# Intencion obtener prerequisitos
db.session.add(Triple(subject='ObtenerPrerequisitos', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ObtenerPrerequisitos', predicate='hasDescription',
                      object="¿Como preguntarias por los requisitos previos de un curso?"))
db.session.add(Triple(subject='ObtenerPrerequisitos', predicate='hasKeyword', object="ObtenerPrerequisitos-Keyword1"))
db.session.add(Triple(subject='ObtenerPrerequisitos', predicate='hasKeyword', object="ObtenerPrerequisitos-Keyword2"))
db.session.add(Triple(subject='ObtenerPrerequisitos-Keyword1', predicate='hasWord', object="prerequisitos"))
db.session.add(Triple(subject='ObtenerPrerequisitos-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerPrerequisitos-Keyword2', predicate='hasWord', object="requisitos"))
db.session.add(Triple(subject='ObtenerPrerequisitos-Keyword2', predicate='hasPOS', object="NOUN"))
db.session.add(
    Triple(subject='ObtenerPrerequisitos', predicate='hasSentence', object="ObtenerPrerequisitos-Sentence-1"))
db.session.add(
    Triple(subject='ObtenerPrerequisitos', predicate='hasSentence', object="ObtenerPrerequisitos-Sentence-2"))
db.session.add(
    Triple(subject='ObtenerPrerequisitos', predicate='hasSentence', object="ObtenerPrerequisitos-Sentence-3"))
db.session.add(
    Triple(subject='ObtenerPrerequisitos', predicate='hasSentence', object="ObtenerPrerequisitos-Sentence-4"))
db.session.add(
    Triple(subject='ObtenerPrerequisitos', predicate='hasSentence', object="ObtenerPrerequisitos-Sentence-5"))
db.session.add(
    Triple(subject='ObtenerPrerequisitos-Sentence-1', predicate='hasText', object="Cuáles son los prerequisitos?"))
db.session.add(
    Triple(subject='ObtenerPrerequisitos-Sentence-2', predicate='hasText', object="Requisitos previos de ingreso "))
db.session.add(
    Triple(subject='ObtenerPrerequisitos-Sentence-3', predicate='hasText', object="Dame a conocer los prerequisitos"))
db.session.add(Triple(subject='ObtenerPrerequisitos-Sentence-4', predicate='hasText',
                      object="Me puedes indicar los prerequistos necesarios?"))
db.session.add(Triple(subject='ObtenerPrerequisitos-Sentence-5', predicate='hasText',
                      object="Que necesito saber antes de iniciar el curso"))

# Intencion obtener duracion

db.session.add(Triple(subject='ObtenerDuracion', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasDescription',
                      object="¿Como preguntarias por la duracion de un curso?"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasKeyword', object="ObtenerDuracion-Keyword1"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasKeyword', object="ObtenerDuracion-Keyword2"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasKeyword', object="ObtenerDuracion-Keyword3"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasKeyword', object="ObtenerDuracion-Keyword4"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword1', predicate='hasWord', object="tiempo"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword2', predicate='hasWord', object="duración"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword2', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword3', predicate='hasWord', object="hora"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword3', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword4', predicate='hasWord', object="semana"))
db.session.add(Triple(subject='ObtenerDuracion-Keyword4', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasSentence', object="QObtenerDuracion-Sentence-1"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasSentence', object="ObtenerDuracion-Sentence-2"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasSentence', object="ObtenerDuracion-Sentence-3"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasSentence', object="ObtenerDuracion-Sentence-4"))
db.session.add(Triple(subject='ObtenerDuracion', predicate='hasSentence', object="ObtenerDuracion-Sentence-5"))
db.session.add(Triple(subject='ObtenerDuracion-Sentence-1', predicate='hasText', object="Qué tiempo dura el curso ?"))
db.session.add(Triple(subject='ObtenerDuracion-Sentence-2', predicate='hasText', object="Duración del curso "))
db.session.add(Triple(subject='ObtenerDuracion-Sentence-3', predicate='hasText', object="Número de horas del mooc?"))
db.session.add(Triple(subject='ObtenerDuracion-Sentence-4', predicate='hasText',
                      object="En cuántas semanas se realiza el curso? "))
db.session.add(Triple(subject='ObtenerDuracion-Sentence-5', predicate='hasText', object="Cuanto dura el curso"))

# Intencion Obtener Precio

db.session.add(Triple(subject='ObtenerPrecio', predicate='rdf:type', object="Intent"))
db.session.add(
    Triple(subject='ObtenerPrecio', predicate='hasDescription', object="¿Como preguntarias por el precio de un curso?"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasKeyword', object="ObtenerPrecio-Keyword1"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasKeyword', object="ObtenerPrecio-Keyword2"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasKeyword', object="ObtenerPrecio-Keyword3"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasKeyword', object="ObtenerPrecio-Keyword4"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword1', predicate='hasWord', object="preciar"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword2', predicate='hasWord', object="valer"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword2', predicate='hasPOS', object="VERB"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword3', predicate='hasWord', object="costo"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword3', predicate='hasPOS', object="PROPN"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword4', predicate='hasWord', object="inversión"))
db.session.add(Triple(subject='ObtenerPrecio-Keyword4', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasSentence', object="ObtenerPrecio-Sentence-1"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasSentence', object="ObtenerPrecio-Sentence-2"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasSentence', object="ObtenerPrecio-Sentence-3"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasSentence', object="ObtenerPrecio-Sentence-4"))
db.session.add(Triple(subject='ObtenerPrecio', predicate='hasSentence', object="ObtenerPrecio-Sentence-5"))
db.session.add(Triple(subject='ObtenerPrecio-Sentence-1', predicate='hasText', object="Cuál es el precio?"))
db.session.add(Triple(subject='ObtenerPrecio-Sentence-2', predicate='hasText', object="Cuánto vale?"))
db.session.add(Triple(subject='ObtenerPrecio-Sentence-3', predicate='hasText', object="Valor del curso?"))
db.session.add(Triple(subject='ObtenerPrecio-Sentence-4', predicate='hasText', object="Costo "))
db.session.add(Triple(subject='ObtenerPrecio-Sentence-5', predicate='hasText', object="Inversión total del curso "))

# Intencion obtener docente
db.session.add(Triple(subject='ObtenerDocente', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasDescription',
                      object="¿Como preguntarias por el docente encargado de un curso?"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasKeyword', object="ObtenerDocente-Keyword1"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasKeyword', object="ObtenerDocente-Keyword2"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasKeyword', object="ObtenerDocente-Keyword3"))
db.session.add(Triple(subject='ObtenerDocente-Keyword1', predicate='hasWord', object="profesor"))
db.session.add(Triple(subject='ObtenerDocente-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerDocente-Keyword2', predicate='hasWord', object="docente"))
db.session.add(Triple(subject='ObtenerDocente-Keyword2', predicate='hasPOS', object="ADJ"))
db.session.add(Triple(subject='ObtenerDocente-Keyword3', predicate='hasWord', object="profesor"))
db.session.add(Triple(subject='ObtenerDocente-Keyword3', predicate='hasPOS', object="VERB"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasSentence', object="ObtenerDocente-Sentence-1"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasSentence', object="ObtenerDocente-Sentence-2"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasSentence', object="ObtenerDocente-Sentence-3"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasSentence', object="ObtenerDocente-Sentence-4"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasSentence', object="ObtenerDocente-Sentence-5"))
db.session.add(Triple(subject='ObtenerDocente', predicate='hasSentence', object="ObtenerDocente-Sentence-6"))
db.session.add(
    Triple(subject='ObtenerDocente-Sentence-1', predicate='hasText', object="Quién es mi profesor en el curso?"))
db.session.add(Triple(subject='ObtenerDocente-Sentence-2', predicate='hasText', object="Docente del mooc?"))
db.session.add(Triple(subject='ObtenerDocente-Sentence-3', predicate='hasText', object="Qué docente imparte el mooc?"))
db.session.add(Triple(subject='ObtenerDocente-Sentence-4', predicate='hasText',
                      object="Quién es el docente encargado de la materia?"))
db.session.add(Triple(subject='ObtenerDocente-Sentence-5', predicate='hasText', object="Nombre del docente del mooc"))
db.session.add(
    Triple(subject='ObtenerDocente-Sentence-6', predicate='hasText', object="Que profesor esta a cargo del curso"))

# Intencion Obtener Cotenidos
db.session.add(Triple(subject='ObtenerContenidos', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ObtenerContenidos', predicate='hasDescription',
                      object="¿Como preguntarias por los temas de un curso?"))
db.session.add(Triple(subject='ObtenerFechasInicio', predicate='hasKeyword', object="ObtenerContenidos-Keyword1"))
db.session.add(Triple(subject='ObtenerContenidos', predicate='hasKeyword', object="ObtenerContenidos-Keyword2"))
db.session.add(Triple(subject='ObtenerContenidos', predicate='hasKeyword', object="ObtenerContenidos-Keyword3"))
db.session.add(Triple(subject='ObtenerContenidos-Keyword1', predicate='hasWord', object="contenido"))
db.session.add(Triple(subject='ObtenerContenidos-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerContenidos-Keyword2', predicate='hasWord', object="temático"))
db.session.add(Triple(subject='ObtenerContenidos-Keyword2', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerContenidos-Keyword3', predicate='hasWord', object="temas"))
db.session.add(Triple(subject='ObtenerContenidos-Keyword3', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ObtenerContenidos', predicate='hasSentence', object="ObtenerContenidos-Sentence-1"))
db.session.add(Triple(subject='ObtenerContenidos', predicate='hasSentence', object="ObtenerContenidos-Sentence-2"))
db.session.add(Triple(subject='ObtenerContenidos', predicate='hasSentence', object="ObtenerContenidos-Sentence-3"))
db.session.add(Triple(subject='ObtenerContenidos-Sentence-1', predicate='hasText', object="Contenido del curso "))
db.session.add(
    Triple(subject='ObtenerContenidos-Sentence-2', predicate='hasText', object="Cuál es la temática de cada curso?"))
db.session.add(Triple(subject='ObtenerContenidos-Sentence-3', predicate='hasText',
                      object="Qué temas se van a tratar en cada curso?"))

db.session.commit()
print("Done")