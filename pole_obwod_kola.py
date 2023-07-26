import math

def pole_obwod(r):
    if r <= 0:
        return "promień musi być większy od 0."
    else:
        p = math.pi * r**2
        l = 2 * math.pi * r
        return f'Pole twojego koła to: {p}, obwód to: {l}.'

while True:
    try:
        podaj_r = float(input("Podaj promień koła: "))
        wynik = pole_obwod(podaj_r)
        print(wynik)
        break 
    except ValueError:
        print("Wprowadzono nieprawidłowe dane. Wprowadź liczbę dodatnią jako promień koła.")
