from data import oppilaat

def nayta_arvosana():
    
    try:
         oppilas_id = int(input("Anna oppilaan ID: "))
    except ValueError:
         print("Virheellinen ID.")
         return
    

    for o in oppilaat:
         if o.oppilas_id == oppilas_id:
              print(f"Löytyi: Nimi: {o.nimi}, Ikä: {o.ika}, Kurssit: {o.arvosanat}")
              return
         
    print("Oppilasta ei löytynyt.")



