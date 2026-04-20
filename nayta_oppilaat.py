from models import Oppilas
from data import oppilaat

# Veeti
# Oppilaiden näyttäminen
# Värejä otsikoita varten.
sininenvari = "\033[34m"
resetti = "\033[0m"
lihavoitu = "\033[1m"



def nayta_oppilaat():
    print(f"{lihavoitu}{sininenvari}===== Listaa Oppilaat ====={resetti}")
    if not oppilaat:
        print("Ei oppilaita.")
        print()
        input("Paina enteriä jatkaaksesi.")
        return
    
    for o in oppilaat:        
        print("ID:", o.oppilas_id,"|","NIMI:", o.nimi,"|","IKÄ:", o.ika)
        print()
        input("Paina enteriä jatkaaksesi.")
        continue