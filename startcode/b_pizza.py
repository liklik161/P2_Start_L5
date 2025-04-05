class Pizza:
    def __init__(self, naam, grootte, toppings):
        self.naam = naam
        self.grootte = grootte
        self.toppings = toppings
        self.prijs = self.bereken_prijs()
    def bereken_prijs(self):
        basis_klein = 8.99
        basis_medium = 10.99
        basis_groot = 12.99
        topping = 1.50
        if self.grootte == "klein":
            prijs = basis_klein
        if self.grootte == "medium":
            prijs = basis_medium
        if self.grootte == "groot":
            prijs = basis_groot
        prijs += len(self.toppings)*topping
        return prijs

    def info_pizza(self):
        print(f"naam: {self.naam}")
        print(f"grootte: {self.grootte}")
        for inhoud in self.toppings:
            print(f"toppings: {inhoud}")
        print(f"prijs: {self.prijs}")


pizza1 = Pizza("margherita", "medium", ["tomatensaus", "kaas"])
pizza2 = Pizza("hawaii", "klein", ["ananas", "salami"])

pizza1.info_pizza()
pizza2.info_pizza()

