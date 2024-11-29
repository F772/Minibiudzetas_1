pajamu_listas = []
islaidu_listas = []

while True:
    print("1. Ivesti pajamas\n"
          "2. Ivesti islaidas\n"
          "3. Atspausdinti pajamu eilutes\n"
          "4. Atspausdinti islaidu eilutes\n"
          "5. Atspausdinti statistika\n"
          "q - Iseiti")

    pasirinkimas = input(": ")
    if pasirinkimas == "q":
        break

    if pasirinkimas == "1":
        atlyginimas = input("Iveskite atlyginima: ")
        for elem in atlyginimas:
            pajamu_listas.append(elem)
        avansas = input("Iveskite avansa: ")
        for elem in avansas:
            pajamu_listas.append(elem)
        stipendija = input("Iveskite stipendija: ")
        for elem in stipendija:
            pajamu_listas.append(elem)


