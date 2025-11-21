# a = 12==13
# print(a)

# OPERATEUR d'entrée et sortie

# a = input("Quel est votre taille ? ")
# a = float(a)

# STRUCTURES ALGORITHMIQUES

# Branchement conditionnel « if » : souvent operation de comparaison
# nbre = -5

# if nbre > 0:
#     print("x est positif")
# else:
#     print("est négatif")    
    
# saisie à la conole d'un prix HT
pht = float(input("prix HT : "))

# code produit 
code = int(input("code produit : "))

# action conditionnelle 

if (code == 1):
    taxe = pht * 0.055
    pttc = pht + taxe
elif (code == 2):  # elif n’est déclenché que si la (les) condition(s) précédente(s) a (ont) échoué.    
    pttc = pht * 1.1    
else:
    pttc = pht * 1.2
    
# affichage avec trabstypage
print("prix TTC : " + str(pttc))

# POUR BLOQUER La ferleture de la console
input("pause...")        
    
    
