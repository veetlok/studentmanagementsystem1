# Kaiken pohja.

class Oppilas:
    def __init__(self, oppilas_id, nimi, ika):
        self.oppilas_id = oppilas_id
        self.nimi = nimi
        self.ika = ika
        self.kurssit = []
        self.arvosanat = {}


# Tietokanta/Lista, johon tieto tallennetaan.
oppilas = [] 


# Toimintojen Funktiot. 
def lisaa_oppilas():
    pass

def nayta_oppilaat():
    pass

def etsi_oppilas():
    pass

def anna_arvosanat():
    pass

def poista_oppilas():
    pass


# Ohjelman valikko.
def valikko():
    while True:

        print("1. Lisää oppilas.")
        print("2. Listaa oppilaat.")
        print("3. Etsi oppilas.")
        print("4. Näytä arvosanat.")
        print("5. Poista oppilas.")
        print("0. Poistu.")

        valinta = input("Valitse vaihtoehto: ")

        if valinta == "1":
            lisaa_oppilas()
        elif valinta == "2":
            nayta_oppilaat()
        elif valinta == "3":
            etsi_oppilas()
        elif valinta == "4":
            anna_arvosanat()
        elif valinta == "5":
            poista_oppilas()
        elif valinta == "0":
            break
        else:
            input("Väärä valinta. Paina enteriä jatkaaksesi.")
            continue
           
# Ohjelma käynnistyy.
if __name__ == "__main__":
    valikko()




