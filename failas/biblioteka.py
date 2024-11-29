import datetime


def ivesti_pajamas(pajamu_listas):
    while True:
        data = input("Iveskite data kaip pvz (YY-MM-DD): ")
        try:
            data_obj = datetime.datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            print("Iveskite data kaip pvz!")
            continue
        pavadinimas = input("Iveskite pajamu pavadinima: ")
        suma = float(input("Iveskite pajamu suma: "))
        pajamu_listas.append([data, pavadinimas, suma])
        break


def ivesti_islaidas(islaidu_listas):
    while True:
        data = input("Iveskite data kaip pvz (YY-MM-DD): ")
        try:
            data_obj = datetime.datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            print("Iveskite data kaip pvz!")
            continue
        pavadinimas = input("Iveskite islaidu pavadinima: ")
        suma = float(input("Iveskite islaidu suma: "))
        islaidu_listas.append([data, pavadinimas, suma])
        break


def statistika(pajamu_listas, islaidu_listas):
        pajamu_suma = sum([(elem[2]) for elem in pajamu_listas])
        islaidu_suma = sum([(elem[2]) for elem in islaidu_listas])
        galutine_suma = pajamu_suma - islaidu_suma
        return pajamu_suma, islaidu_suma, galutine_suma
