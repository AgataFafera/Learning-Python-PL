import time 
import sys 

#powitanie

print("Witaj w grze. Czy jesteś gotowy/a na wyzwanie?")
imie = input("Podaj swoje imię: ")
time.sleep(1)
print("Witaj, "+ imie + "!")

#zmienne w grze

zdrowie = 100

#funkcja służąca czytaniu litera po literze

def literowanie(tekst):
    literki = [litera for litera in tekst]
    for i in literki:
        time.sleep(0.009)
        print(i, end='')

#rozdzialy gry zapisane w funkcjach 

def rozdzial1(): 
    global zdrowie
    tekst = '''
Wchodzisz do ciemnego lasu, pełnego starych drzew i niebezpiecznych stworzeń.
Po dłuższym marszu napotykasz chatkę, w której świeci się światło. Co robisz?
Wpisz 1, jeśli chcesz wejść do chatki. Wpisz 2, jeśli chcesz poczekać na zewnątrz. '''
    literowanie(tekst)
    
    while True:
        wybor = input("Wpisz numer.")
        if wybor == '1': 
            tekst = """
W chatce napotykasz starą czarownicę, która właśnie miesza eliksiry w kociołku.
Na twój widok podnosi głowę i chichocze."""
            literowanie(tekst)
            break
        elif wybor == '2': 
            zdrowie += 10
            tekst = '''
Za chatką, w składziku śmieci, znajdujesz amulet. Trzymając go, czujesz przypływ sił!
Zyskujesz 10 punktów zdrowia!
Zwabiona hałasem czarownica wychodzi z chatki i podchodzi do ciebie.'''
            literowanie(tekst)
            break
        else: 
            print("Nieprawidłowy wybór.")
        
        
        
def rozdzial2(): 
    global zdrowie 
    tekst = """
Czarownica zaprasza cię na herbatę. Podczas rozmowy z nią dowiadujesz się o wielkim skarbie, 
który jest strzeżony przez potężnego smoka i znajduje się w jasknini na krańcu lasu.
Czarownica proponuje ci wypicie tajemniczego eliksiru, który przyrządziła. Czy się zgodzisz?
Jeśli tak, wpisz 1. Jeśli nie, wpisz 2."""
    literowanie(tekst)
    while True:
        wybor = input("Wpisz liczbę.")
        if wybor == '1': 
            tekst = ''' 
Wypijasz miksturę. Smakuje paskudnie!")
Zyskujesz 10 punktów zdrowia! '''
            zdrowie += 10
            break
        elif wybor == '2': 
            tekst = """
Odmawiasz wypcia mikstury.
Czarownica jest nieźle wkurzona!
Wściekła, rzuca na ciebie zaklęcie. Tracisz 20 punktów zdrowia! """
            literowanie(tekst)
            zdrowie -= 20
            break
        else: 
            print('Nieprawidłowy wybór.')
        
def rozdzial3(): 
    global zdrowie
    tekst = ''' 
Podróżujesz lasem w celu odnalezienia jaskini.
Nagle las się kończy, a przed tobą ukazuje się wzgórze.
Po jego drugiej stronie jest jasknia. To tu!
Wchodzisz do jaskini. Od razu słyszysz donośnie chrapanie śpiącego smoka. Na co się decydujesz? 
Aby wbiec do leża smoka i go zaatakować we śnie, wpisz 1.
Aby po cichutku zbliżyć się do leża, wpisz 2. '''
    literowanie(tekst)
    while True:    
        wybor = input("Wpisz liczbę: ")
        if wybor == '1': 
            tekst = '''
Z krzykiem wpadasz na smoka z mieczem w ręku. Atakujesz go, miecz jednak odbija się od skóry. Smok się budzi...
Smok rzuca się na ciebie i zjada cię. Koniec gry! '''
            literowanie(tekst)
            sys.exit()
            break
        elif wybor == '2': 
            tekst = ''' 
Powoli wkraczasz do leża smoka. Ten jest jednak bardzo czuły na każdy hałas i budzi się.
\"Witaj\" - mówi smok swoim głębokim głosem - \"czy jesteś jednym z tych szaleńców, którzy przybli po mój skarb?\"
Wpisz 1, aby przywitać smoka i go pozdrowić. Wpisz 2, aby obrzucić go obelgami za pożeranie ludzi. '''
            literowanie(tekst)
            while True:
                wybor = input("Wpisz liczbę: ")
                if wybor == '1': 
                    tekst = '''
\"Nikt jeszcze mnie tak przyjaźnie nie przywitał...\" - mówi smok, pochylając głowę.
\"Widzę, że masz przyjazne zamiary. Możesz w takim razie zostać moim przyjacielem i ujrzeć mój skarb\"
Smok powoli obraca się w swoim gnieździe ze złota i ukazuje smocze jajo.
\"Oto mój skarb.\"
Koniec gry. Gratulacje! '''
                    literowanie(tekst)
                if wybor == '2': 
                    tekst = ''' 
Smok spokojnie czeka, aż skończysz swoją tyradę.
Po chwili brakuje ci powietrza od ciągłego krzyku. Nagle zauważasz potężny smoczy ogon lądujący na tobie. '''
                    literowanie(tekst)
                    zdrowie -= 100
                    if zdrowie < 0: 
                        tekst = "Zginąłeś. Przegrana!"
                        literowanie(tekst)
                        sys.exit()
                        break
                    else: 
                        tekst = ''' 
Cudem przeżyłeś. Co chcesz zrobić?
Wpisz 1, aby uciec z jaskini. Wpisz 2, aby spróbować porozmawiać ze smokiem. '''
                        literowanie(tekst)
                        while True:
                            wybor = input("Wpisz liczbę: ")
                            if wybor == '1': 
                                tekst = "Uciekasz z jaskini. Nie udało ci się wykonać misji. Przegrana!"
                                literowanie(tekst)
                                sys.exit()
                                break
                            elif wybor == '2': 
                                tekst = '''
Próbujesz przebłagać smoka, by więcej ciebie nie krzywdził.                    
\"Nie chcę cię zabijać, nie chowam też urazy\" - odpowiada spokojnie smok.                   
\"Wielu śmiałków próbuje zdobyć mój skarb, sądząc że w ten sposób się wzbogacą i odmienią swoje życie.\"                    
\"Nie zdają sobie jednak sprawy, że mój skarb im w tym nie pomoże.\"                   
\"Czym w takim razie jest twój skarb?\" - pytasz.
Smok powoli obraca się w swoim gnieździe ze złota i ukazuje smocze jajo.
\"Oto mój skarb.\" '''
                                literowanie(tekst)
                                time.sleep(2)
                                print("Koniec gry. Gratulacje!")
                            break
                        else: 
                            print('Nieprawidłowy wybór.')
                break            
            else: 
                print('Nieprawidłowy wybór.')
     
        break
    else:
        print('Nieprawidłowy wybór.')
        


#aktywowanie historii
            
rozdzial1()        
rozdzial2()        
rozdzial3()
