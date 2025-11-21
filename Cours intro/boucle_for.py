# Principe de la boucle for : s'applique sur des sequences de valeurs
# pas une boucle indicé 

# range(4) → 0 1 2 3 
# range(1,4) → 1 2 3 
# range(0,5,2) → 0 2 4 pas=2

# VCaleur limite
n = int(input("n : "))

#initialiation 
sommePaire =0
sommeTotale =0

# Effectuer la somme

for i in range(1,n+1):  # pas 1 automatique et  n+1 n'est pas inclus
    #somme si valeur paire
    if(i/2 ==0):
        sommePaire = sommePaire + i
    # mais on est bien dans le for 
    sommeTotale = sommeTotale + i

# affichage avec transtypage
print("Somme des valeur pairs : " + str(sommePaire))
print("Somme totale : " + str(sommeTotale))

# pour bloquer la fermeture de la console
input("pause...")