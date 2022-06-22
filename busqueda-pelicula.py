import requests
import urllib

KEY="xxxxxxx"
URL_BASE="https://imdb-api.com"
ENDPOINT=f"en/API/SearchMovie/{KEY}"

busqueda = input("Introduce una expresión de búsqueda: ")

# Para cambiar los espacios a %20
busqueda_codificada = urllib.parse.quote(busqueda)

r = requests.get(f"{URL_BASE}/{ENDPOINT}/{busqueda_codificada}")
if r.status_code == 200:
    busqueda_json = r.json()
    print(busqueda_json)

    # la más relevante suele ser la primera
    for pelicula in busqueda_json["results"]:
        id = pelicula["id"]
        print(f"El id de la pelicula es: {id}")
        break

else:
    print("Error en la API")
    print(r)

