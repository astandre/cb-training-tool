# Herramienta recolectora de intenciones para entrenamiento de chatbots

## Requerimientos

Los requerimientos iniciales se encuentran en el archivo requirements.txt

Python 3.7

## Instalacion
Para instalar las dependencias necesarias usar el comando:

``
pip install -r requirements.txt
``

## Configuracion

Debemos configurar la base de datos que vayamos a usar, en el archivo .env (Este archivo puede estar invisible en entornos linux). Gracias al ORM las tablas se generaran automaticamente.

``
DATA_BASE='mysql+pymysql://user:pass@localhost/db_name'
``

Ejemplo:

``
DATA_BASE='mysql+pymysql://root:@localhost/test'
``

# Carga inicial de datos

Para crear la base de datos y cargar los datos iniciales ejecutar el archivo *initial_data.py*

# Guia de despliegue con wsgi_mod

https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/
