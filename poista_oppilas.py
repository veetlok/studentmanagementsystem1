# Poista Oppilas
# from models import Oppilas
from data import oppilaat

# Väreja otsikoita varten.
sininenvari = "\033[34m"
resetti = "\033[0m"
lihavoitu = "\033[1m"

def poista_oppilas():

    print(f"{lihavoitu}{sininenvari}===== Poista Oppilas ====={resetti}")

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