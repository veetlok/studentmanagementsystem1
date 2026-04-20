from lisaa_oppilas import lisaa_oppilas
from nayta_oppilaat import nayta_oppilaat
from etsi_oppilas import etsi_oppilas
from poista_oppilas import poista_oppilas
from arvosanat import lisaa_arvosana
from nayta_arvosana import nayta_arvosana

# Värejä otsikoita varten.
sininenvari = "\033[34m"
punainenvari = "\033[0;31m"
resetti = "\033[0m"
lihavoitu = "\033[1m"

# Ohjelman valikko.
def valikko():
    
    print(f"{lihavoitu}{sininenvari}===== VALIKKO ====={resetti}")

    while True:
        
        print("1. Lisää oppilas.")
        print("2. Listaa oppilaat.")
        print("3. Etsi oppilas.")
        print("4. Lisää oppilaan arvosana.")
        print("5. Näytä oppilaan arvosana.")
        print("6. Poista oppilas.")
        print(f"0. {lihavoitu}{punainenvari}Poistu.{resetti}")

        try:
            valinta = int(input("Valitse vaihtoehto: "))
        except ValueError:
            print("Anna kelvollinen luku!")
            continue

        if valinta == 1:
            lisaa_oppilas()
        elif valinta == 2:
            nayta_oppilaat()
        elif valinta == 3:
            etsi_oppilas()
        elif valinta == 4:
            lisaa_arvosana()
        elif valinta == 5:
            nayta_arvosana()
        elif valinta == 6:
            poista_oppilas()
        elif valinta == 0:
            break
        else:
            input("Väärä valinta. Paina enteriä jatkaaksesi.")
            continue
           
# Ohjelma käynnistyy.
if __name__ == "__main__":
    valikko()

