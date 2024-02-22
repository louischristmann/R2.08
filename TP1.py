class Voiture:
    def __init__(self, marque=None, modele=None, puissance_fiscale=None, couleur=None):
        self.marque = marque
        self.modele = modele
        self.puissance_fiscale = puissance_fiscale
        self.couleur = couleur

if __name__ == "__main__":
    mycar1 = Voiture("renault", "scenic", "2", "rouge")
    print("Attributs de mycar1:")
    print("Marque:", mycar1.marque)
    print("Modèle:", mycar1.modele)
    print("Puissance fiscale:", mycar1.puissance_fiscale)
    print("Couleur:", mycar1.couleur)

    mycar2 = Voiture()
    print("\nAttributs de mycar2:")
    print("Marque:", mycar2.marque)
    print("Modèle:", mycar2.modele)
    print("Puissance fiscale:", mycar2.puissance_fiscale)
    print("Couleur:", mycar2.couleur)

    mycar3 = Voiture("Fiat", "Panda", "2017")
    print("\nAttributs de mycar3:")
    print("Marque:", mycar3.marque)
    print("Modèle:", mycar3.modele)
    print("Puissance fiscale:", mycar3.puissance_fiscale)
    print("Couleur:", mycar3.couleur)

    mycar4 = Voiture(couleur="bleu")
    print("\nAttributs de mycar4:")
    print("Marque:", mycar4.marque)
    print("Modèle:", mycar4.modele)
    print("Puissance fiscale:", mycar4.puissance_fiscale)
    print("Couleur:", mycar4.couleur)
