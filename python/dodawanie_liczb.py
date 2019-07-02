# try:
#     print("Podaj pierwsza liczbe: ")
#     pierwsza_liczba = int(input())
#     print("Podaj druga liczbe: ")
#     druga_liczba = int(input())
#     print(f"Twoj wynik, ktory uzyskales to {pierwsza_liczba + druga_liczba} ")
# except ValueError:
#     print("Nie podałeś liczby ani cyfry")


def Niedzielnik():
    while True:
        try:
            print("poda pierwsza liczbe: ")
            a = int(input())
            print("poda druga liczbe: ")
            b = int(input())
            print (a / b)
            break
        except ZeroDivisionError:
            print("nie mozna dzielic przez ZERO")
            continue
        except ValueError:
            print("nie moga byc stringi")
            continue

Niedzielnik()

