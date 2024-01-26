#powitanie użytkownika 
print("Oto sito Eratostenesa, algortym wyznaczanie liczb pierwszych mniejszych od danej liczby. ")

#pobranie liczby
while True:
  try:
    n = int(input("Podaj liczbę n: "))

    L = [] #lista do przechowania liczb
    for number in range(2,n):
      L.append(number) #dodanie wszystkich liczb do listy
      for i in L:
        for j in L: #podwójna pętla w celu sprawdzenia podzielności
          if j % i == 0 and i != j: #wykrycie liczby złożonej
            L.remove(j) #usunięcie liczby złożonej
    print(L)
    
  #błąd nieprawidłowych danych
  except ValueError:
    print("Wprowadzono nieprawidłowe dane. Wpisz liczbę.")