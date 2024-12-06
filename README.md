# 🐾Pokédex - Romina

## ¡Bienvenido a Pokédex - Romina! 🎮
Este proyecto es una aplicación web desarrollada en Django que utiliza la API pública PokéAPI. Con esta Pokédex, puedes:

- Explorar información detallada de Pokémon.
- Buscar por nombre o ID.
- Visualizar cadenas evolutivas.

## 🚀 Requisitos

Antes de empezar, asegúrate de tener instalados los siguientes componentes:
- Python 3.7+ (Seleccionar PATH en la instalación)
- pip (administrador de paquetes de Python)
- Virtualenv ( Realizar pip install virtualenv luego de instalar Python)

## 🔧 Instalación

   Clona este repositorio:

- git clone https://github.com/Miinaro/PokeDex-Romina

O descarga el proyecto desde Code > Download ZIP.

Abre la terminal (CMD o Command Prompt) y dirígete a la carpeta del proyecto:

- cd PokeDex-Romina

Crea un entorno virtual:

- python -m venv venv

Activa el entorno virtual:

- venv\Scripts\activate

Instala las dependencias necesarias:

- python.exe -m pip install -r requeriments.txt

Inicia el servidor:

- python manage.py runserver

Luego abre tu navegador y accede a: http://127.0.0.1:8000

## 🎨 Decisiones de Diseño

Este proyecto fue desarrollado con:

- Django para la lógica del backend.
- HTML y CSS para la interfaz.

*Razones de elección:*

- Experiencia previa con estas tecnologías.
- Plazo limitado para completar el desarrollo.
- Eficiencia al trabajar con herramientas conocidas.

## ✨ Mejoras Futuras

- Sugerencias de búsqueda: 
   Actualmente, al buscar un Pokémon, se genera una lista con todos los nombres que incluyen las letras ingresadas (por ejemplo, "k"). Optimizar este sistema para mejorar la    experiencia del usuario sería ideal.

- Sprites faltantes: 
   Algunos sprites (especialmente los últimos Pokémon) no se cargan correctamente. Esto requiere una investigación adicional para resolver el problema.


- Interfaz más dinámica: 
    Tomando la inspiracion de [Pokemon.Gameinfo](https://pokemon.gameinfo.io/es), sería excelente tener una lista completa de Pokémon en la página inicial. Al buscar, el         Pokémon debería resaltarse dinámicamente, por razones de requerimientos se dejo la idea.

- Animaciones en sprites: 
    Mejorar la estética del índice utilizando sprites animados como los que se ven en [Pokemon Concept](https://www.behance.net/gallery/113562309/Pokemon-Pokedex-Website-Redesign-Concept#)
