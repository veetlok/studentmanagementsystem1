from models import Oppilas
from data import oppilaat

kurssit = [
    "Matematiikka",
    "Äidinkieli",
    "Englanti",
    "Fysiikka",
    "Ruotsi",
    "Kemia",
    "Biologia"
    ]


#lisää arvosana
def lisaa_arvosana():
    while True: # Loopissa niin kauan kunnes oppilaan tiedot annetaan oikein.     
        try:
            oppilas_id = int(input("Anna oppilaan ID: "))
        except ValueError:
            print("Virheellinen ID.")
            return
    
        for o in oppilaat:
            if o.oppilas_id == oppilas_id:
                print(f"Löytyi: {o.nimi}, ikä {o.ika}")
                break
        else:
            print("Oppilasta ei löytynyt.")
            return

        print("1. Matematiikka.")
        print("2. Äidinkieli.")
        print("3. Englanti.")
        print("4. Fysiikka.")
        print("5. Ruotsi.")
        print("6. Kemia.")
        print("7. Biologia.")
        
        try:
            valittu_numero = int(input("Valitse kurssi jolle arvosana annetaan: "))
        except ValueError:
            print("Anna kelvollinen numero.")
        
        # Valitaan kurssi jolle arvosana halutaan antaa.

        if valittu_numero == 1:
            valittu_kurssi = "Matematiikka"
        elif valittu_numero == 2:
            valittu_kurssi = "Äidinkieli"
        elif valittu_numero == 3:
            valittu_kurssi = "Englanti"
        elif valittu_numero == 4:
            valittu_kurssi = "Fysiikka"
        elif valittu_numero == 5:
            valittu_kurssi = "Ruotsi"
        elif valittu_numero == 6:
            valittu_kurssi = "Kemia"
        elif valittu_numero == 7:
            valittu_kurssi = "Biologia"
        else:
            print("Et voi valita tätä. Yritä uudelleen.")
            return
        

        # Arvosanan lisäys kurssille.
        
        while True:
            try:
                kurssi_arvosana = int(input("Anna arvosana kurssille. (1-5): "))
            except ValueError:
                print("Vain luvut ovat käytössä.")

            if kurssi_arvosana >= 6 or kurssi_arvosana <= 0: # Kurseille on mahdollisuus antaa arvosana vain numeroiden 1 ja 5 väliltä.
                print("Anna arvosana 1 ja 5 väliltä.")            
            else:
                o.arvosanat[valittu_kurssi] = kurssi_arvosana # Lisää oppilaan dictionaryyn (models.py) kurssi ja siihen liitetty arvosana.
                break

        break
        