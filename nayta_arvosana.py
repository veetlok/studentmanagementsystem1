from data import oppilaat
import numpy as np

# Väreja otsikoita varten.
sininenvari = "\033[34m"
resetti = "\033[0m"
lihavoitu = "\033[1m"

# Veeti
# Oppilaan ID:llä etsiminen ja valuerror jos virheellinen input
def nayta_arvosana():
    
    print(f"{lihavoitu}{sininenvari}===== Näytä Oppilaan Arvosana ====={resetti}")

    try:
         oppilas_id = int(input("Anna oppilaan ID: "))
    except ValueError:
         print("Virheellinen ID.")
         return
    
# Tulosten esittäminen
    for o in oppilaat:
         if o.oppilas_id == oppilas_id:
               print(f"Löytyi: Nimi: {o.nimi}, Ikä: {o.ika}, Kurssit: {o.arvosanat}")  
                           
               keskiarvo = np.mean(list(o.arvosanat.values()))
 
               print("Oppilaan arvosanojen keskiarvo: " + str(keskiarvo))     
               return
         
    print("Oppilasta ei löytynyt.")



