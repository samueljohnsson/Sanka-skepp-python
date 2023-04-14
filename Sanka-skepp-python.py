import random

antalkolumner = 10
antalrader = 10

# den bräda som båtarna genereras på som är facit
brädaFacit = [["~" for i in range(antalkolumner)] for j in range(antalrader)]



# den bräda som printas ut och visar gissningar (träffar, missar)
brädaSkott = [["~" for i in range(antalkolumner)] for j in range(antalrader)] 



# definiera funktion som skriver ut bräda
def skriv_ut(bräda):
    print("   ",end="") # gör så att brädhuvud med A-J bokstäver hamnar rakt över kolumnerna
    brädhuvud=[]
    for k in range(ord('A'),ord('A')+antalkolumner): # for-loop som loopar mellan unicode för A-J
        brädhuvud.append(chr(k)) # lägger till bokstaven till brädhuvudet
   
    for bokstav in brädhuvud: # for-loop som skriver ut varje bokstav i brädhuvudet
        print(bokstav, end=" ") # justera end-variabel så den skriver ut på samma rad
    print() # blankt print-statement, radbyte

    # skriver ut hela brädan
    for rad in range(antalrader): # for-loop som skriver ut varje rad i brädet
        if rad >= 9:  # för för att 10:an ska hamna rätt (ett hopp till vänster) på 9e iterationen
            print(rad+1,"",end="")
        else:
            print("",rad+1,"",end="") # skriver ut radnummer som centreras rätt, därav ""

        for kol in bräda[rad]: # for-loop som skriver ut varje kol (element) i raden
            print(kol,end=" ") # ,end="" för att print ska fortsätta skriva i samma rad
        print() #för att skriva på nästa rad

print() # utseendes skull





# definera funktioner till genereringen av båtar
def grannar(bräda,rad_pos,kolumn_pos): # funktion som hittar "grannarna" till en position genom att ta brädan, positionens rad, och positionens kolumn som parametrar
    grannar = [] # tom lista som grannarna till positionen ska läggas till på
    for kolumn in range(-1, 2): # for-loop som iterar en före och en efter pos kolumn (-1,2 eftersom slut är exclusive i range()
        kolumnKollar = kolumn_pos + kolumn # kolumnen som kollas är positionens + den i for-loopen (kolumnen innan till kolumnen efter postionen)
        if kolumnKollar >= 0 and kolumnKollar <= len(bräda)-1: # om kolumnen på pos vi undersöker är en den första/sista kollar vi inte kolumnen innan (på första kol) och efter (på sista kol) eftersom de blir indexet blir negativt respektive out of range
            for rad in range(-1, 2): # for-loop som itererar mellan raden innan och raden efter pos
                radKollar = rad_pos + rad # raden som kollas är rad_pos + den i for-loopen (en innan och sen en efter)
                if radKollar >= 0 and radKollar <= len(bräda)-1: # om raden på pos vi undersöker är en den första/sista kollar vi inte raden innan (på första rad) och efter (på sista rad) eftersom indexet blir negativt respektive out of range
                    if radKollar == rad_pos and kolumnKollar == kolumn_pos: # om rad+kolumn som kollas är positionen som är funtionsargumenten
                        continue # hoppa till nästa iteration
                    grannar.append(bräda[radKollar][kolumnKollar]) # lägg till i grannar-listan
    return grannar # returnera listan med grannar   




def joina(l): # joinar en lista med listor i till en lista
    return [item for sublist in l for item in sublist]




