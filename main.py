from aplikace import Aplikace

aplikace = Aplikace()

while True:
    print("Evidence pojištěných\n---------------------------")
    print("1 - Přidat pojištěného")
    print("2 - Vyhledat pojištěného")
    print("3 - Vypis pojištěných")
    print("4 - Konec")
    volba = input("Zadejte číslo volby:")
    if volba == "1":
        aplikace.pridat_pojisteneho()
    elif volba == "2":
        pojisteny = aplikace.vyhledat_pojisteneho()
        if pojisteny is None:
            print("Vámi hledaný není v evidenci pojištěných.")
        else:
            print(pojisteny)
    elif volba == "3":
        aplikace.vypis_pojistenych()
    elif volba == "4":
        print("Konec aplikace")
        break
    else:
        print("Neplatná volba.")