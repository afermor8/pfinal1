# Descripción

Este proyecto usa la API de https://imdb-api.com para responder algunas de las
siguientes cuestiones:

 1. Busca una película. El usuario debe introducir la expresión de búsqueda.
 2. Calcula, según el rating de IMDB, si la película es buena para ver.
 3. Muestra el trailer en video.

El fichero `curl.md` muestra el uso básico de la API, cómo se usuarian los endpoints
y el formato JSON de salida. También muestra cómo se usa la `key` de autenticación
para esta API.

Para obtener la `key` de la API es necesario registrarse en la web https://imdb-api.com/ (es gratis).

Una vez hemos buscado la película, obtenemos su ID. Eso nos permite calcular el rating y decidir
si la película es buena o mala.

Finalmente, usando también el ID, podemos mostrar un enlace a un video o incluso obtener la URL
embed para un fichero HTML.

## Documentación de la API:

La documentación se encuentra en https://imdb-api.com/api

## Ejemplo

Buscamos una película:

```
python3 busqueda-pelicula.py 
Introduce una expresión de búsqueda: Sprited Away
{'searchType': 'Movie', 'expression': 'Sprited Away', 'results': [{'id': 'tt0245429', 'resultType': 'Title', 'image': 'https://imdb-api.com/images/original/MV5BMjlmZmI5MDctNDE2YS00YWE0LWE5ZWItZDBhYWQ0NTcxNWRhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_Ratio0.7273_AL_.jpg', 'title': 'Spirited Away', 'description': '(2001)'}, {'id': 'tt19048034', 'resultType': 'Title', 'image': 'https://imdb-api.com/images/original/MV5BMTE1YTFkODEtYTVkMC00NmUyLTk5NjktODdmMGQxOTMyZWE0XkEyXkFqcGdeQXVyOTgzNzQ2MjQ@._V1_Ratio1.0000_AL_.jpg', 'title': 'Spirited Away', 'description': '(2020) (Podcast Episode) - Season 2 | Episode 17 - The Cinema Sideshow (2019) (Podcast Series)'}], 'errorMessage': ''}
El id de la pelicula es: tt0245429
```

Calculamos la recomendación usando el rating de IMDB:

```
python3 calcular-rating.py 
Introduce un id de pelicula: tt0245429
{'imDbId': 'tt0245429', 'title': 'Spirited Away', 'fullTitle': 'Spirited Away (2001)', 'type': 'Movie', 'year': '2001', 'imDb': '8.6', 'metacritic': '96', 'theMovieDb': '8.5', 'rottenTomatoes': '97', 'filmAffinity': '8.1', 'errorMessage': ''}
La película es muy buena
```

Mostramos información sobre el trailer de la película:

```
python3 mostrar-trailer.py 
Introduce un id de pelicula: tt0245429
{'imDbId': 'tt0245429', 'title': 'Spirited Away', 'fullTitle': 'Spirited Away (2001)', 'type': 'Movie', 'year': '2001', 'videoId': 'vi3619684633', 'videoTitle': 'Spirited Away', 'videoDescription': 'CT #2A Post', 'thumbnailUrl': 'https://m.media-amazon.com/images/M/MV5BMzZjOWEyNTEtNjhmMC00YmZlLTkyMzAtM2Y5MzFjYmJlODIzXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg', 'uploadDate': None, 'link': 'https://www.imdb.com/video/vi3619684633', 'linkEmbed': 'https://www.imdb.com/video/imdb/vi3619684633/imdb/embed', 'errorMessage': ''}
El enlace manual al trailer es https://www.imdb.com/video/vi3619684633
El enlace para la template es https://www.imdb.com/video/imdb/vi3619684633/imdb/embed
```
