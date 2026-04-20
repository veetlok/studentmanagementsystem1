from data import oppilaat

# Veeti
# Oppilaan ID:llä etsiminen ja valuerror jos virheellinen input
def nayta_arvosana():
    
    try:
         oppilas_id = int(input("Anna oppilaan ID: "))
    except ValueError:
         print("Virheellinen ID.")
         return
    
# Tulosten esittäminen
    for o in oppilaat:
         if o.oppilas_id == oppilas_id:
              print(f"Löytyi: Nimi: {o.nimi}, Ikä: {o.ika}, Kurssit: {o.arvosanat}")
              
              print(f"Kaikkien kurssien keskiarvo: {o.arvosanat}")
              return
         
    print("Oppilasta ei löytynyt.")



