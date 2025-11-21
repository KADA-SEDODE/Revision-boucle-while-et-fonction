# while condition:
#     bloc d'instruction


# valeur limite
n = int(input("n : "))

#initialiation 
sommePaire = 0
sommeTotale = 0

# Effectuer la somme
i = 1 # ne pas oublier l'initialisation de i

while (i<=n):
    #somme si valeur paire
    if (i/2 ==0):
        sommePaire = sommePaire + i
    # Somme toujours, paire ou pas
    sommeTotale = sommeTotale + i
    #incrementation
    i = i + 1

# affichage avec transtypage
print("Somme des valeur pairs : " + str(sommePaire))
print("Somme totale : " + str(sommeTotale))

# pour bloquer la fermeture de la console
input("pause...")