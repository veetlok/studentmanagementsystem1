from data import oppilaat
import numpy as np



def nayta_arvosana():
    
    try:
         oppilas_id = int(input("Anna oppilaan ID: "))
    except ValueError:
         print("Virheellinen ID.")
         return
    

    for o in oppilaat:
         if o.oppilas_id == oppilas_id:
               print(f"Löytyi: Nimi: {o.nimi}, Ikä: {o.ika}, Kurssit: {o.arvosanat}")  
                           
               keskiarvo = np.mean(list(o.arvosanat.values()))
 
               print("Oppilaan arvosanojen keskiarvo: " + str(keskiarvo))     
               return
         
    print("Oppilasta ei löytynyt.")



