# Usando la API con curl

He usado la API de https://imdb-api.com/ para extraer información sobre películas.

## Búsqueda de película

Por lo general el primer resultado de la lista es el más relevante.

```
export key="XXXXXXX"
export busqueda="The%20Matrix%201999"
curl -s https://imdb-api.com/en/API/SearchMovie/$key/$busqueda | json_pp
{
   "errorMessage" : "",
   "expression" : "The Matrix 1999",
   "results" : [
      {
         "description" : "(1999)",
         "id" : "tt0133093",
         "image" : "https://imdb-api.com/images/original/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_Ratio0.6800_AL_.jpg",
         "resultType" : "Title",
         "title" : "The Matrix"
      },
      {
         "description" : "(1999 TV Movie)",
         "id" : "tt0365467",
         "image" : "https://imdb-api.com/images/original/MV5BZjJjMTg5MTEtMDkwMy00ZjUyLTg5ODYtMmNmY2ZiNGVlZTdjXkEyXkFqcGdeQXVyODA1NjQ0OTY@._V1_Ratio0.6800_AL_.jpg",
         "resultType" : "Title",
         "title" : "Making 'The Matrix'"
      },
      {
         "description" : "(1999 Video)",
         "id" : "tt5319308",
         "image" : "https://imdb-api.com/images/original/MV5BNDUzOWFjOWUtZmM5NS00M2QyLWFkYzQtOTIwZDg2ZGMwYzM5XkEyXkFqcGdeQXVyODA1NjQ0OTY@._V1_Ratio0.6800_AL_.jpg",
         "resultType" : "Title",
         "title" : "The Matrix: Follow the White Rabbit"
      },
      {
         "description" : "(1999 TV Movie)",
         "id" : "tt0438231",
         "image" : "https://imdb-api.com/images/original/nopicture.jpg",
         "resultType" : "Title",
         "title" : "The Matrix: The Movie Special"
      }
   ],
   "searchType" : "Movie"
}
```

## Búsqueda de rating de la película

Una vez conocido el 'id' de la película, podemos buscar su rating.
Siguiendo el ejemplo anterior, id tt0133093

```
export key="XXXXXXX"
export id="tt0133093"
curl -s https://imdb-api.com/en/API/Ratings/$key/$id | json_pp
{
   "errorMessage" : "",
   "filmAffinity" : "7.9",
   "fullTitle" : "The Matrix (1999)",
   "imDb" : "8.7",
   "imDbId" : "tt0133093",
   "metacritic" : "73",
   "rottenTomatoes" : "88",
   "theMovieDb" : "8.2",
   "title" : "The Matrix",
   "type" : "Movie",
   "year" : "1999"
}
```

## Obtener trailer de la película

Nos interesa el 'link' al trailer de la película, o incluso el 'linkEmbed' para nuestro servicio web.

```
export key="XXXXXXX"
export id="tt0133093"
curl -s https://imdb-api.com/en/API/Trailer/$key/$id | json_pp
{
   "errorMessage" : "",
   "fullTitle" : "The Matrix (1999)",
   "imDbId" : "tt0133093",
   "link" : "https://www.imdb.com/video/vi1032782617",
   "linkEmbed" : "https://www.imdb.com/video/imdb/vi1032782617/imdb/embed",
   "thumbnailUrl" : "https://m.media-amazon.com/images/M/MV5BNDQ4NTRmN2ItYjgzMS00MzY3LWEwNmYtYmE2ODllZDdhNGI1XkEyXkFqcGdeQXdvbmtpbQ@@._V1_.jpg",
   "title" : "The Matrix",
   "type" : "Movie",
   "uploadDate" : null,
   "videoDescription" : "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers. ",
   "videoId" : "vi1032782617",
   "videoTitle" : "Theatrical Trailer",
   "year" : "1999"
}
```
