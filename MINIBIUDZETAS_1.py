import pickle

pajamu_listas = []
islaidu_listas = []

try:
    with open("listas.pickle", mode="rb") as file:
        pajamu_listas, islaidu_listas = pickle.load(file)
except (FileNotFoundError, EOFError):
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
        avansas = input("Iveskite avansa: ")
        stipendija = input("Iveskite stipendija: ")
        pajamu_listas.append(f"Atlyginimas: {atlyginimas}")
        pajamu_listas.append(f"Avansas: {avansas}")
        pajamu_listas.append(f"Stipendija: {stipendija}")

    if pasirinkimas == "2":
        nuoma = input("Iveskite busto nuomos islaidas: ")
        komunaliniai = input("Iveskite komunalinias islaidas: ")
        maistas = input("Iveskite maisto islaidas: ")
        islaidu_listas.append(f"Busto nuomos islaidos: {nuoma}")
        islaidu_listas.append(f"Komunalines islaidos: {komunaliniai}")
        islaidu_listas.append(f"Maisto islaidos: {maistas}")

    if pasirinkimas == "3":
        print(pajamu_listas)

    if pasirinkimas == "4":
        print(islaidu_listas)

with open("listas.pickle", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump((pajamu_listas, islaidu_listas), file)

