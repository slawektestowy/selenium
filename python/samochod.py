class auto:

    marka = "Skoda"

    def __init__(self, model, kolor, rok):
        self.model = model
        self.kolor = kolor
        self.rok = rok

samochod_1 = auto("Kodiak","Czerwony", "2010")
samochod_2 = auto("Superb", "Czarny", "2019")
samochod_3 = auto("Fabia", "Zielony", "2015")
print(samochod_1.kolor)
print(samochod_1.marka)
print(auto.marka)