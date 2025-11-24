
Descripción de la aplicación y guía paso a paso para su funcionamiento local. 

UANFilms: Plataforma de Catálogo de Películas

UANFilms es una aplicación web full-stack desarrollada con Django y React que permite a los usuarios explorar, añadir y reseñar películas. Este proyecto está diseñado para funcionar tanto en un entorno de desarrollo local como para ser desplegado en la nube utilizando Azure.

Características Principales

Backend Robusto con Django: API RESTful construida con Django REST Framework.

Frontend Moderno con React: Interfaz de usuario dinámica y reactiva.

Autenticación JWT: Sistema de autenticación seguro basado en tokens (JSON Web Tokens).

Gestión de Contenido: Funcionalidades CRUD (Crear, Leer, Actualizar, Borrar) para películas y reseñas.

Almacenamiento de Imágenes: Soporte para subida de portadas de películas.

Poblado de Datos Iniciales: La base de datos se puebla automáticamente con películas de ejemplo al ejecutar las migraciones.

Arquitectura del Proyecto

El proyecto está organizado en dos carpetas principales:

uanfilms-backend: Contiene el proyecto de Django.

uanfilms-frontend: Contiene la aplicación de React.

🚀 Guía de Instalación y Ejecución Local

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

Prerrequisitos

Asegúrate de tener instalados los siguientes programas:

Python 3.10+ y pip.

Node.js 16+ y npm.

Git.

Un servidor de base de datos MySQL.

Paso 1: Clonar el Repositorio

Abre tu terminal y clona este repositorio:


git clone https://github.com/DanAHerrer/UANFilmsLocal.git
Paso 2: Configuración del Backend (Django)

Navega a la carpeta del backend:

cd uanfilms-backend



Instala las dependencias de Python:


pip install -r requirements.txt

Configura la Base de Datos MySQL:

Abre tu cliente de MySQL y crea una nueva base de datos.


CREATE DATABASE uanfilms_db;

Configura las variables de entorno:

En la raíz de la carpeta uanfilms-backend, crea o edita un archivo llamado .env.

Copia y pega el siguiente contenido, reemplazando los valores con tus propias credenciales de MySQL.

code
Env
download
content_copy
expand_less
# Archivo .env
SECRET_KEY='tu-secret-key-aqui' # Puedes generar una nueva o usar la del proyecto
DEBUG=True

DATABASE_NAME=uanfilms_db
DATABASE_USER=root # O tu usuario de MySQL
DATABASE_PASSWORD=tu_contraseña_de_mysql
DATABASE_HOST=localhost
DATABASE_PORT=3306

Aplica las migraciones y puebla la base de datos:

Este comando creará las tablas y ejecutará la migración de datos para añadir las películas iniciales.


python manage.py migrate

Crea un superusuario para acceder al panel de administración:


python manage.py createsuperuser

Inicia el servidor del backend:

python manage.py runserver

El servidor de Django estará funcionando en http://localhost:8000.

Paso 3: Configuración del Frontend (React)

Abre una nueva terminal y navega a la carpeta del frontend:
Desde la consola de tu computador 

cd uanfilms-frontend

Instala las dependencias de Node.js:

npm install

Inicia la aplicación de React:
npm start
La aplicación de React se abrirá automáticamente en tu navegador en `http://localhost:3000`.


Despliegue en Azure

Este proyecto está preparado para ser desplegado en Azure. La configuración en settings.py detecta automáticamente el entorno de Azure y utiliza los servicios correspondientes (Azure Database for MySQL, Azure Blob Storage). El despliegue se automatiza a través de un pipeline de CI/CD definido en el archivo .github/workflows/main_...yml.
