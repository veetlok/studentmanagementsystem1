from models import Oppilas
from data import oppilaat

kurssit = [
    1 == "Matematiikka",
    2 == "Äidinkieli",
    3 == "Englanti",
    4 =="Fysiikka",
    5 == "Ruotsi",
    6 == "Kemia",
    7 =="Biologia"
    ]

arvosanat = []

#lisää arvosana
def lisaa_arvosana():
    while True: # Loopissa niin kauan kunnes oppilaan tiedot annetaan oikein.
        try:
            oppilas_id = int(input("Anna oppilaan ID: "))
        except ValueError:
            print("Virheellinen ID.")
            return
        

        print("1. Matematiikka.")
        print("2. Äidinkieli.")
        print("3. Englanti.")
        print("4. Fysiikka.")
        print("5. Ruotsi.")
        print("6. Kemia.")
        print("7. Biologia.")

        if kurssit:
            input("Valitse kurssi: ")
            break
#         else:
#             input("Väärä valinta. Paina enteriä jatkaaksesi.")
#             continue
    
#         try:
#             kurssit = input
#             arvosana = input("Anna oppilaan arvosana: ")
            
#             break
#         except ValueError:  # Jos ikä annetaan väärin, niin looppi jatkuu.
#             print("Kirjoitus muoto väärä, yritä uudelleen.")


# def nayta_arvosana():
#     print("terveterve")