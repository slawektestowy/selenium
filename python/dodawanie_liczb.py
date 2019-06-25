try:
    print("Podaj pierwsza liczbe: ")
    pierwsza_liczba = int(input())
    print("Podaj druga liczbe: ")
    druga_liczba = int(input())
    print(f"Twoj wynik, ktory uzyskales to {pierwsza_liczba + druga_liczba} ")
except ValueError:
    print("Nie podałeś liczby ani cyfry")


def Niedzielnik(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return("nie mozna dzielic przez ZERO")

print(Niedzielnik(1,0))

