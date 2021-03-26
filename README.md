# Gamekings Update Checker v1.0

Dit script checkt met een interval (standaard 60 seconden) of er een nieuwe video op gamekings.tv beschikbaar is. 
Voor gebruik moet je eerst Python 3.x installeren en de module beautifulsoup4.

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

Let op: Zet de interval niet lager dan 60 seconden om de servers van Gamekings niet te belasten.

Terminal view:

<img src="https://i.imgur.com/Q3eUFqa.png" width="500">

Succes view:

<img src="https://i.imgur.com/6OWMQop.png" width="500">
