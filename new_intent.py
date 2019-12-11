from app import Triple
from app import db

# Intencion Listar Cursos
db.session.add(Triple(subject='ListarCursos', predicate='rdf:type', object="Intent"))
db.session.add(Triple(subject='ListarCursos', predicate='hasDescription',
                      object="¿Como preguntarias por un listado de los cursos?"))
db.session.add(Triple(subject='ListarCursos', predicate='hasKeyword', object="ListarCursos-Keyword1"))
db.session.add(Triple(subject='ListarCursos', predicate='hasKeyword', object="ListarCursos-Keyword2"))
db.session.add(Triple(subject='ListarCursos', predicate='hasKeyword', object="ListarCursos-Keyword3"))
db.session.add(Triple(subject='ListarCursos-Keyword1', predicate='hasWord', object="listar"))
db.session.add(Triple(subject='ListarCursos-Keyword1', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ListarCursos-Keyword2', predicate='hasWord', object="todos"))
db.session.add(Triple(subject='ListarCursos-Keyword2', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ListarCursos-Keyword3', predicate='hasWord', object="oferta"))
db.session.add(Triple(subject='ListarCursos-Keyword3', predicate='hasPOS', object="NOUN"))
db.session.add(Triple(subject='ListarCursos', predicate='hasSentence', object="ListarCursos-Sentence-1"))
db.session.add(Triple(subject='ListarCursos', predicate='hasSentence', object="ListarCursos-Sentence-2"))
db.session.add(Triple(subject='ListarCursos', predicate='hasSentence', object="ListarCursos-Sentence-3"))
db.session.add(Triple(subject='ListarCursos-Sentence-1', predicate='hasText', object="Que cursos hay?"))
db.session.add(
    Triple(subject='ListarCursos-Sentence-2', predicate='hasText', object="Cuál es la oferta actual de cursos"))
db.session.add(Triple(subject='ListarCursos-Sentence-3', predicate='hasText',
                      object="Muestrame los cursos"))

db.session.commit()