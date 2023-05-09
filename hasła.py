import random
import string

#intro generatora haseł
intro = ''' Witaj w generatorze haseł. 
Aby wygenerować hasło z samymi literami, wpisz L. 
Aby wygenerować hasło z samymi cyframi, wpisz C. 
Aby wygenerować hasło z literami i cyframi, wpisz LIC.
Aby wygenerować hasło z literami, cyframi i znakami specjalnymi, wpisz W.
Następnie podaj długość hasła.
'''

#funkcja dla hasła z samymi literami
def litery(dlugosc):
    znaki = string.ascii_letters
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
    return haslo

#funkcja dla hasła z literam i cyframi
def litery_cyfry(dlugosc):
    znaki = string.ascii_letters + string.digits
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
    return haslo
    
#funkcja dla hasła z samymi cyframi
def cyfry(dlugosc): 
    znaki = string.digits
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
    return haslo
    
#funkcja dla hasła z literami, cyframi i znakami specjalnymi 
def litery_cyfry_znaki(dlugosc):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
    return haslo

#zapytanie o długość hasła z uwzględnieniem błędu użytkownika
while True:
    try:    
        dlugosc = int(input("Podaj długość hasła: ")) 
        break
    except ValueError as e:
            print("Podaj odpowiednią wartość liczbową!")

#zapytanie o rodzaj hasła z uwzględnieniem błędu użytkownika
while True:
    wybor = input("Wybierz rodzaj hasła: ")
    if wybor.lower() in ['l', 'c', 'lic', 'w']:
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

#wywołanie odpowiedniej funkcji, zaprezentowanie hasła
if wybor.lower() == 'l':
    haslo = litery(dlugosc)
    print("Oto twoje hasło: ", haslo)
    
elif wybor.lower() == 'c':
    haslo = cyfry(dlugosc)
    print("Oto twoje hasło: ", haslo)
    
elif wybor.lower() == 'lic':
    haslo = litery_cyfry(dlugosc)
    print("Oto twoje hasło: ", haslo)
    
elif wybor.lower() == 'w':
    haslo = litery_cyfry_znaki(dlugosc)
    print("Oto twoje hasło: ", haslo)