def skapa_båt(längd): # funktion som skapar en båt med parametern längd
    generera = True # skapa booleskt värde till huvud while-loopen
    
    while generera:
        start_rad = random.randint(0,9) # slumpad startrad
        start_kol = random.randint(0,9) # slumpad startkolumn

        riktning = random.choice(["vågrätt", "lodrätt"]) # slumpar riktning som skeppet ska ligga på

        if riktning == "vågrätt": # om båten ska gå vågrätt
            if start_kol + längd > 10: # om startkolumn + båtens längd går utanför brädan
                start_kol = 10-längd # sätt i kanten på brädan så att den passar

            grannarBåtdelar = [] # tom lista som ska hålla alla båtdelarnas positioners grannar
            for i in range(längd): # for loop som itererar över båtens positioner
                grannarBåtdelar.append(grannar(brädaFacit,start_rad,start_kol+i)) # lägger till grannarna för båtens alla delar i listan

            grannarBåtdelar = joina(grannarBåtdelar) # båtdelarna läggs ursprungligen till i en lista i den större listan pga funktionen grannr(), detta fixar och gör det sedan enklare att söka efter element i listan

            # behöver inte kolla om slumpad startposition är en båt eftersom det görs med grannar() på den båtdel 2
            
            if ":" not in grannarBåtdelar: # om kriterierna (ingen inom 1 position) möts
                for i in range(längd): # itererar över båtens längd för att sedan skriva ut
                    brädaFacit[start_rad][start_kol+i] = ":" # skriver ut, eftersom båten går vågrätt behöver vi bara ändra på kolumnen
                generera = False # avsluta loopen
        
            else: # om båtdel ":" finns i grannar --> det finns båtar i närheten av positionen
                continue # hoppa till nästa iteration (ny slumpad plats)

        else: # om riktning = lodrätt
            if start_rad + längd > 10: # kollar om båten passar på brädet
                start_rad = 10-längd # om ej så placera båten i kanten

            grannarBåtdelar = [] # tom lista som ska hålla båtdelarnas grannar
            for i in range(längd): # for-loop som itererar över båtens positioner för att sedan kolla dess grannar
                grannarBåtdelar.append(grannar(brädaFacit,start_rad+i,start_kol)) # lägg till aktuell båtdels grannar i listan

            grannarBåtdelar = joina(grannarBåtdelar) # gör listan grannarBåtdelar till en lista istället för en lista med listor i

            if ":" not in grannarBåtdelar: # om ingen av båtdelarna har en båt inom 1 position
                for i in range(längd): # itererar över båtens längd för att sedan sätta ut ":"
                    brädaFacit[start_rad+i][start_kol] = ":" # sätt ut ":" på båtens delar, eftersom båten går lodrätt behöver vi bara ändra på raden
                generera = False # avsluta loopen

            else: # om båtdel ":" finns i grannar --> det finns båtar i närheten
                continue # börja om
 



# Anropa funktioner som genererar båtar

for i in range(4): # generera 4 båtar 1 långa
    skapa_båt(1)

for i in range(3): # generera 3 båtar 2 långa
    skapa_båt(2)

for i in range(2): # generera 2 båtar 3 långa
    skapa_båt(3)

for i in range(1): # generera 1 båt 4 lång
    skapa_båt(4)




# skriv ut facit för Calles skull
'''
print("Facit: ")
skriv_ut(brädaFacit) 
print()
'''



# själva spelet
antal_skott = 0 # räknar antal skott skjutna
träffar = 0 # räknar antal träffar
max_träffar = 1*4+2*3+3*2+4*1 # antal totala träffar möjliga

while träffar < max_träffar: # så länge träffar är mindre än totala antalet möjliga träffar, dvs så länge man ej vunnit

    skriv_ut(brädaSkott) # skriver ut brädet med träffade och missade skott som uppdateras under spelets gång
    print(f"Antal skott skjutna: {antal_skott}") # skriver ut antal skott
    print(f"Antal träffar: {träffar}") # skriver ut antal träffar
    print() # blank rad för snygghets skull


    # ta emot och validera input
    try: # provar att ta input
        kol,rad = input("Ange position (kolumn mellanslag rad): ").split(" ") # tar input på kol och rad och splitar till två olika variabler vid mellanslaget

    except ValueError: # vid ValueError, ex. om input är "b5" och inte går att splita vid mellanslag
        kol,rad = input("Fel, försök igen. Ange position: ").split(" ") # ta ny input
        
    while kol.upper() not in ["A","B","C","D","E","F","G","H","I","J"] or rad not in ["1","2","3","4","5","6","7","8","9","10"]: # sålänge kolumn eller rad är ogiltlig
        kol,rad = input("Ogiltig kolumn/rad, försök igen. Ange position: ").split(" ") # ta ny input

    kol = int(ord(kol.upper())-65) # konverterar kolumnens bokstav till motvarande index där A = 0, B = 1 ... osv
    rad = int(rad)-1 # rad-1 för att få index rätt då fösta raden är rad 1 och inte 0


    # spelet
    if brädaSkott[rad][kol] == "x" or brädaSkott[rad][kol] == "o": # om användaren redan gissat på den positionen
        print("Du har redan gissat den positionen")
        print()

    elif brädaFacit[rad][kol] == ":": # om det finns en båt på pos på brädaFacit
        print("TRÄFF!")
        brädaSkott[rad][kol] = "x" # ändra på brädaGissningar positionen till x
        antal_skott += 1 # öka antal skott med 1
        träffar += 1 # öka träffar med 1
        print() # ny rad för snyggare formatering

    else: # om miss
        print("MISS!")
        brädaSkott[rad][kol] = "o" # ändra på brädaGissningar positionen till o
        antal_skott += 1 # öka antal skott med 1
        print() # ny rad för snyggare formatering
   

print(f"Du vann! Det tog {antal_skott} skott.") # när vi tagit oss ur while-loopen, dvs träffat alla båtar och vunnit





