import pygame   #Pygame module za pravljenje igrica
import math     #za matematicke operacije
import random   #za generiranje random brojeva
import tkinter as tk    #tkinter je modula za kreiranje GUI appova
from tkinter import messagebox #za display message boxa

class kocka(object):        #definiraj classu za kockice koje cine zmiju
    redovi = 20             #broj redova 20
    w = 500                 #definiraj sirinu game prostora
    def __init__(self,start,dirnx=1,dirny=0, color=(255, 0, 0)): #definiraj constructor metodu za classu
        self.pos = start       #Postavi pocetnu poziciju kocke
        self.dirnx = 1          #Postavi horizontalni smjer kocke prema desno (kako bi se zmija pocela kretati na pocetku bez inputa)
        self.dirny = 0          #Vertikalni smjer kocke se ne mjenja
        self.color = color      #Postavljanje boje u boju, trenutno (255, 0 , 0 boji zmiju u crvenu)
    
    #pokret funkcija se koristi za kretanje kocke na novu poziciju na gridu
    def pokret(self, dirnx, dirny):
        self.dirnx = dirnx  #postavi horzontalni smjer 
        self.dirny = dirny  #postavi vertikalni smjer
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny) #Updateanje pozicije kocke dodavanjem smjerova kretanja na elemente pos tuple-a kreirajuci novi tuple

    #Funkcija nacrtaj s 3 parametra: self(kocka), povrsina (prozor igre), oci. Izracuvana udaljenost izmedu kockica i uzima poziciju kocke
    def nacrtaj(self, povrsina, oci=False):
        udaljenost = self.w // self.redovi      #Izracunava udaljenost izmedu kockica tako sto dijeli sirinu game prozora s brojem redova u kocka classi.
        i = self.pos[0]     #Horizontalna pozicija kocke spremljena u i varijablu   
        j = self.pos[1]     #Vertikalna pozicijawj kocke spremljena u j varijablu


        #Nacrta rectangle na povrsina game window, zadane boje(crvena) i dimenzija, bez ovog nema zmije
        pygame.draw.rect(povrsina, self.color, (i*udaljenost+1, j*udaljenost+1, udaljenost-2, udaljenost-2))
        if oci:     #If oci true, izvrti linije za nacrtati oci
            centar = udaljenost//2  #Izracun centra kocke
            radius = 3
            krugSredina = (i*udaljenost+centar-radius,j*udaljenost+8)   #Kalkulira poziciju prvog kruga koji predstavlja lijevo oko
            krugSredina2 = (i*udaljenost + udaljenost -radius*2, j*udaljenost+8)    #Kalkulira poziciju drugog kruga koji predstavlja desno oko
            pygame.draw.circle(povrsina, (0,0,0), krugSredina, radius)  #Za isprintati lijevo oko
            pygame.draw.circle(povrsina, (0,0,0), krugSredina2, radius) #Za isprintati desno oko

