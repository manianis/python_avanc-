class EnRotationException(Exception):
    pass


class Moteur:
    def __init__(self, vitesse_max):
        self.vitesse = 0.0
        self.vitesse_max = vitesse_max
        self.roues = []
        self.direction = 1
        self.coef_vitesse = 1.0

    def _enRotationException(self):
        if self.vitesse != 0:
            raise EnRotationException("Ne peut pas faire cette opération lorsque le moteur tourne.")

    def directionDroite(self):
        if self.direction != 1:
            self._enRotationException()
        self.direction = 1

    def directionGauche(self):
        if self.direction != -1:
            self._enRotationException()
        self.direction = -1

    def coefficientVitesse(self, coef_vitesse):
        coef_vitesse = min(max(0.0, coef_vitesse), 1.0)
        if coef_vitesse != self.coef_vitesse:
            self.coef_vitesse = coef_vitesse
            self.entrainer()

    def turnOn(self):
        self.vitesse = self.direction * self.vitesse_max * self.coef_vitesse
        self.entrainer()

    def turnOff(self):
        self.vitesse = 0.0
        self.entrainer()

    def entrainer(self):
        for roue in self.roues:
            roue.tourner(self.vitesse)

    def monter(self, roue):
        self._enRotationException()
        if roue not in self.roues:
            self.roues.append(roue)
        self.entrainer()

    def demonter(self, roue):
        self._enRotationException()
        if roue in self.roues:
            roue.tourner(0.0)
            self.roues.remove(roue)

    def __str__(self):
        return f"Moteur\nVitesse : {self.vitesse}\n"


class RoueDentee:
    def __init__(self, nom, diametre):
        self.nom = nom
        self.diametre = diametre
        self.vitesse = 0.0
        self.colles = []
        self.voisins = []

    def _enRotationException(self):
        if self.vitesse != 0.0:
            raise EnRotationException("Ne peut pas faire cette opération lorsque le moteur tourne.")

    def enRotation(self):
        return self.vitesse != 0.0

    def tourner(self, vitesse):
        if vitesse != self.vitesse:
            self.vitesse = vitesse
            self.entrainer()

    def entrainer(self):
        for roue in self.voisins:
            roue.tourner(-self.vitesse * self.diametre / roue.diametre)
        for roue in self.colles:
            roue.tourner(self.vitesse)

    def coller(self, roue):
        self._enRotationException()
        if roue not in self.colles:
            self.colles.append(roue)
            roue.coller(self)

    def decoller(self, roue):
        self._enRotationException()
        if roue in self.colles:
            self.colles.remove(roue)
            roue.decoller(self)

    def engrainer(self, roue):
        self._enRotationException()
        if roue not in self.voisins:
            self.voisins.append(roue)
            roue.engrainer(self)

    def desengrainer(self, roue):
        self._enRotationException()
        if roue in self.voisins:
            self.voisins.remove(roue)
            roue.desengrainer(self)

    def __str__(self):
        return f"{self.nom}\nDiamètre : {self.diametre}\nVitesse : {self.vitesse}\n"


moteur = Moteur(1500)
roue1 = RoueDentee("roue 1", 10)
moteur.monter(roue1)

roue21 = RoueDentee("roue 21", 100)
roue1.engrainer(roue21)

roue22 = RoueDentee("roue 22", 10)
roue21.coller(roue22)

roue3 = RoueDentee("roue 3", 100)
roue22.engrainer(roue3)

moteur.turnOn()
print(f"Moteur entraine {roue1.nom}, en rotation")
print(moteur)
print(roue1)
print(roue21)
print(roue22)
print(roue3)
print()

moteur.turnOff()
print(f"Moteur entraine {roue1.nom}, arrêté")
print(moteur)
print(roue1)
print(roue21)
print(roue22)
print(roue3)
print()

moteur.demonter(roue1)
moteur.monter(roue3)

moteur.coefficientVitesse(0.005)
moteur.turnOn()
print(f"Moteur entraine {roue3.nom}, en rotation")
print(moteur)
print(roue1)
print(roue21)
print(roue22)
print(roue3)
print()

moteur.turnOff()
moteur.demonter(roue3)
moteur.monter(roue21)

moteur.coefficientVitesse(0.1)
moteur.turnOn()
print(f"Moteur entraine {roue21.nom}, en rotation")
print(moteur)
print(roue1)
print(roue21)
print(roue22)
print(roue3)
print()

moteur.turnOff()
roue21.decoller(roue22)

moteur.turnOn()
print(f"Moteur entraine {roue21.nom}, en rotation")
print(moteur)
print(roue1)
print(roue21)
print(roue22)
print(roue3)
print()
