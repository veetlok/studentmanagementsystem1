# Malli jota käytetään oppilaiden luomiseen
class Oppilas:
    def __init__(self, oppilas_id, nimi, ika):
        self.oppilas_id = oppilas_id
        self.nimi = nimi
        self.ika = ika
        self.kurssit = []
        self.arvosanat = {}