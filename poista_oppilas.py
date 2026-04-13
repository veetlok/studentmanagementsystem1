# Poista Oppilas
# from models import Oppilas
from data import oppilaat

def poista_oppilas():

    try:
        poistettava_oppilastunnus = (int(input("Anna oppilaan ID jonka haluat poistaa. : ")))
    except ValueError:
         print("Virheellinen ID.")
         return

    for o in oppilaat:
        if o.oppilas_id == poistettava_oppilastunnus:
            oppilaat.remove(o)
            print("Oppilas poistettu onnistuneesti.")
        else:
            print("Oppilasta ei löytynyt.")