import requests

KEY="xxxxxxxx"
URL_BASE="https://imdb-api.com"
ENDPOINT=f"en/API/Ratings/{KEY}"

id = input("Introduce un id de pelicula: ")

r = requests.get(f"{URL_BASE}/{ENDPOINT}/{id}")
if r.status_code == 200:
    rating_json = r.json()
    print(rating_json)

    if rating_json["imDb"]:
        imdb = float(rating_json["imDb"])
    else:
        imdb = -1

    if imdb > 9:
        print("La película es una obra maestra")
    elif imdb > 8:
        print("La película es muy buena")
    elif imdb > 7:
        print("La película es buena")
    elif imdb > 6:
        print("La película es entretenida")
    elif imdb > 5:
        print("La película es más bien mala")
    elif imdb == -1:
        print("La película no tiene rating en IMDB")
    else:
        print("La película es muy mala. Mejor no verla.")
else:
    print("Error en la API")
    print(r)

