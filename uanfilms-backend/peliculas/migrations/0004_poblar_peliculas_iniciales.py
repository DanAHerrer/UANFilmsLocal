from django.db import migrations
from django.core.files import File
import hashlib
import os


SEED_IMAGES_DIR = os.path.join('peliculas', 'seed_images')

PELICULAS_INICIALES = [
    {
        "titulo": "Spider-Man: Across the Spider-Verse",
        "sinopsis": "Miles Morales es catapultado a través del Multiverso...",
        "ano_lanzamiento": 2023,
        "director": "Joaquim Dos Santos",
        "genero": "Animación, Acción, Aventura",
        "elenco": "Shameik Moore, Hailee Steinfeld, Oscar Isaac",
        "portada_filename": "spider-man-across-the-spider-verse.jpg"
    },
    {
        "titulo": "Inception",
        "sinopsis": "A un ladrón que roba secretos corporativos...",
        "ano_lanzamiento": 2010,
        "director": "Christopher Nolan",
        "genero": "Ciencia Ficción, Acción, Thriller",
        "elenco": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
        "portada_filename": "inception.jpg"
    },
    {
        "titulo": "The Shawshank Redemption",
        "sinopsis": "Dos hombres encarcelados establecen un vínculo...",
        "ano_lanzamiento": 1994,
        "director": "Frank Darabont",
        "genero": "Drama",
        "elenco": "Tim Robbins, Morgan Freeman, Bob Gunton",
        "portada_filename": "the-shawshank-redemption.jpg"
    },
    {
        "titulo": "Parasite",
        "sinopsis": "La familia Kim, sin trabajo, se interesa por la rica familia Park...",
        "ano_lanzamiento": 2019,
        "director": "Bong Joon-ho",
        "genero": "Comedia Negra, Thriller",
        "elenco": "Song Kang-ho, Choi Woo-shik, Park So-dam",
        "portada_filename": "parasite.jpg"
    },
    {
        "titulo": "Pulp Fiction",
        "sinopsis": "Las vidas de dos asesinos a sueldo, un boxeador, la esposa de un gángster y una pareja de ladrones se entrelazan...",
        "ano_lanzamiento": 1994,
        "director": "Quentin Tarantino",
        "genero": "Crimen, Drama",
        "elenco": "John Travolta, Uma Thurman, Samuel L. Jackson",
        "portada_filename": "pulp-fiction.jpg"
    },
    {
        "titulo": "Mad Max: Fury Road",
        "sinopsis": "En un futuro post-apocalíptico, una mujer se rebela contra un tirano con la ayuda de un vagabundo...",
        "ano_lanzamiento": 2015,
        "director": "George Miller",
        "genero": "Acción, Ciencia Ficción, Aventura",
        "elenco": "Tom Hardy, Charlize Theron, Nicholas Hoult",
        "portada_filename": "mad-max-fury-road.jpg"
    }
]

def calcular_hash(titulo, ano):
    texto_a_hashear = f"{titulo.lower().replace(' ', '')}{ano}"
    return hashlib.sha256(texto_a_hashear.encode('utf-8')).hexdigest()

def crear_peliculas_iniciales(apps, schema_editor):
    Pelicula = apps.get_model('peliculas', 'Pelicula')

    for pelicula_data in PELICULAS_INICIALES:
        if not Pelicula.objects.filter(titulo=pelicula_data["titulo"], ano_lanzamiento=pelicula_data["ano_lanzamiento"]).exists():
            
            pelicula = Pelicula(
                titulo=pelicula_data["titulo"],
                sinopsis=pelicula_data["sinopsis"],
                ano_lanzamiento=pelicula_data["ano_lanzamiento"],
                director=pelicula_data["director"],
                genero=pelicula_data["genero"],
                elenco=pelicula_data["elenco"],
                codigo_hash=calcular_hash(pelicula_data["titulo"], pelicula_data["ano_lanzamiento"])
            )

          
            portada_path = os.path.join(SEED_IMAGES_DIR, pelicula_data["portada_filename"])
            
            
            if os.path.exists(portada_path):
               
                with open(portada_path, 'rb') as f:
                   
                    pelicula.portada.save(pelicula_data["portada_filename"], File(f), save=False)
            
            pelicula.save()


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_pelicula_portada'), 
    ]

    operations = [
        migrations.RunPython(crear_peliculas_iniciales),
    ]