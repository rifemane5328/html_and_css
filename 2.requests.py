import requests


url = "https://akabab.github.io/superhero-api/api/all.json"

try:
    response = requests.get(url)
    if response.status_code == 200:
        heroes = response.json()
        for hero in heroes[:5]:
            print(f"Ім'я:{hero['name']}, здібності:{hero['powerstats']}")
    else:
        print(f"Помилка:{response.status_code}")


except Exception as e:
    print(f"Виникла помилка {e}")


