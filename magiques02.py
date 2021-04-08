NBRES_A_99 = [
    'zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept',
    'huit', 'neuf', 'dix', 'onze', 'douze', 'treize', 'quatorze',
    'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf', 'vingt',
    'vingt-et-un', 'vingt-deux', 'vingt-trois', 'vingt-quatre',
    'vingt-cinq', 'vingt-six', 'vingt-sept', 'vingt-huit',
    'vingt-neuf', 'trente', 'trente-et-un', 'trente-deux',
    'trente-trois', 'trente-quatre', 'trente-cinq', 'trente-six',
    'trente-sept', 'trente-huit', 'trente-neuf', 'quarante',
    'quarante-et-un', 'quarante-deux', 'quarante-trois',
    'quarante-quatre', 'quarante-cinq', 'quarante-six',
    'quarante-sept', 'quarante-huit', 'quarante-neuf', 'cinquante',
    'cinquante-et-un', 'cinquante-deux', 'cinquante-trois',
    'cinquante-quatre', 'cinquante-cinq', 'cinquante-six',
    'cinquante-sept', 'cinquante-huit', 'cinquante-neuf', 'soixante',
    'soixante-et-un', 'soixante-deux', 'soixante-trois', 'soixante-quatre',
    'soixante-cinq', 'soixante-six', 'soixante-sept', 'soixante-huit',
    'soixante-neuf', 'soixante-dix', 'soixante-et-onze', 'soixante-douze',
    'soixante-treize', 'soixante-quatorze', 'soixante-quinze',
    'soixante-seize', 'soixante-dix-sept', 'soixante-dix-huit',
    'soixante-dix-neuf', 'quatre-vingt', 'quatre-vingt-et-un',
    'quatre-vingt-deux', 'quatre-vingt-trois', 'quatre-vingt-quatre',
    'quatre-vingt-cinq', 'quatre-vingt-six', 'quatre-vingt-sept',
    'quatre-vingt-huit', 'quatre-vingt-neuf', 'quatre-vingt-dix',
    'quatre-vingt-et-onze', 'quatre-vingt-douze', 'quatre-vingt-treize',
    'quatre-vingt-quatorze', 'quatre-vingt-quinze', 'quatre-vingt-seize',
    'quatre-vingt-dix-sept', 'quatre-vingt-dix-huit',
    'quatre-vingt-dix-neuf'
]


class Numerals:
    def __init__(self, val):
        self.val = self.convert_to_int(val)

    @staticmethod
    def convert_to_int(val):
        if type(val) == int:
            return val
        elif type(val) == str:
            if val.lower() in NBRES_A_99:
                return NBRES_A_99.index(val.lower())
            raise UnboundLocalError(f"Nombre inconnu {val}")
        elif isinstance(val, Numerals):
            return val.val

    def __add__(self, val):
        return Numerals(self.val + self.convert_to_int(val))

    def __sub__(self, val):
        return Numerals(self.val - self.convert_to_int(val))

    def __str__(self):
        return(NBRES_A_99[self.val]
               if 0 <= self.val < len(NBRES_A_99)
               else "Invalide")


n1 = Numerals('cinq')
n2 = Numerals('dix')
n3 = n1 + n2
n4 = n3 + Numerals('quarante')
n5 = n4 - 6
print(n1)
print(n2)
print(f"{n1} + {n2} = {n3}")
print(f"{n3} + quarante = {n4}")
print(f"{n4} - 6 = {n5}")
