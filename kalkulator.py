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
    if y != 0:
        z = x / y 
        print(z)
    else: 
        print("Nie można dzielić przez zero")

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


    
wybor = input("Wybierz swoje działanie: ")

if wybor.lower() == 'd': 
    a = int(input('Wpisz pierwszą liczbę'))
    b = int(input('Wpisz drugą liczbę'))
    dodawanie(a,b)
    
elif wybor.lower() == 'o': 
    a = int(input('Wpisz liczbę, od której chcesz odjąć'))
    b = int(input('Wpisz liczbę, którą chcesz odjąc od pierwszej'))
    odejmowanie(a,b)
    
elif wybor.lower() == 'm': 
    a = int(input('Wpisz pierwszą liczbę'))
    b = int(input('Wpisz drugą liczbę'))
    mnozenie(a,b)
    
elif wybor.lower() == 'dz': 
    a = int(input('Wpisz liczbę, którą chcesz dzielić'))
    b = int(input('Wpisz liczbę, przez którą chcesz dzielić'))
    dzielenie(a,b)
    
elif wybor.lower() == 'p': 
    a = int(input('Wpisz podstawę potęgi'))
    b = int(input('Wpisz potęgę'))
    potega(a,b)
    
elif wybor.lower() == 'sin': 
    a = int(input('Wpisz liczbę'))
    sinus(a)
    
elif wybor.lower() == 'cos': 
    a = int(input('Wpisz liczbę'))
    cosinus(a)
    
elif wybor.lower() == 'tan': 
    a = int(input('Wpisz liczbę'))
    tangens(a)
    
else: 
    print('Wpisz poprawny tekst')
