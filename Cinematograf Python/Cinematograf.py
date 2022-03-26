from Drama import Drama
from Animatie import Animatie
import random,sys

class Cinematograf(object):
    def __init__(self,lista_filme = None):
        if lista_filme:
            self.lista_filme = lista_filme
        else:
            self.lista_filme = []

    def adauga_drama(self):
        global durata
        print("Introduceti informatiile despre drama pe care doriti sa o adaugati: ")
        titlu = input("Titlu: ")
        while True:
            try:
                durata = int(input("Durata(nr. de minute): "))
                if durata > 180:
                    raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute.")
            except ValueError as e:
                print(repr(e))
                print("Reincercati sa introduceti o durata valida!")
                continue
            break
        varsta_minima = input("Varsta minima: ")
        drama_adaugata = Drama(titlu, durata, varsta_minima)

        self.lista_filme.append(drama_adaugata)
        print(f"Filmul {titlu} a fost adaugat in lista. Va multumim!")

    def adauga_animatie(self):
        global durata
        print("Introduceti informatiile despre animatia pe care doriti sa o adaugati: ")
        titlu = input("Titlu: ")
        while True:

            try:
                durata = int(input("Durata(nr. de minute): "))
                if durata > 180:
                    raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute.")
            except ValueError as e:
                print(repr(e))
                print("Reincercati sa introduceti o durata valida!")
                continue
            break
        limba_dublare = input("Introduceti limba in care se face dublarea: ")
        animatie_adaugata = Animatie(titlu, durata, limba_dublare)
        self.lista_filme.append(animatie_adaugata)
        print(f"Filmul {titlu} a fost adaugat in lista. Va multumim!")

    def afisare(self):
        if self.lista_filme:
            for film in self.lista_filme:
                if isinstance(film,Drama):
                    print(f"Numele filmului: {film.titlu}," + f"Durata: {film.durata}," + f"Varsta minima: {film.varsta_minima}")
                if isinstance(film, Animatie):
                    print(f"Numele filmului: {film.titlu}," + f"Durata: {film.durata}," + f"Limba dublare: {film.dublare()}")

        else:
            print("Nu exista filme de afisat!")


    def afisare_animatii(self):

        semafor = 0
        for film in self.lista_filme:
            if isinstance(film, Animatie):
                semafor = 1
                break

        if semafor == 0:
            print("Nu exista animatii de afisat!")
        else:
            for film in self.lista_filme:
                if isinstance(film, Animatie):
                    print(f"Numele filmului: {film.titlu}," + f"Durata: {film.durata}," + f"Limba dublare: {film.dublare()}")

    def alege_film(self):

        if self.lista_filme:
             film = random.choice(self.lista_filme)
             if isinstance(film, Drama):
                 print(
                     f"Numele filmului: {film.titlu}," + f"Durata: {film.durata}," + f"Varsta minima: {film.varsta_minima}")
             if isinstance(film, Animatie):
                 print(
                     f"Numele filmului: {film.titlu}," + f"Durata: {film.durata}," + f"Limba dublare: {film.dublare()}")

    def salveaza_filme(self):
        nume_fisier = input("Specificati numele fisierului: ")
        with open(file=nume_fisier, mode = "wt") as fisier:
            if self.lista_filme:
                for film in self.lista_filme:
                    if isinstance(film, Drama):
                        fisier.write(f"Numele filmului: {film.titlu}," + f"Durata: {film.durata}," + f"Varsta minima: {film.varsta_minima}\n")
                    if isinstance(film, Animatie):
                        fisier.write(f"Numele filmului: {film.titlu}," + f"Durata: {film.durata}," + f"Limba dublare: {film.dublare()}\n")

            else:
                fisier.write("Nu exista filme salvate!")

    def exit(self):
        print("Programul se va inchide. Va multumim!")
        sys.exit(0)
