from Cinematograf import Cinematograf

if __name__ == "__main__":
    cinematograf = Cinematograf()
    print("Bine ati venit!")
    while True:

        comanda = input("\nIntroduceti o comanda: ")

        if comanda == "adauga_drama":
            cinematograf.adauga_drama()

        elif comanda == "adauga_animatie":
            cinematograf.adauga_animatie()
        elif comanda == "afisare":
            cinematograf.afisare()
        elif comanda == "afisare_animatii":
            cinematograf.afisare_animatii()
        elif comanda == "alege_film":
            cinematograf.alege_film()
        elif comanda == "salveaza_filme":
            cinematograf.salveaza_filme()
        elif comanda == "exit":
            cinematograf.exit()
        else:
            print("Ati introdus o comanda invalida. Reincercati!\n")