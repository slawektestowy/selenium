class pracownik:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return("Mam na imie " + self.imie + " " + self.nazwisko)

class pozycja(pracownik):

    def __init__(self, imie, nazwisko, poz):
        pracownik.__init__(self,imie,nazwisko)
        self.poz = poz



pracownik1 = pracownik("John", "Rambo")
print(pracownik1.nazwisko)

pracownik2 = pozycja("Jan", "Burak", "Manager")
print(pracownik2.przedstaw_sie())