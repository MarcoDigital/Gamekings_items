# Gamekings Update Checker v1.0

Dit script checkt met een interval (standaard 60 seconden) of er een nieuwe video op gamekings.tv beschikbaar is. 
Voor gebruik moet je eerst Python 3.x installeren en de module [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

Beautifulsoup4 installatie
```python
pip install beautifulsoup4
```

Het bestand kan je vanuit Terminal of Powershell met de volgende commandline opstarten:

macOS
```python
python3 gamekings_items.py
```

Win10
```python
py gamekings_items.py
```

Je kan de terminal vervolgens minimaliseren en op achtergrond laten draaien.

Als het programma een nieuwe upload ziet zal zal notify() functie aangesproken worden. Hierbij word de browser automatisch geopend.
Voel je vrij om je functionaliteit toe te voegen.

#### Update 28/3/2021
Email functionaliteit is toegevoegd onder de 'Email-notify' branche. Hiermee stuurt het programma je een email bij een nieuwe video. Je kan dit bijvoorbeeld 24/7 op een Raspberry Pi draaien. Dit werkt momenteel alleen met Gmail accounts. De gegevens worden **niet opgeslagen**. Gebruik je 2FA op je Gmail? Maak dan een app-specifiek wachtwoord aan voor je account en gebruik dit als wachtwoord. Als je logingegevens verkeerd zijn zal het programma dit laten weten.

<img src="https://i.imgur.com/UprHZWY.jpg" width="300">

### Let op
1. Dit programma geeft geen onbetaald toegang tot GK Premium items. [Support Gamekings!](https://www.gamekings.tv/get-premium/)
2. Zet de interval niet lager dan 60 seconden om de servers niet te belasten.
3. Dit programma is niet gemaakt door personeel van Blammo Media/Gamekings.


Terminal view:

<img src="https://i.imgur.com/Q3eUFqa.png" width="500">

Succes view:

<img src="https://i.imgur.com/6OWMQop.png" width="500">
