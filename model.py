STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "W"
PORAZ = "X"
ZACETEK = "Start"
class Igra:

#     def __init__(self, geslo: str, crke: list) -> None:
#         self.geslo = geslo.upper()
#         self.crke = crke

    def __init__(self, geslo, crke=None) -> None:
        self.geslo = geslo.upper()
        if crke is not None:
            self.crke = crke
        else:
            self.crke = []
    
#     def napacne_crke(self):
#         napacne = []
#         for crka in self.crke:
#             if not (crka in self.geslo):
#                 napacne.append(crka)
#         return napacne

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

#     def pravilne_crke(self):
#         pravilne = []
#         for crka in self.crke:
#             if crka.lower() in self.geslo:
#                 pravilne.append(crka)
#         return pravilne

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ""
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += "_"
        return niz

#     def pravilni_del_gesla(self):
#         return "".join([(crka if crka in self.crke else "_") for crka in self.geslo])

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

#     def ugibaj(self, crka):
#         # Najprej preverimo, ali je črka ponovljena.
#         #     Če je črka ponovljena, se stanje igre ne spremeni. Vrnemo konstanto PONOVLJENA_CRKA.
#         # Če smo dobili novo črko, moramo posodobiti stanje igre.
#         #     Ali smo zmagali? --> ZMAGA
#         #     Ali smo izgubili? --> PORAZ
#         #     Ali je črka pravilna? --> PRAVILNA_CRKA
#         #     Sicer: --> NAPACNA_CRKA
#         if crka in self.crke:
#             return PONOVLJENA_CRKA
#         else:
#             self.crke.append(crka)
#             if self.zmaga():
#                 return ZMAGA
#             elif self.poraz():
#                 return PORAZ
#             elif crka in self.pravilne_crke():
#                 return PRAVILNA_CRKA
#             else:
#                 return NAPACNA_CRKA

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open("besede.txt", encoding="utf8") as d:
    bazen_besed = d.read().split("\n")

# bazen_besed = []
# with open("besede.txt", encoding="utf8") as d:
#     for beseda in d:
#         bazen_besed.append(beseda.strip())


import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)
#import uuid (zgenerira nek unique id)
class Vislice:
    def __init__(self) -> None:
        self.igre = {}
    def prost_id_igre(self):
        return len(self.igre)
    def nova_igra(self):
        igra = nova_igra()
        novi_id= self.prost_id_igre()
        self.igre[novi_id] = (igra, ZACETEK)
        return novi_id
    def ugibaj(self, id_igre, crka):
        igra= self.igre[id_igre][0]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)