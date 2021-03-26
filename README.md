# Gamekings checker

Dit script checkt met een interval (standaard 60 seconden) of er een nieuwe video op gamekings.tv beschikbaar is. 
Voor gebruik moet je Python 3.x installeren en de module beautifulsoup4 installeren via pip. https://pypi.org/project/beautifulsoup4/

Het bestand kan je vanaf Terminal, Powershell of CMD uitvoeren met de volgende commandline:

python3 gamekings_items.py

Je kan de terminal vervolgens minimaliseren en op achtergrond laten draaien.

Als het programma een nieuwe upload ziet zal zal notify() aangesproken worden. Hierbij word de browser automatisch geopend.
Voel je vrij om je functionaliteit toe te voegen.

Let op: Zet de interval niet lager dan 60 seconden om de servers van Gamekings niet te belasten.

<img src="https://i.imgur.com/U6JOU4z.png" width="500">