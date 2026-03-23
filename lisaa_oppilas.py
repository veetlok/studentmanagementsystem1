from models import Oppilas
from data import oppilaat

def lisaa_oppilas():
    while True:
        try:
            nimi = input("Anna nimi: ")
            ika = int(input("Anna ikä: "))
            oppilas_id = id(nimi)
            break
        except ValueError:
            print("Kirjoitus muoto väärä, yritä uudelleen.")
        except:
            print("Jotain meni pieleen, yritä uudelleen.")
    
    uusi = Oppilas(oppilas_id, nimi, ika)
    oppilaat.append(uusi)

    print("Oppilas lisätty!")