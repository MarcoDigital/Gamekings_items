import requests
from bs4 import BeautifulSoup
import time
import webbrowser


url = "https://www.gamekings.tv"
interval = 60  # Interval in seconden voor website check
listtitels = []
listartikels = []
i = 1


class bcolors:
    groen = '\u001b[38;5;2m'
    reset = '\033[0m'


def gen():
    """Haalt titels en video's op uit de website"""
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    titels = soup.find_all("a", class_="slider__link")
    artikels = soup.find_all("a", class_="slider__link")
    for titel in titels:
        lijst = titel.get_text()
        trim = lijst.strip()
        listtitels.append(trim)

    for artikel in artikels:
        lijst = artikel.get("href")
        listartikels.append(lijst)

    return lijst  # Retour snapshot voor vergelijker()


def printer(listtitels, listartikels):
    """Print de laatste 10 artikelen op de console"""
    print("\n")
    for i, (titel, link) in enumerate(zip(listtitels, listartikels), 1):
        print(f"{i} {titel}\n{link}\n")


def vergelijker(val1, val2):
    """Vergelijkt de eerste en tweede iteratie van gen()"""
    if waarde1 == waarde2:
        listtitels.clear()  # Lijsten leegmaken
        listartikels.clear()  # Lijsten leegmaken
    else:
        listtitels.clear()
        listartikels.clear()
        gen()
        printer(listtitels, listartikels)
        notify()


def notify():
    """Notificeert de gebruiker"""
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(
        f"\n{bcolors.groen}{current_time}: Er is een nieuwe Gamekings video beschikbaar. De nieuwe lijst is hierboven.{bcolors.reset}")
    print(f"{stars}\n{message}")
    print(
        f"Ik check elke {interval} seconden. Je kan dit scherm minimaliseren.")
    webbrowser.open(url)  # Opent de browser bij nieuwe video.
    listtitels.clear()
    listartikels.clear()


if __name__ == "__main__":
    while True:
        waarde1 = gen()
        if i == 1:
            printer(listtitels, listartikels)
            message = "Ik laat je automatisch weten wanneer er weer een nieuwe GK video beschikbaar is..."
            stars = len(message) * "-"
            print(f"{stars}\n{message}")
            print(
                f"Ik check elke {interval} seconden. Je kan dit scherm minimaliseren.")
            i += 1
        else:
            pass
        time.sleep(interval)
        waarde2 = gen()
        vergelijker(waarde1, waarde2)
