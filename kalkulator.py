import math

intro = """ By wybrać dodawanie, wpisz D. By wybrać odejmowanie, wpisz O. By wybrać mnożenie, wpisz M. 
By wybrać dzielenie, wpisz DZ. By wybrać potęgowanie, wpisz P. By wybrać sinus, wpisz SIN. By wybrać cosinus, wpisz
COS. By wybrać tangens, wpisz TAN. """

print(intro)


def dodawanie(x, y):
    z = x + y
    print(z)


def odejmowanie(x, y):
    z = x - y
    print(z)


def mnozenie(x, y):
    z = x * y
    print(z)


def dzielenie(x, y):
    z = x / y
    print(z)


def potega(x, y):
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

if wybor == 'd' or wybor == 'D':
    a = int(input('Wpisz pierwszą liczbę'))
    b = int(input('Wpisz drugą liczbę'))
    dodawanie(a, b)

elif wybor == 'o' or wybor == 'O':
    a = int(input('Wpisz liczbę, od której chcesz odjąć'))
    b = int(input('Wpisz liczbę, którą chcesz odjąc od pierwszej'))
    odejmowanie(a, b)

elif wybor == 'm' or wybor == 'M':
    a = int(input('Wpisz pierwszą liczbę'))
    b = int(input('Wpisz drugą liczbę'))
    mnozenie(a, b)

elif wybor == 'Dz' or wybor == 'DZ' or wybor == 'dz' or wybor == 'dZ':
    a = int(input('Wpisz liczbę, którą chcesz dzielić'))
    b = int(input('Wpisz liczbę, przez którą chcesz dzielić'))
    dzielenie(a, b)

elif wybor == 'p' or wybor == 'P':
    a = int(input('Wpisz podstawę potęgi'))
    b = int(input('Wpisz potęgę'))
    potega(a, b)

elif wybor == 'sin' or wybor == 'SIN' or wybor == 'Sin':
    a = int(input('Wpisz liczbę'))
    sinus(a)

elif wybor == 'COS' or wybor == 'cos' or wybor == 'Cos':
    a = int(input('Wpisz liczbę'))
    cosinus(a)

elif wybor == 'tan' or wybor == 'TAN' or wybor == 'Tan':
    a = int(input('Wpisz liczbę'))
    tangens(a)

else:
    print('Wpisz poprawny tekst')
