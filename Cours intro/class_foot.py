# 1) Classe Joueur — le modèle général

class Joueur:
    def __init__(self, nom, numero, vitesse):
        self.nom = nom
        self.numero = numero
        self.vitesse = vitesse

    def jouer(self):
        print(self.nom, "participe à l’action.")
# “Toute personne dans l’équipe est un joueur avec un nom, un numéro et une vitesse.”

# 2) Classe Attaquant — hérite de Joueur

class Attaquant(Joueur):
    def marquer(self):
        print(self.nom, "marque un but !")

    def jouer(self):
        print(self.nom, "attaque et tente de tirer au but.")

# Il hérite de Joueur → il a nom, numéro, vitesse
# Il a des actions en plus : marquer()
# Il modifie la méthode jouer() → polymorphisme

# 3) Classe Gardien — hérite de Joueur

class Gardien(Joueur):
    def arreter(self):
        print(self.nom, "arrête le ballon !")

    def jouer(self):
        print(self.nom, "protège les cages.")

# Hérite de Joueur
# Action spécifique : arrêter()
# Sa manière de “jouer” n’est pas la même → polymorphisme

# 4) Création des objets (les joueurs réels)

mbappe = Attaquant("Mbappé", 10, 96)
onana = Gardien("Onana", 24, 60)

# 5) Actions des joueurs

mbappe.jouer()     # version attaquant
mbappe.marquer()

onana.jouer()      # version gardien
onana.arreter()

# La même méthode jouer() donne deux comportements différents
# → polymorphisme