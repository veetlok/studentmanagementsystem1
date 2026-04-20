from models import Oppilas
from data import oppilaat

# Veeti
# Oppilaiden näyttäminen

def nayta_oppilaat():
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