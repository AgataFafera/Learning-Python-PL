import math 

intro = """ By wybrać dodawanie, wpisz D. By wybrać odejmowanie, wpisz O. By wybrać mnożenie, wpisz M. 
By wybrać dzielenie, wpisz DZ. By wybrać potęgowanie, wpisz P. By wybrać sinus, wpisz SIN. By wybrać cosinus, wpisz
COS. By wybrać tangens, wpisz TAN. """

print(intro)

def dodawanie(x,y): 
    z = x + y 
    print(z)
    

def odejmowanie(x,y): 
    z = x - y 
    print(z) 

def mnozenie(x,y): 
    z = x * y 
    print(z) 

def dzielenie(x,y): 
    try:
        z = x / y 
        print(z)
    except ZeroDivisionError as e:
        print("Nie można dzielić przez zero!")
    
def potega(x,y): 
    z = x ** y 
    print(z) 

def sinus(x): 
    z = math.sin(x) 
    print(z) 

def cosinus(x): 
    z = math.cos(x)
    print(z) 

def tangens(x): 
    z = math.tan(x)
    print(z) 
    
while True:
    wybor = input("Wybierz swoje działanie: ")
    if wybor.lower() in ['d', 'o', 'm', 'dz', 'p', 'sin', 'cos', 'tan']:
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

if wybor.lower() == 'd': 
    try:
        a = int(input('Wpisz pierwszą liczbę'))
        b = int(input('Wpisz drugą liczbę'))
        dodawanie(a,b)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
    
elif wybor.lower() == 'o': 
    try:
        a = int(input('Wpisz liczbę, od której chcesz odjąć'))
        b = int(input('Wpisz liczbę, którą chcesz odjąc od pierwszej'))
        odejmowanie(a,b)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
    
elif wybor.lower() == 'm': 
    try:
        a = int(input('Wpisz pierwszą liczbę'))
        b = int(input('Wpisz drugą liczbę'))
        mnozenie(a,b)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
    
elif wybor.lower() == 'dz': 
    try:
        a = int(input('Wpisz liczbę, którą chcesz dzielić'))
        b = int(input('Wpisz liczbę, przez którą chcesz dzielić'))
        dzielenie(a,b)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
    
elif wybor.lower() == 'p': 
    try:
        a = int(input('Wpisz podstawę potęgi'))
        b = int(input('Wpisz potęgę'))
        potega(a,b)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
    
elif wybor.lower() == 'sin': 
    try:
        a = float(input('Wpisz liczbę'))
        sinus(a)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
    
elif wybor.lower() == 'cos': 
    try:
        a = float(input('Wpisz liczbę'))
        cosinus(a)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
    
else wybor.lower() == 'tan': 
    try:
        a = float(input('Wpisz liczbę'))
        tangens(a)
    except ValueError as e:
        print("Podaj odpowiednią wartość liczbową!")
