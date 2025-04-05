class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")
kat = Dier("kat", "miauw")
kat.maak_geluid()
hond = Dier("hond", "woef")
hond.maak_geluid()
koe = Dier("koe", "moo")
koe.maak_geluid()