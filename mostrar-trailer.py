import requests

KEY="xxxxxx"
URL_BASE="https://imdb-api.com"
ENDPOINT=f"en/API/Trailer/{KEY}"

id = input("Introduce un id de pelicula: ")

r = requests.get(f"{URL_BASE}/{ENDPOINT}/{id}")
if r.status_code == 200:
    trailer_json = r.json()
    print(trailer_json)

    if trailer_json["link"]:
        link_manual = trailer_json["link"]
        print(f"El enlace manual al trailer es {link_manual}")
    if trailer_json["linkEmbed"]:
        link_embed = trailer_json["linkEmbed"]
        print(f"El enlace para la template es {link_embed}")
else:
    print("Error en la API")
    print(r)

