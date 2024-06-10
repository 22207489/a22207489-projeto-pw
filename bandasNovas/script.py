from django.db import transaction
import json
from bandasNovas.models import Banda, Album, Musica

# Function to download cover image and return a File object

# Clear existing data
Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

# Load data from JSON file
with open('bandasNovas/json/bandas.json') as f:
    json_data = json.load(f)

# Create objects from JSON data
with transaction.atomic():
    for band_data in json_data['bands']:
        band_obj = Banda.objects.create(
            nome=band_data['name'],
            nacionalidade_da_banda=band_data['nationality']
        )
        for album_data in band_data['albums']:
            # Download cover image if available
            album_obj = Album.objects.create(
                titulo=album_data['title'],
                ano_de_lancamento=album_data['year'],
                banda=band_obj,
            )
            # Create and associate music objects with the album
            for song_data in album_data['songs']:
                Musica.objects.create(
                    nome=song_data['name'],
                    duracao=song_data['duration'],
                    link=song_data.get('link', ''),  # If link is not available, set it to empty string
                    album=album_obj
                )
