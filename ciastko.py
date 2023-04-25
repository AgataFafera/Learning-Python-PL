import random

szczesliwy_numer = random.randint(1, 500)

wrozba_numer = random.randint(1, 10)

planeta_numer = random.randint(1, 7)

wrozba_tekst = ''

planeta_tekst = ''

if wrozba_numer == 1:
    wrozba_tekst = "Czeka cię udany dzień!"

if wrozba_numer == 2:
    wrozba_tekst = "Przygotuj się na kłopoty!"

if wrozba_numer == 3:
    wrozba_tekst = "Ktoś chce Cię oszukać!"

if wrozba_numer == 4:
    wrozba_tekst = "Ktoś czeka na Ciebie, nie zwlekaj!"

if wrozba_numer == 5:
    wrozba_tekst = "Zadbaj o siebie dzisiaj!"

if wrozba_numer == 6:
    wrozba_tekst = "Będzie ciężko, ale czeka Cię nagroda!"

if wrozba_numer == 7:
    wrozba_tekst = "Spodziewaj się niespodzianki!"

if wrozba_numer == 8:
    wrozba_tekst = "Nie poddawaj się pomimo początkowych trudności!"

if wrozba_numer == 9:
    wrozba_tekst = "Nie odkładaj tego na potem!"

if wrozba_numer == 10:
    wrozba_tekst = "Nie ma tego złego, co by na dobre nie wyszło!"

if planeta_numer == 1:
    planeta_tekst = "Merkury"

if planeta_numer == 2:
    planeta_tekst = "Wenus"

if planeta_numer == 3:
    planeta_tekst = "Mars"

if planeta_numer == 4:
    planeta_tekst = "Jowisz"

if planeta_numer == 5:
    planeta_tekst = "Saturn"

if planeta_numer == 6:
    planeta_tekst = "Uran"

if planeta_numer == 7:
    planeta_tekst = "Neptun"

print(
    f"Twoja wróżba na dziś to: {wrozba_tekst} Twój szczęśliwy numer to {szczesliwy_numer}. Twoja szczęśliwa planeta to {planeta_tekst}. ")