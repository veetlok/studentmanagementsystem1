from data import oppilaat

# Värejä otsikoita varten.
sininenvari = "\033[34m"
resetti = "\033[0m"
lihavoitu = "\033[1m"

def etsi_oppilas():
    
    print(f"{lihavoitu}{sininenvari}===== Etsi Oppilas ====={resetti}")

    try:
         oppilas_id = int(input("Anna oppilaan ID: "))
    except ValueError:
         print("Virheellinen ID.")
         return
    

    for o in oppilaat:
         if o.oppilas_id == oppilas_id:
              print(f"Löytyi: {o.nimi}, ikä {o.ika}")
              return
         
    print("Oppilasta ei löytynyt.")


             

    


