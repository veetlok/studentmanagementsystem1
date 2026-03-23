from lisaa_oppilas import lisaa_oppilas
from nayta_oppilaat import nayta_oppilaat
from etsi_oppilas import etsi_oppilas
from poista_oppilas import poista_oppilas
# from kysy_arvosanat import kysy_arvosanat

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
            kysy_arvosanat()
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




