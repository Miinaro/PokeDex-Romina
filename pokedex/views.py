import requests
import aiohttp
import asyncio
from django.shortcuts import render
from django.core.paginator import Paginator

async def fetch_pokemon_details(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_all_pokemon_details(pokemons):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_pokemon_details(session, pokemon['url']) for pokemon in pokemons]
        return await asyncio.gather(*tasks)

def pokemon_list(request):
    # URL base de la API de Pokémon
    url = "https://pokeapi.co/api/v2/pokemon?limit=10277&offset=0"
    
    # Obtener el tipo de Pokémon filtrado desde la URL (si está presente)
    type_filter = request.GET.get('type', None)

    # Si hay un filtro por tipo, agregarlo a la URL de la API
    if type_filter:
        url = f"https://pokeapi.co/api/v2/type/{type_filter}"
    
    # Realizar la solicitud a la API
    response = requests.get(url)
    
    # Si no se filtra por tipo, obtenemos la lista completa de Pokémon
    if type_filter:
        pokemon_data = response.json()
        pokemons = pokemon_data['pokemon']
        pokemons = [pokemon['pokemon'] for pokemon in pokemons]  # Filtrar solo el objeto Pokémon
    else:
        pokemon_data = response.json()
        pokemons = pokemon_data['results']

    # Obtener el número de página de la URL (por defecto es 1)
    page_number = request.GET.get('page', 1)
    
    # Crear el paginador
    paginator = Paginator(pokemons, 14)  # Mostramos 14 Pokémon por página
    page_obj = paginator.get_page(page_number)
    
    # Obtener los detalles de los Pokémon para la página actual
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    detailed_pokemons_data = loop.run_until_complete(fetch_all_pokemon_details(page_obj.object_list))
    
    # Estructurar los detalles de los Pokémon para mostrar en la plantilla
    detailed_pokemons = [{
        'id': pokemon_details['id'],
        'name': pokemon_details['name'],
        'sprites': pokemon_details['sprites'],
        'types': [type['type']['name'] for type in pokemon_details['types']]
    } for pokemon_details in detailed_pokemons_data]

    return render(request, 'index.html', {'pokemons': detailed_pokemons, 'page_obj': page_obj, 'type_filter': type_filter})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '').lower()
        pokemon_data = None
        pokemon_suggestions = []

        if query:
            # Intentar buscar un Pokémon específico por nombre o ID
            try:
                url = f'https://pokeapi.co/api/v2/pokemon/{query}'
                response = requests.get(url)
                if response.status_code == 200:
                    pokemon_data = response.json()
            except Exception as e:
                print(f"Error al buscar el Pokémon: {e}")

            # Si no se encuentra un Pokémon específico, buscar sugerencias
            if not pokemon_data:
                try:
                    # Obtener lista de Pokémon desde la API
                    url = 'https://pokeapi.co/api/v2/pokemon?limit=10277'
                    response = requests.get(url)
                    if response.status_code == 200:
                        all_pokemon = response.json().get('results', [])
                        # Filtrar Pokémon cuyos nombres contengan el término de búsqueda
                        pokemon_suggestions = [
                            {'name': p['name'], 'url': p['url']}
                            for p in all_pokemon if query in p['name']
                        ]

                        # Obtener detalles de cada sugerencia (limitando a los primeros 10 para optimizar)
                        for suggestion in pokemon_suggestions[:10]:
                            detail_response = requests.get(suggestion['url'])
                            if detail_response.status_code == 200:
                                suggestion.update(detail_response.json())
                except Exception as e:
                    print(f"Error al buscar sugerencias: {e}")

        return render(
            request,
            'search.html',
            {
                'pokemon_data': pokemon_data,
                'query': query,
                'pokemon_suggestions': pokemon_suggestions
            }
        )

# Detalle de un Pokémon
def pokemon_detail(request, name):
    # Obtener datos básicos del Pokémon
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
    if response.status_code != 200:
        return render(request, 'pokemon_detail.html', {'error': 'Pokémon no encontrado'})
    
    pokemon_data = response.json()

    # Obtener datos de especie para acceder a la cadena evolutiva
    species_response = requests.get(pokemon_data['species']['url'])
    if species_response.status_code != 200:
        evolution_details = None
    else:
        species_data = species_response.json()
        
        # Obtener la cadena evolutiva
        evolution_chain_url = species_data['evolution_chain']['url']
        evolution_chain_response = requests.get(evolution_chain_url)
        if evolution_chain_response.status_code != 200:
            evolution_details = None
        else:
            evolution_chain_data = evolution_chain_response.json()
            
            # Extraer evoluciones
            evolution_details = []
            current_evolution = evolution_chain_data['chain']
            while current_evolution:
                evolution_name = current_evolution['species']['name']
                # Obtener el sprite del Pokémon
                evolution_pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{evolution_name}')
                if evolution_pokemon_response.status_code == 200:
                    evolution_pokemon_data = evolution_pokemon_response.json()
                    evolution_details.append({
                        'name': evolution_name,
                        'sprite': evolution_pokemon_data['sprites']['front_default']
                    })
                current_evolution = current_evolution['evolves_to'][0] if current_evolution['evolves_to'] else None

    # Pasar los datos al template
    context = {
        'pokemon_data': pokemon_data,
        'evolution_details': evolution_details
    }
    return render(request, 'pokemon_detail.html', context)