from models import Oppilas
from data import oppilaat

def lisaa_oppilas():
    oppilas_id = input("Anna ID: ")
    nimi = input("Anna nimi: ")
    ika = int(input("Anna ikä: "))

    uusi = Oppilas(oppilas_id, nimi, ika)
    oppilaat.append(uusi)

    print("Oppilas lisätty!")