import time 
import sys 

#powitanie

print("Witaj w grze. Czy jesteś gotowy/a na wyzwanie?")
imie = input("Podaj swoje imię: ")
time.sleep(1)
print("Witaj, "+ imie + "!")

#zmienne w grze

zdrowie = 100

#rozdzialy gry zapisane w funkcjach 

def rozdzial1(): 
    global zdrowie
    print("Wchodzisz do ciemnego lasu, pełnego starych drzew i niebezpiecznych stworzeń.")
    time.sleep(2)
    print("Po dłuższym marszu napotykasz chatkę, w której świeci się światło. Co robisz?")
    print("Wpisz 1, jeśli chcesz wejść do chatki. Wpisz 2, jeśli chcesz poczekać na zewnątrz.")
    wybor = int(input("Wpisz numer."))
    if wybor == 1: 
        tekst1 = """W chatce napotykasz starą czarownicę, która właśnie miesza eliksiry w kociołku.
        Na twój widok podnosi głowę i chichocze."""
        print(tekst1)
    elif wybor == 2: 
        print("Za chatką, w składziku śmieci, znajdujesz amulet. Trzymając go, czujesz przypływ sił!")
        print("Monety + 10")
        zdrowie += 10
        time.sleep(2)
        print("Zwabiona hałasem czarownica wychodzi z chatki i podchodzi do ciebie.")
    else: 
        print("Nieprawidłowy wybór. Koniec gry.")
        sys.exit()
        
        
def rozdzial2(): 
    global zdrowie 
    tekst = """Czarownica zaprasza cię na herbatę. Podczas rozmowy z nią dowiadujesz się o wielkim skarbie, 
    który jest strzeżony przez potężnego smoka i znajduje się w jasknini na krańcu lasu."""
    print(tekst)
    time.sleep(2)
    print("Czarownica proponuje ci wypicie tajemniczego eliksiru, który przyrządziła. Czy się zgodzisz?")
    print("Jeśli tak, wpisz 1. Jeśli nie, wpisz 2.")
    wybor = int(input("Wpisz liczbę."))
    if wybor == 1: 
        print("Wypijasz miksturę. Smakuje paskudnie!")
        time.sleep(2)
        print("Zyskujesz 10 punktów zdrowia!")
        zdrowie += 10
    elif wybor == 2: 
        print("Odmawiasz wypcia mikstury.")
        time.sleep(1)
        print("Czarownica jest nieźle wkurzona!")
        time.sleep(1)
        print("Wściekła, rzuca na ciebie zaklęcie. Tracisz 20 punktów zdrowia!")
        zdrowie -= 20
    else: 
        print('Nieprawidłowy wybór. Koniec gry.')
        sys.exit()
        
def rozdzial3(): 
    global zdrowie
    print("Podróżujesz lasem w celu odnalezienia jaskini.")
    time.sleep(1)
    print("Nagle las się kończy, a przed tobą ukazuje się wzgórze.")
    time.sleep(1)
    print("Po jego drugiej stronie jest jasknia. To tu!")
    time.sleep(1)
    print("Wchodzisz do jaskini. Od razu słyszysz donośnie chrapanie śpiącego smoka. Na co się decydujesz? ")
    print("Aby wbiec do leża smoka i go zaatakować we śnie, wpisz 1.")
    print("Aby po cichutku zbliżyć się do leża, wpisz 2.")
    wybor = int(input("Wpisz liczbę: "))
    if wybor == 1: 
        print("Z krzykiem wpadasz na smoka z mieczem w ręku. Atakujesz go, miecz jednak odbija się od skóry. Smok się budzi...")
        time.sleep(3)
        print("Smok rzuca się na ciebie i zjada cię. Koniec gry!")
        sys.exit()
    elif wybor == 2: 
        print("Powoli wkraczasz do leża smoka. Ten jest jednak bardzo czuły na każdy hałas i budzi się.")
        time.sleep(1)
        print("\"Witaj\" - mówi smok swoim głębokim głosem - \"czy jesteś jednym z tych szaleńców, którzy przybli po mój skarb?\"")
        print("Wpisz 1, aby przywitać smoka i go pozdrowić. Wpisz 2, aby obrzucić go obelgami za pożeranie ludzi.")
        wybor = int(input("Wpisz liczbę: "))
        if wybor == 1: 
            print("\"Nikt jeszcze mnie tak przyjaźnie nie przywitał...\" - mówi smok, pochylając głowę.")
            time.sleep(2)
            print("\"Widzę, że masz przyjazne zamiary. Możesz w takim razie zostać moim przyjacielem i ujrzeć mój skarb\"")
            time.sleep(3)
            print("Smok powoli obraca się w swoim gnieździe ze złota i ukazuje smocze jajo.")
            print("\"Oto mój skarb.\"")
            time.sleep(2)
            print("Koniec gry. Gratulacje!")
        if wybor == 2: 
            print("Smok spokojnie czeka, aż skończysz swoją tyradę.")
            time.sleep(2)
            print("Po chwili brakuje ci powietrza od ciągłego krzyku. Nagle zauważasz potężny smoczy ogon lądujący na tobie.")
            zdrowie -= 100
            if zdrowie < 0: 
                print("Zginąłeś. Przegrana!")
                sys.exit()
            else: 
                print("Cudem przeżyłeś. Co chcesz zrobić?")
                print("Wpisz 1, aby uciec z jaskini. Wpisz 2, aby spróbować porozmawiać ze smokiem.")
                wybor = int(input("Wpisz liczbę: "))
                if wybor == 1: 
                    print("Uciekasz z jaskini. Nie udało ci się wykonać misji. Przegrana!")
                    sys.exit()
                elif wybor == 2: 
                    print("Próbujesz przebłagać smoka, by więcej ciebie nie krzywdził.")
                    time.sleep(2)
                    print("\"Nie chcę cię zabijać, nie chowam też urazy\" - odpowiada spokojnie smok.")
                    time.sleep(1)
                    print("\"Wielu śmiałków próbuje zdobyć mój skarb, sądząc że w ten sposób się wzbogacą i odmienią swoje życie.\"")
                    time.sleep(1)
                    print("\"Nie zdają sobie jednak sprawy, że mój skarb im w tym nie pomoże.\"")
                    time.sleep(1)
                    print("\"Czym w takim razie jest twój skarb?\" - pytasz.")
                    print("Smok powoli obraca się w swoim gnieździe ze złota i ukazuje smocze jajo.")
                    print("\"Oto mój skarb.\"")
                    time.sleep(2)
                    print("Koniec gry. Gratulacje!")
                else: 
                    print('Nieprawidłowy wybór. Koniec gry.')
                    sys.exit()
        else: 
            print('Nieprawidłowy wybór. Koniec gry.')
            sys.exit()
    else:
        print('Nieprawidłowy wybór. Koniec gry.')
        sys.exit()
        
            

#aktywowanie historii
            
rozdzial1()        
rozdzial2()        
rozdzial3()
