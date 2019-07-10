import random


def generuj(min, max):
    return random.randint(min,max)


for i in range(0,6):
    print(generuj(1,49))

