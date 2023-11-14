

def go():
    lista = "a s d".split(" ")

    total_iter = len(lista)*3 + 1

    index = 0
    while total_iter != 0:
        item = lista[index]

        index = (index+1)%len(lista)

        total_iter -= 1


if __name__ == "__main__":
    go()
