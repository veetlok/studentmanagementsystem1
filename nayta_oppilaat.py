from models import Oppilas
from data import oppilaat

# Veeti
# Oppilaiden näyttäminen
# Värejä otsikoita varten.
sininenvari = "\033[34m"
resetti = "\033[0m"
lihavoitu = "\033[1m"



def nayta_oppilaat():
    print(f"{lihavoitu}{sininenvari}===== NÄYTÄ OPPILAAT ====={resetti}")
    if not oppilaat:
        print("Ei oppilaita.")
        print()
        return
    
    for o in oppilaat:        
        print("ID:", o.oppilas_id,"|","NIMI:", o.nimi,"|","IKÄ:", o.ika)
        print()
        continue