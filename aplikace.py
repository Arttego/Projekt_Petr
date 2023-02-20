from pojistenci import Pojisteny

class Aplikace:
    def __init__(self):
        self.pojistene_osoby = []

    def pridat_pojisteneho(self):
        jmeno = input("Zadajte jméno:")
        prijmeni = input("Zadajte příjmení:")
        vek = int(input("Zadajte věk:"))
        telefon = input("Zadajte telefonní číslo:")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojistene_osoby.append(pojisteny)

    def vyhledat_pojisteneho(self):
        jmeno = input("Zadejte jméno:")
        prijmeni = input("Zadejte příjmení:")
        for pojisteny in self.pojistene_osoby:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None

    def vypis_pojistenych(self):
        for pojisteny in self.pojistene_osoby:
            print(pojisteny)