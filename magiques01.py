from random import randint


class Eleve:
    def __init__(self, nom_prenom):
        self.nom_prenom = nom_prenom

    def __str__(self):
        return f"{self.nom_prenom:32}"

    def __repr__(self):
        return f"Eleve(nom_prenom: {self.nom_prenom:45})"


class Devoir:
    def __init__(self, devoir, coef):
        self.devoir = devoir
        self.coef = coef

    def __str__(self):
        return f"Devoir : {self.devoir}, Coef : {self.coef}"

    def __repr__(self):
        return f"Devoir(devoir: {self.devoir}, coef: {self.coef})"


class EleveCollection:
    def __init__(self):
        self.eleves = []

    def __len__(self):
        return len(self.eleves)

    def __getitem__(self, index):
        return self.eleves[index]

    def __setitem__(self, index, eleve):
        self.eleves[index] = eleve

    def __contains__(self, eleve):
        for el in self.eleves:
            if el.nom_prenom == eleve.nom_prenom:
                return True
        return False

    def __add__(self, eleve):
        if eleve not in self:
            self.eleves.append(eleve)
        return self

    def __str__(self):
        s = "Liste des élèves :\n"
        if len(self.eleves) == 0:
            s += "Aucun élève."
            return s
        for idx, eleve in enumerate(self.eleves):
            s += f"{idx+1:2}. {eleve}\n"
        return s


class DevoirCollection:
    def __init__(self):
        self.devoirs = []

    def __len__(self):
        return len(self.devoirs)

    def __getitem__(self, index):
        return self.devoirs[index]

    def __setitem__(self, index, eleve):
        self.devoirs[index] = eleve

    def __contains__(self, devoir):
        for dev in self.devoirs:
            if dev.devoir == devoir.devoir:
                return True
        return False

    def __add__(self, devoir):
        if devoir not in self:
            self.devoirs.append(devoir)
        return self

    def __str__(self):
        s = "Liste des Devoirs :\n"
        if len(self.devoirs) == 0:
            s += "Aucun devoir."
            return s
        for idx, devoir in enumerate(self.devoirs):
            s += f"{idx+1:2}. {devoir.devoir} {devoir.coef:3.1f}\n"
        return s


class Classe:
    def __init__(self, libelle):
        self.libelle = libelle
        self.eleves = EleveCollection()
        self.devoirs = DevoirCollection()
        self.notes = {}
        self.init_notes()

    def init_notes(self):
        for el in self.eleves:
            for dev in self.devoirs:
                key = f"{el.nom_prenom}_{dev.devoir}"
                if key not in self.notes:
                    self.notes[key] = 0.0

    def __add__(self, obj):
        if isinstance(obj, Eleve):
            self.eleves += obj
        if isinstance(obj, Devoir):
            self.devoirs += obj
        self.init_notes()
        return self

    def get_key_by_index(self, idxel, idxdev):
        return f"{self.eleves[idxel].nom_prenom}_{self.devoirs[idxdev].devoir}"

    def get_tuple(self, idxel):
        return tuple([idxel, self.eleves[idxel].nom_prenom] +
                     [self.notes[self.get_key_by_index(idxel, idxdev)] 
                      for idxdev in range(len(self.devoirs))] +
                     [self.get_moyenne(idxel)])

    def get_col_index(self, colname):
        if colname == "Elève":
            return 1
        elif colname == "MOY":
            return 2 + len(self.devoirs)
        else:
            for idx, dev in enumerate(self.devoirs):
                if dev.devoir == colname:
                    return idx + 2
        return -1

    def sort_by(self, colname, descending=False):
        colidx = self.get_col_index(colname)
        if colidx == -1:
            return
        lst = [self.get_tuple(idxel) for idxel in range(len(self.eleves))]
        lst.sort(key=lambda t: t[colidx], reverse=descending)
        eleves = EleveCollection()
        for t in lst:
            eleves += self.eleves[t[0]]
        self.eleves = eleves
        self.init_notes()

    def set_note(self, idxel, idxdev, note):
        key = self.get_key_by_index(idxel, idxdev)
        self.notes[key] = note

    def get_note(self, idxel, idxdev):
        key = self.get_key_by_index(idxel, idxdev)
        return self.notes[key]

    def get_moyenne(self, idxel):
        sn, sc = 0.0, 0.0
        for idxdev, dev in enumerate(self.devoirs):
            key = self.get_key_by_index(idxel, idxdev)
            sn += self.notes[key] * dev.coef
            sc += dev.coef
        if sc == 0.0:
            return 0.0
        return sn / sc

    def __str__(self):
        s = f"Liste des notes des élèves {self.libelle} :\n"
        if len(self.eleves) == 0:
            s += "Aucun élève."
            return s
        s += " " * 4 + f"{'Elève':32}"
        for idxdev, dev in enumerate(self.devoirs):
            s += f"{dev.devoir[:5]:>6}"
        s += "   MOY\n"
        for idxel, eleve in enumerate(self.eleves):
            s += f"{idxel+1:2}. {eleve}"
            for idxdev, dev in enumerate(self.devoirs):
                key = self.get_key_by_index(idxel, idxdev)
                s += f" {self.notes[key]:5.2f}"
            s += f" {self.get_moyenne(idxel):5.2f}\n"
        return s


clse = Classe('2TI')

clse += Eleve("Ahmed Ammar")
clse += Eleve("Ayoub Mlika")
clse += Eleve("Ahmed Khadrouf")
clse += Eleve("Adem Moussa")
clse += Eleve("Montassar Hachfi")
clse += Eleve("Ali Arfaoui")
clse += Eleve("Ali Gueder")

clse += Devoir("DC", 1.0)
clse += Devoir("TP", 1.0)

nbreel = len(clse.eleves)
nbredev = len(clse.devoirs)

for i in range(nbreel):
    for j in range(nbredev):
        clse.set_note(i, j, randint(20, 40) * 0.5)

print(clse)

clse += Devoir("DS", 2.0)

nbreel = len(clse.eleves)
nbredev = len(clse.devoirs)

for i in range(nbreel):
    for j in range(nbredev):
        clse.set_note(i, j, randint(20, 40) * 0.5)

print(clse)

clse.sort_by('MOY', True)
print(clse)

clse.sort_by('DS', True)
print(clse)
