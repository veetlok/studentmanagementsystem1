from models import Oppilas
from data import oppilaat

def lisaa_oppilas():
    while True: # Loopissa niin kauan kunnes oppilaan tiedot annetaan oikein.
        try:
            nimi = input("Anna nimi: ")
            ika = int(input("Anna ikä: "))
            oppilas_id = id(nimi)
            break
        except ValueError:  # Jos ikä annetaan väärin, niin looppi jatkuu.
            print("Kirjoitus muoto väärä, yritä uudelleen.")


    uusi = Oppilas(oppilas_id, nimi, ika)
    oppilaat.append(uusi)

    print("Oppilas lisätty!", "ID:", oppilas_id, "|", "NIMI:", nimi, "|", "IKÄ:", ika) # Näyttää luodun henkilön.
    print()
    input("Paina nappia jatkaaksesi.")