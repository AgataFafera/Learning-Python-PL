import matplotlib.pyplot as plt
import numpy as np  

#pobranie od użytkownika współczynników
while True:
  try:
    a = int(input('Podaj współczynnik a: '))
    b = int(input('Podaj współczynnik b: '))
    c = int(input('Podaj współczynnik c: '))

    #obliczenie delty
    delta = b**2 - 4*a*c

    #błąd dzielenia przez zero
    if a == 0:
            raise ZeroDivisionError("Współczynnik a nie może być równy zero.")

    #obliczenie wierzchołków paraboli
    p = -b/(2*a)
    q = -delta/(4*a)

    #stworzenie zakresu wartości x
    x_wartosci = np.linspace(-10, 10, 100)
    #wartości y na podstawie wzoru parabolii
    y_wartosci = a * x_wartosci**2 + b * x_wartosci + c

    #rysowanie wykresu
    plt.plot(x_wartosci, y_wartosci)
    plt.xlabel('Oś X') #nazwa osi X
    plt.ylabel('Oś Y') #nazwa osi Y
    plt.title('Wykres parabolii') #tytuł
    plt.grid() #siatka
    plt.plot(p, q, marker="o") #wierzchołek paraboli
    plt.show()
    break

  #błąd nieprawidłowych danych
  except ValueError:
    print("Wprowadzono nieprawidłowe dane. Współczynniki a, b i c muszą być liczbami.") 

    
  

