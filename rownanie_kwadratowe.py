import math

def rownanie_kwadratowe(a, b, c): 
    if a == 0:
        return "to nie jest równanie kwadratowe, współczynnik a musi być różny od 0."
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "delta mniejsza od 0, brak rozwiązań w zbiorze liczb rzeczywistych."
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return x1, x2

while True:
    try:
        wspol_a = float(input("Podaj współczynnik a: "))
        wspol_b = float(input("Podaj współczynnik b: "))
        wspol_c = float(input("Podaj współczynnik c: "))
        
        wynik = rownanie_kwadratowe(wspol_a, wspol_b, wspol_c)
        print(f'Wynik twojego równania kwadratowego to: {wynik}.')
        
    except ValueError:
        print("Wprowadzono nieprawidłowe dane. Współczynniki a, b i c muszą być liczbami.")
