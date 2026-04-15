# gestor_de_tareas_py
Aplicación de consola en Python para la gestión de tareas, que permite agregar, listar, completar y eliminar tareas con almacenamiento persistente en un archivo JSON.
Gestor de Tareas - Python



Aplicación de consola desarrollada en Python para la gestión de tareas, con almacenamiento persistente en archivo JSON.

Descripción
Este proyecto permite crear, visualizar, completar y eliminar tareas desde una interfaz por consola. Los datos se almacenan localmente en un archivo tasks.json, lo que permite mantener la información entre ejecuciones.

Funcionalidades
Agregar nuevas tareas
Listar tareas existentes
Marcar tareas como completadas
Eliminar tareas
Persistencia de datos en archivo JSON
Tecnologías utilizadas
Python 3
JSON (para almacenamiento de datos)
Estructura del proyecto
Gestor de tareas/
│── app.py
│── tasks.json
│── run.bat
│── README.md
Requisitos
Tener Python 3 instalado
Sistema operativo Windows (para ejecución con archivo .bat)
Ejecución
Opción 1: Desde consola
Ubicarse en la carpeta del proyecto y ejecutar:

python app.py
Opción 2: Usando archivo .bat
Hacer doble click en el archivo run.bat.

Importante: Es necesario configurar correctamente la ruta dentro del archivo .bat para que apunte a la ubicación donde se encuentran los archivos del proyecto.

Ejemplo:

cd /d "C:\ruta\al\proyecto\Gestor de tareas"
Dentro de esa carpeta deben encontrarse los siguientes archivos:

app.py
tasks.json
Archivo de datos
El archivo tasks.json se utiliza para almacenar las tareas. Debe contener inicialmente una lista vacía:

[]
Objetivo del proyecto
Este proyecto fue desarrollado con fines educativos para reforzar conceptos fundamentales como:

Manejo de archivos
Estructuras de datos
Organización de código
Lógica de programación
Autor
Ramiro Silva
