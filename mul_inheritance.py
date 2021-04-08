class Animal:
    def __init__(self):
        super().__init__()
        print("Animal.__init__()")


class Herbivore(Animal):
    def __init__(self):
        super().__init__()
        print("Herbivore.__init__()")


class Carnivore(Animal):
    def __init__(self):
        super().__init__()
        print("Carnivore.__init__()")


class Omnivore(Herbivore, Carnivore):
    def __init__(self):
        super().__init__()
        print("Omnivore.__init__()")


humain = Omnivore()
