from models import Oppilas
from data import oppilaat

def nayta_oppilaat():
    if not oppilaat:
        print("Ei oppilaita.")
        return
    
    for o in oppilaat:
        print("ID:", o.oppilas_id,"|","NIMI:", o.nimi,"|","IKÄ:", o.ika)