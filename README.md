# PokeDex - Romina

Este proyecto es una aplicación básica de Pokédex desarrollada en Django, que consume la API pública [PokéAPI](https://pokeapi.co/). Permite a los usuarios explorar detalles de Pokémon, buscar por nombre o ID, y visualizar cadenas evolutivas.

## Requisitos

Antes de empezar, asegúrate de tener instalado:

- Python 3.8+
- pip (administrador de paquetes de Python)
- Virtualenv 

## Instalación

1. Clona este repositorio:

   git clone https://github.com/Miinaro/PokeDex-Romina

O tambien se puede descargar el archivo en Code > Download Zip

2. Abrir CMD o Command Prompt (Win + R)
     2.a Reridigirce a la carpeta donde se encuentre el proyecto
        ...\PokeDex-Romina>

3. Crear un Entorno virtual con el siguiente comando:
     python -m venv venv

4. Activar entorno virtual
     venv\Scripts\activate

5. Instalar los requerimientos necesarios
     python.exe -m pip install -r requeriments.txt

6. Iniciar proyecto
     python manage.py runserver

     Abre tu navegador y accede a: http://127.0.0.1:8000

## Decisiones de Diseño

El proyecto fue desarrollado utilizando Django, HTML y CSS debido a:
    - Experiencia previa con estas tecnologías.
    - Plazo limitado para completar la tarea.
    - Mayor eficiencia trabajando con herramientas conocidas.
    
## Cosas ha mejorar
Sugerencias de búsqueda:
    Actualmente, si no se escribe el nombre completo de un Pokémon, se genera una lista de sugerencias con todos los nombres que incluyen la letra ingresada (por ejemplo, "k"). Optimizar esta funcionalidad sería ideal.

Sprites faltantes:
    Algunos sprites (especialmente los últimos Pokémon) no se cargan correctamente. Esto requiere una investigación adicional para resolver el problema.

Interfaz más dinámica:
    Tomando la inspiracion de [Pokemon.Gameinfo](https://pokemon.gameinfo.io/es), sería excelente tener una lista completa de Pokémon en la página inicial. Al buscar, el Pokémon debería resaltarse dinámicamente, por razones de requerimientos se dejo la idea.

Animaciones en sprites:
    Mejorar la estética del índice utilizando sprites animados como los que se ven en [Pokemon Concept](https://www.behance.net/gallery/113562309/Pokemon-Pokedex-Website-Redesign-Concept#)





