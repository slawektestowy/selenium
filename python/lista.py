lista = ["Bartek", "Tomek", "Basia", 1, 2, 3, 4 ]

print(lista[2])
for i in lista:
    print(i)

print(lista[0:4])
print(lista.index("Tomek"))   # miejsce na ktorym znajduje sie dany element listy

lista.append("Jedynka") # dodanie elementu na koncu listy
lista.insert(0, "nova") # dodanie elementu na konkretnym miejscu listty
print(lista)

print(len(lista)) # sprawdzenie dlugosci listy

lista.remove("Basia")
print(lista)

del lista[0]
print(lista)


pierwsza_lista = ["koc", 'kanapa', "aparat"]
druga_lista = ["auto", "noga", 1, 2, 4]
print(pierwsza_lista*3)
print(pierwsza_lista + druga_lista)