import math

#powitanie
print("Ten program umożliwi ci sprawdzenie, z jaką prędkością powinna poruszać się satelita, aby utrzymać się na danej orbicie.")

try:
    #pobranie od użytkownika promienia orbity
    r = int(input("Podaj, w jakiej odległości od środka Ziemi znajduje się satelita [km]: "))
    r = r*1000 #zmiana na metry
    
    #masa Ziemi w kg
    M = 6e24
    
    #stała grawitacji w [N*m^2/kg^2]
    G = 6.67e-11
    
    #obliczenie prędkości orbitalnej w m/s
    v = math.sqrt(G*M/r)

    #odpowiedź dla użytkownika
    print(f"Satelita powinna poruszać z prędkością v wynoszącą {v} m/s")

#błąd nieprawidłowej wartości
except ValueError:
    print("Podano nieprawidłowe dane. Wprowadź liczbę.")