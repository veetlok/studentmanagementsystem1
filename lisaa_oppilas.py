from models import Oppilas
from data import oppilaat

# Värejä otsikoita varten.
sininenvari = "\033[34m"
resetti = "\033[0m"
lihavoitu = "\033[1m"

def lisaa_oppilas():

    # Looppi alkaa:
    while True:
        print(f"{lihavoitu}{sininenvari}===== Lisää Oppilas ====={resetti}")
        print("1. Lisää oppilas.")
        print("2. Päivitä oppilaan tiedot.")
        print("3. Peruuta.")    
            
        try:
            valinta = int(input("Valitse vaihtoehto: "))
        except ValueError:
            print("Anna kelvollinen luku!")
            continue

        # Uuden oppilaan lisääminen
        if valinta == 1:
            try:
                nimi = input("Anna nimi: ")
                ika = int(input("Anna ikä: "))
                oppilas_id = id(nimi)
                
                # Kerää uuden oppilaan tiedot uuteen paikkaan
                uusi = Oppilas(oppilas_id, nimi, ika)
                oppilaat.append(uusi)
                
                # Näyttää luodun henkilön.
                print()
                print("Oppilas lisätty!", "ID:", oppilas_id, "|", "NIMI:", nimi, "|", "IKÄ:", ika) 
                print()
                input("Paina nappia jatkaaksesi.")
                break
            
            except ValueError:
                print("Kirjoitus muoto väärä, yritä uudelleen.")
            


        if valinta == 2:
            print("1. Päivitä nimi")
            print("2. Päivitä ikä.")
    
            try:
                valinta = int(input("Valitse vaihtoehto: "))
            except ValueError:
                print("Anna kelvollinen luku!")
                continue
    
            # Syötetään muokattavan oppilaan id: 
            try:
                oppilas_id = int(input("Anna oppilaan ID: "))
            except ValueError:
                print("Virheellinen ID.")
                continue
    
            # Päivittää olemassa olevan oppilaan tietoja:
            oppilas = next((o for o in oppilaat if o.oppilas_id == oppilas_id), None)

            if oppilas is None:
                print("Oppilasta ei löydy!")
                continue

            # Nimen päivittäminen
            if valinta == 1:
                oppilas.nimi = (input("Anna uusi nimi:"))
                print("Nimi päivitetty!")
                print()
                break

            # Iän päivittäminen
            if valinta == 2:
                try:
                    oppilas.ika = int(input("Anna uusi ikä:"))
                    print("Ikä päivitetty!")
                    print()
                    break
                except ValueError:
                    print("Anna kelvollinen luku!")
                    continue

        # Paluu main sivulle:        
        if valinta == 3:
            return