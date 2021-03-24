import requests
from bs4 import BeautifulSoup

url = "https://www.gamekings.tv"
req = requests.get(url).text
soup = BeautifulSoup(req, "html.parser")
titels = soup.find_all("a", class_="slider__link")
artikels = soup.find_all("a", class_="slider__link")

listtitels = []
listartikels = []


def gen(titels, artikels):
    for titel in titels:
        lijst = titel.get_text()
        trim = lijst.strip()
        listtitels.append(trim)

    for artikel in artikels:
        lijst = artikel.get("href")
        listartikels.append(lijst)


gen(titels, artikels)

for i, (titel, link) in enumerate(zip(listtitels, listartikels), 1):
    print(f"{i} {titel}\n{link}\n")
