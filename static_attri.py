class Eleve:
    nbre = 0

    def __init__(self, nom_prenom):
        Eleve.nbre += 1
        self.nom_prenom = nom_prenom

        print(f"Eleve n°{self.nbre} : {self.nom_prenom}")


el1 = Eleve("Ayoub Mlika")
el2 = Eleve("Ali Arfaoui")
el3 = Eleve("Aziz Ferjani")

print(Eleve.nbre)
print(el1.nbre)
print(el2.nbre)
print(el3.nbre)
