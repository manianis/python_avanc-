class Calcul:
    @staticmethod
    def somme(a, b):
        return a + b

    @staticmethod
    def prod(a, b):
        return a * b


calc = Calcul()
print(calc.somme(6, 3))
print(calc.prod(5, 8))

print(Calcul.somme(6, 3))
print(Calcul.prod(5, 8))
