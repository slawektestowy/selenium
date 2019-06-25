dziennik = {1:"Kowalski", 2:"Nowak", 3:"Kucharski", 4:"Cichy"}

print(dziennik.get(2))
print(dziennik.get(3))

print(dziennik[1])

dziennik[5] = "Mucha"
print(dziennik)

for i in dziennik.keys():
    print(i)


for i in dziennik.values():
    print(i)

del dziennik[4]

print(dziennik)

