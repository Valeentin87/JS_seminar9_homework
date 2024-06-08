# с помощью данного скрипта получаем html код страницы с грибами
from bs4 import BeautifulSoup
import requests

url1 = "https://griby.org.ua/griby/osnovnye-griby"
url2 = "https://griby.org.ua/griby/samye-opasnye-yadovitye-griby/#google_vignette"
# response = requests.get(url)
# print(response)

def make_file(file_name: str, url):
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    response = requests.get(url, headers=headers)
    #print(response.text)

    with open(f'{file_name}', 'w') as file:
        file.write(response.text)

make_file("edible_mushrooms.html", url1)
make_file("poisonous_mushrooms.html", url2)

