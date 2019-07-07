file = open("nowy.txt", "a")  # tryb "w" nadpisuje istniejace dane, tryb "a" dodaje
file.write("\nNowszy tekst")
file.close()