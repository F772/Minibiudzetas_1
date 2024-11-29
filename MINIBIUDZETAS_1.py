import pickle
import failas.biblioteka
from failas.biblioteka import ivesti_pajamas, ivesti_islaidas, statistika

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
        ivesti_pajamas(pajamu_listas)

    if pasirinkimas == "2":
        ivesti_islaidas(islaidu_listas)

    if pasirinkimas == "3":
        print(pajamu_listas)

    if pasirinkimas == "4":
        print(islaidu_listas)

    if pasirinkimas == "5":
        pajamu_suma, islaidu_suma, galutine_suma = statistika(pajamu_listas, islaidu_listas)
        print(f"Galutine suma: {galutine_suma}")
        print(f"Pajamu suma: {pajamu_suma}")
        print(f"Islaidu suma: {islaidu_suma}")

with open("listas.pickle", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump((pajamu_listas, islaidu_listas), file)
