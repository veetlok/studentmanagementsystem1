from data import oppilaat

def etsi_oppilas():
    
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


             

    


