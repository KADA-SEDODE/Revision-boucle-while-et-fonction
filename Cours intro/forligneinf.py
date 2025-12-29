with open("voitures.txt" , "r") as f:
    for ligne in f:
        print(ligne.strip(), len(ligne))
        
# .strip() enlève \n        
# with ferme automatiquement le fichier