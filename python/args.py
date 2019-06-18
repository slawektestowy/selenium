# def rzeczy(*args):
#     for i in args:
#         print(i)
#
# rzeczy('litera', "string", "float")
#
# print("$" * 30)
#
# def rzeczy(pierwsza_rzecz, *args):
#     print(pierwsza_rzecz)
#     print(args[0])
#     for i in args:
#         print(i)
#
# rzeczy('litera', "string", "float", "number")


def dziennik(klasa, **kwargs):
    print(f'Klasa {klasa}')
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get('Kucharski'))

dziennik('3A', Kowalski = "1", Nowak = "2", Kucharski = "3")
