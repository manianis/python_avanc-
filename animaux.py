class Animal:
    def __init__(self, categorie, nom, aliments):
        self.categorie = categorie
        self.nom = nom
        self.aliments = aliments

    def manger(self):
        alim = ", ".join(self.aliments)
        print(f"Le {self.nom} est un {self.categorie} il mange {alim}")


class Herbivore(Animal):
    def __init__(self, nom, aliments):
        Animal.__init__(self, 'Herbivore', nom, aliments)


class Carnivore(Animal):
    def __init__(self, nom, aliments):
        Animal.__init__(self, 'Carnivore', nom, aliments)


class Omnivore(Animal):
    def __init__(self, nom, aliments):
        Animal.__init__(self, 'Omnivore', nom, aliments)


class Lapin(Herbivore):
    def __init__(self):
        Herbivore.__init__(self, "Lapin", ["Carottes", "Avoine"])


class Lion(Carnivore):
    def __init__(self):
        Carnivore.__init__(self, "Lion", ["Viandes"])


class Hyene(Carnivore):
    def __init__(self):
        Carnivore.__init__(self, "Hyene", ["Cadavres", "Viandes"])


class Homme(Carnivore):
    def __init__(self):
        Carnivore.__init__(self, "Homme", ["Viandes", "Fruits", "Légumes"])


# PP
lap = Lapin()
lap.manger()

leo = Lion()
leo.manger()

hyn = Hyene()
hyn.manger()

hum = Homme()
hum.manger()
