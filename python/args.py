def rzeczy(*args):
    for i in args:
        print(i)

rzeczy('litera', "string", "float")

print("$" * 30)

def rzeczy(pierwsza_rzecz, *args):
    print(pierwsza_rzecz)
    print(args[0])
    for i in args:
        print(i)

rzeczy('litera', "string", "float", "number")