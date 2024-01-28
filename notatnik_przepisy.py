import random

# Klasa służąca działaniu na przepisach będących obiektami
class Notatnik:
    def __init__(self, nazwa, czas_przygotowania, skladniki, wykonanie, ktory_posilek):
        self.nazwa = nazwa  # nazwa potrawy
        self.czas_przygotowania = czas_przygotowania  # czas gotowania w minutach
        self.skladniki = skladniki  # potrzebne składniki
        self.wykonanie = wykonanie  # opis wykonania
        self.ktory_posilek = ktory_posilek  # rodzaj: śniadanie, obiad, kolacja, deser

    def wyswietl_info(self):
            print(
                f"Nazwa potrawy: {self.nazwa}, czas przygotowania: {self.czas_przygotowania} minut, składniki: {self.skladniki},"
                f"wykonanie = {self.wykonanie}, rodzaj posiłku: {self.ktory_posilek}."
            )


# Powitanie użytkownika
    print("Witaj w Notatniku do gromadzenia przepisów i pomysłów na posiłki.")
    print("Co chcesz teraz zrobić?")


# Lista do przechowywania przepisów
potrawy = []

# Funkcja zdefiniowana w celu uniknęcia zagnieżdżonej pętli while True
# Dłuży do sprawdzenia, czy użytkownik chce dodać kolejną potrawę
def druga_petla(kolejna_potrawa):
    while True:
        kolejna_potrawa = input("Czy chcesz dodać kolejną potrawę? (tak/nie): ")
        if kolejna_potrawa.lower() == "tak":
            break
        elif kolejna_potrawa.lower() == "nie":
             break
        else:
            print("Nieprawidłowy wybór. Wpisz 'tak' lub 'nie'.")
            continue

# Pętla while True sprawiająca, że po każdej operacji na obiektach wraca się do pierwotnego zapytania
while True:

    # Prosty interfejs informujący, jakie działania są dostępne
    print(
        "By dodawać nowe potrawy, wpisz DODAJ.\n"
        "By usunąć potrawy, wpisz USUN.\n"
        "By obejrzeć wszystkie potrawy w notatniku, wpisz LISTA.\n"
        "By wylosować pomysł na dany posiłek, wpisz LOSUJ.\n"
        "By wyjść z programu, wpisz KONIEC."
    )

    wybor = input("WYBÓR: ") # Wybór działania

    if wybor.lower() == "dodaj": # Dodanie nowej potrawy
        nazwa = input("Podaj nazwę potrawy: ") # Dodanie nazwy potrawy
        czas_przygotowania = int(input("Podaj czas przygotowania w minutach: ")) # Dodanie czasu
        skladniki = input("Podaj składniki (oddzielone przecinkiem): ").split(", ") # Dodanie listy ze składnikami oddzielonymi przecinkami
        wykonanie = input("Podaj opis wykonania: ") # Dodanie opisu wykonania
        ktory_posilek = input("Podaj rodzaj posiłku (śniadanie, obiad, kolacja, desert): ") # Dodanie rodzaju posiłku (śniadanie, obiad, kolacja, deser)

        if ktory_posilek.lower() in ["śniadanie", "obiad", "kolacja", "deser"]: # Sprawdzenie poprawności wpisanego posiłku
            nowa_potrawa = Notatnik(nazwa, czas_przygotowania, skladniki, wykonanie, ktory_posilek) # Dodanie nowego obiektu do klasy
            potrawy.append(nowa_potrawa) # Dodanie obiektu do utworzonej wcześniej listy

            # Użycie pętli znajdującej się na górze kodu
            druga_petla(nowa_potrawa)
            continue
        else:
            print("Nieprawidłowa potrawa.") # Komunikat o nieprawidłowym wprowadzeniu potrawy


    if wybor.lower() == "usun": # Usuwanie potraw z listy potrawy
        nazwa_do_usuniecia = input("Podaj nazwę potrawy do usunięcia: ") # Pobranie nazwy usuwanej potrawy

        for potrawa in potrawy: # Pętla for sprawdzająca, czy potrawa znajduje się na liście
            if potrawa.nazwa.lower() == nazwa_do_usuniecia.lower():
                potrawy.remove(potrawa)
                print(f"Potrawa o nazwie {nazwa_do_usuniecia} została usunięta.") # Komunikat o usunęciu potrawy

            else:
                print(f"Nie znaleziono potrawy o nazwie {nazwa_do_usuniecia}.") # Komunikat o braku wpisanej potrawy na liście 



    elif wybor.lower() == "losuj": # Losowanie przez użytkownika pomysłu na potrawę z wcześniej zgromadzonych
        if not potrawy: # Warunek sprawdzający, czy istnieją już obiekty na liście
            print("Nie masz jeszcze żadnych potraw w notatniku.") # Komunikat informujący o braku obiektów na liście
        else:
            while True:
                wybor2 = input( # Wybór rodzaju potrawy do wylosowania
                    "Jaki rodzaj potrawy chcesz wylosować? Wpisz jedno z poniższych:"
                    "śniadanie, obiad, kolacja, deser"
                )
                if wybor2.lower() in ["śniadanie", "obiad", "kolacja", "deser"]: # Sprawdzenie, czy podany rodzaj potrawy jest poprawny
                    break
                else:
                    print("Nieprawidłowy wybór. Wpisz poprawny rodzaj posiłku.") # Komunikat o nieprawidłowo podanym rodzaju potrawy

            dostepne_potrawy = [potrawa for potrawa in potrawy if potrawa.ktory_posilek.lower() == wybor2.lower()] # Dodanie aktualnie dostępnych potraw na listę

            if dostepne_potrawy:
                wylosowana_potrawa = random.choice(dostepne_potrawy) # Losowanie za pomocą modułu random
                wylosowana_potrawa.wyswietl_info() # Wyświetlenie informacji o wylosowanej potrawie
            else:
                print(f"Brak potraw dostępnych dla rodzaju posiłku: {wybor2}") # Informacja o braku potraw dla danej kategorii

    elif wybor.lower() == "lista":
        if not potrawy:
            print("Nie masz jeszcze żadnych potraw w notatniku.") # Komunikat informujący o braku potraw w Notatniku
        else:
            for potrawa in potrawy:
                potrawa.wyswietl_info() # Wyświetlenie informacji o potrawie jeśli ta znajduje się na liście

    elif wybor.lower() == "koniec": # Zakończenie używania programu
        break
