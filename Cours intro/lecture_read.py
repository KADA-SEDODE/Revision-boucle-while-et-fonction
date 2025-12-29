f = open("voitures.txt" , "r")

s = f.read()

# affichage du contenu
print("** contenu de s **")
print(s)
print("** fin contenu **")

# informations sur la variable s
print("type de s :", type(s))
print("longueur de s :", len(s))

# fermeture du fichier
f.close()