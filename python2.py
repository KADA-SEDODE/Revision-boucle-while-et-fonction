def demander_age(nom_personne):
    age = 0 
    while age == 0:   
        age_str = input(nom_personne + "Quel est votre âge ? ") 
        try:
            age = int(age_str)
        except:
            print("Erreur : Vous devez entrer un nom pour l'age."
                )    
    return age 
    
# demande de nom  
def demander_nom():
    reponse_nom = ""
    while reponse_nom =="":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom
        

# demande de nom
nom1 = demander_nom()
nom2 = demander_nom()

# demande l'age               
age1 = demander_age(nom1)   
age2 = demander_age(nom2)  

    
print("Vous vous appelez "+ nom1 + ", vous avez " + str(age1) + " ans.")
print("l'an prochain vous aurez "+ str(age1+1) + " ans.")         

print("Vous vous appelez "+ nom2 + ", vous avez " + str(age2) + " ans.")
print("l'an prochain vous aurez "+ str(age2+1) + " ans.")         
       