#Definiraj classu za zmiju
class zmija(object):
    tijelo = []     #Lista za pratiti zmijino tijelo
    skrece = {}     #Dictionary za pratiti promjene smjera
    def __init__(self, color, pos) -> None:     #Konstruktor medota za classu
        self.color = color  #postavi boju zmije
        self.head = kocka(pos)  #Kreiraj novu kocku za glavu zmije
        self.tijelo.append(self.head)   #Appendaj glavu zmije na tijelo
        self.dirnx = 0  #Horizontalni smjer
        self.dirny = 0  #Vertikalni smjer

    #pokret funkcija prati koje tipke stiscemo i postavlja smjer po tome
    def pokret(self):
        for event in pygame.event.get():    #pygame.even funkcija povlaci listu svih eventova koji su se dogodili od zadnjeg poziva funkcije.
                                            #For loop iterata preko tih eventova
            if event.type == pygame.QUIT:   #Provjera jel se dogodio quit event (npr user stisnuo na x za izlaz)
                pygame.quit()               #Ako da pygame.quit funkcija izlazi iz igre
            
            tipke = pygame.key.get_pressed()    #pygame.key.get_pressed() funkcija prati listu trenutno stisnutih keyeva. Ako je key stisnut daje True, inace False.

            #Ako je stisnuta lijeva strelica, postavi horizontalni smjer na -1 tj zmije ide lijevo
            if tipke[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.skrece[self.head.pos[:]] = [self.dirnx, self.dirny]    #Update skrece dictionarija s novim key value parom. Key je trenutna pozicija zmijine glave.
                                                                                #Value je lista sa horizontalnim i vertikalnim smjerom u kojem ce zmija skrenuti
            #za desnu tipku
            elif tipke[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.skrece[self.head.pos[:]] = [self.dirnx, self.dirny]

            #Gore    
            elif tipke[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.skrece[self.head.pos[:]] = [self.dirnx, self.dirny]

            #Dolje
            elif tipke[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.skrece[self.head.pos[:]] = [self.dirnx, self.dirny]
        
        for i, k in enumerate(self.tijelo):     #For loop koji prolazi elemente self.tijelo liste i prati index i
            p = k.pos[:]        #Kreira koopiju trenutne pozicije trenutnog elementa self.tijelo liste
            if p in self.skrece:    #Provjera je li p u self.skrece dictionariju
                skretanje = self.skrece[p]  #Ako je, skretanju dodjeljujemo listu s horizontalnim i vertikalnim smjerom
                k.pokret(skretanje[0], skretanje[1])
                if i == len(self.tijelo)-1: #Ako je trenutni element zadnji element u self.tijelo listi, key value par je maknut iz self.skrece dictionarija
                    self.skrece.pop(p)
            
            #Ovaj dio koda brine se o kretnji zmije, kad s lijeve strane prede ekran, pojavi se s desne.
            #Kad s desne, pojavi se s lijeve, itd. Ako se ni jedan od uvjeta ne ostavi, zmija se krece u trenutnom smjeru.
            else:
                if k.dirnx == -1 and k.pos[0] <= 0: k.pos = (k.redovi-1, k.pos[1])
                elif k.dirnx == 1 and k.pos[0] >= k.redovi-1: k.pos = (0,k.pos[1])
                elif k.dirny == 1 and k.pos[1] >= k.redovi-1: k.pos = (k.pos[0], 0)
                elif k.dirny == -1 and k.pos[1] <= 0: k.pos = (k.pos[0],k.redovi-1)
                else: k.pokret(k.dirnx,k.dirny)

    #Metoda zmija classe koja dodaje novu kocku na tijelo zmije
    def dodajKocku(self):
        rep = self.tijelo[-1]   #rep = zadnja kockica liste zmijinog tijela
        dx, dy = rep.dirnx, rep.dirny   #Assignamo 2 varijable odjednom dx = rep.dirnx, dy = rep.dirny, odredujemo lokaciju zadnje kockice zmijinog tijela

        if dx == 1 and dy == 0:     #Ako se zadnja kockica krece u desno, dodaj kockicu s lijeve strane
            self.tijelo.append(kocka((rep.pos[0]-1,rep.pos[1])))
        elif dx == -1 and dy == 0:  #Ako se zadnja kockica krece u lijevo, dodaj kockicu s desne strane
            self.tijelo.append(kocka((rep.pos[0]+1,rep.pos[1])))
        elif dx == 0 and dy == 1:   #Ako se krece prema gore, dodaj kockicu od dolje
            self.tijelo.append(kocka((rep.pos[0],rep.pos[1]-1)))
        elif dx == 0 and dy == -1:  #Ako se krece prema dolje, dodaj kockicu od gore
            self.tijelo.append(kocka((rep.pos[0],rep.pos[1]+1)))

        #S ovim odredujemo smjer dodane kockice da bude isti smjeru kretanja prethodno zadnje kockice
        self.tijelo[-1].dirnx = dx
        self.tijelo[-1].dirny = dy

    #Metoda zmija classe, uzima povrsina parametar koji predstavlja game window povrsinu i onda prode kroz listu kockica i za svaku pozove nacrtaj metodu. 
    def nacrtaj(self, povrsina):                #Ako je kockica glava zmije, isprinta i oci
        for i, k in enumerate(self.tijelo):
            if i == 0:
                k.nacrtaj(povrsina, True)
            else:
                k.nacrtaj(povrsina)
    
    #Metoda koja se koristi za reset zmijinog tijela. Uzima pos argument koji predstavlja pocetnu poziciju zmijine glave. Resetira listu zmijinog tijela da sadrzi samo glavu.
    # isprazni skrece dictionary i stavi dirnx i dirny na 0 sto znaci da se zmija ne krece.
    def reset(self, pos):
     self.head = kocka(pos)
     self.tijelo = [self.head]
     self.skrece = {}
     self.dirnx = 0
     self.dirny = 0

#Funkcija iscrtaj mrezu iscrtava mrezu na igrajucu povrsinu. Uzima sirinu prozora w, povrsinu game windowa povrsina i broj redova.
def iscrtajMrezu(w, redovi, povrsina):
    velicinaIzmedu = w // redovi    #Kalkulira udaljenost izmedu linija na mrezi

    x = 0
    y = 0
    for i in range(redovi):     #Iterata kroz svaki red i stupac, koristi x, y za kordinate i tamo printa bijele linije pomocu pygame.draw.line
        x = x + velicinaIzmedu  #Svaki iteration dodaje na x i y razmak izmedu redova kako bi isprintao grid.
        y = y + velicinaIzmedu

        pygame.draw.line(povrsina, (255, 255, 255), (x,0) , (x,w))
        pygame.draw.line(povrsina, (255, 255, 255), (0,y) , (w,y))

#Funkcija se koristi za udpateanje game windowa
def ponoviProzor(povrsina):
    global redovi, sirina, z, snack
    povrsina.fill((0,0,0))  #ispuni game window crnom bojom
    z.nacrtaj(povrsina)     #nacrtaj zmiju
    snack.nacrtaj(povrsina) #nacrtaj snack
    iscrtajMrezu(sirina, redovi, povrsina)  #iscrtaj mrezu
    pygame.display.update() #updateaj display za prikaz promjena


#Funkcija generira kordinate snackova za zmiju
def randomSnack(redovi, item):
    
    pozicije = item.tijelo  #pozicije prati sve lokacije kockica zmijinog tijela kako nebi isprintali snack na zmijinom tijelu

    while True: #loop se vrti sve dok se ne nadu dobri kordinati za nagradu
         x = random.randrange(redovi)   #x je random broj u rangu 0-redovi -1
         y = random.randrange(redovi)   #y je random broj u rangu 0-redovi -1
         if len(list(filter(lambda z:z.pos == (x,y) , pozicije))) > 0:  #Ova linija provjerava preklapaju li se x y kordinati sa zmijom
              continue  #ako da, ponovi generaciju random brojeva
         else:  #Inace brejk iz loopa i vrati kordinate za snack
              break
    return (x,y)

#funkcija za Display poruke, subjekt ce biti naslov 
def message_box(subjekt, sadrzaj):
     root = tk.Tk()     #kreira novi tkinter window
     root.attributes("-topmost", True)  #ova linija se pobrine da prozor iskoci preko ostalih prozora
     root.withdraw()    #Ova linija skriva prozor tako da nije vidljiv na ekranu
     messagebox.showinfo(subjekt, sadrzaj)
     try:   #Ovaj dio koda unistava prozor ako  vec nije unisten
          root.destroy()
     except:
          pass     


def main ():
    global sirina, redovi, z, snack
    sirina = 500    #postavi dimenzije game prozora
    redovi = 20     #Broj redova
    pobjeda = pygame.display.set_mode((sirina, sirina)) #Inicijaliziraj game window
    z = zmija((255, 0, 0), (10,10)) #Kreiraj zmija objekt startne pozicije 10,10 boje 255, 0, 0 tj. crevene
    snack = kocka(randomSnack(redovi, z), color=(0,255,0))
    igra = True

    sat = pygame.time.Clock()   #Postavi game clock

    while igra:
        pygame.time.delay(50)   #postavi delay od 50 milisekundi na game loop
        sat.tick(10)    #Sat kuca 10 frameova po sekundi
        z.pokret()      #Pokreci zmiju u trenutnom smjeru
        if z.tijelo[0].pos == snack.pos:    #Provjeri jeli zmija pojela snack i dodaj kocku na rep ako je
             z.dodajKocku()
             snack = kocka(randomSnack(redovi, z), color=(0,255,0))
        for x in range(len(z.tijelo)):      #Provjerava sudaranje zmije sa svojim tijelom i printa score s porukom
             if z.tijelo[x].pos in list(map(lambda z:z.pos, z.tijelo[x+1 :])):
                print('Score: ', len(z.tijelo))
                message_box('You lost!', 'Play again')
                z.reset((10, 10)) 
                break  
        ponoviProzor(pobjeda)   #ponovno nacratj game window

main()