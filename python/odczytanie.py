file = open("wiadomosc.txt")
zawartosc = file.read()
print(zawartosc)
file.close

file = open("wiadomosc.txt")
zawartosc = file.readlines()
print(zawartosc)
file.close


file = open("wiadomosc.txt")
zawartosc = file.readline()
print(zawartosc)
file.close


print("#" * 30)

file = open("wiadomosc.txt")
for l in file:
    print(l)
file.close()