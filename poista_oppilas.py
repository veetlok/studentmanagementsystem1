# Poista Oppilas
# from models import Oppilas
from data import oppilaat

def poista_oppilas():

    poistettava_oppilastunnus = (int(input("Anna oppilaan ID jonka haluat poistaa. : ")))

    for o in oppilaat:
        if o.oppilas_id == poistettava_oppilastunnus:
            oppilaat.remove(o)
            print("Oppilas poistettu onnistuneesti.")
        else:
            print("Oppilasta ei löytynyt.")


