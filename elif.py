"""Fonction  pour afficher  les infos d'un personne"""
def afficher_info_personne(nom, age):
    print()
    print("Vous vous appelez "+ nom + ", vous avez " + str(age) + " ans.")
    print("l'an prochain vous aurez "+ str(age + 1) + " ans.")  
    
    # age == 17 -> vous etre presque majeur
    # age == 18 -> vous etes tout juste majeur
    
    #elif = sinon si, il est exclusif
    if age == 17 :
        print("Vous êtes presque majeur.")
    elif age == 18 :
        print("Tout juste majeur : felicitation")        
        
    elif age >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")

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
        

# # demande de nom
nom1 = demander_nom()
nom2 = demander_nom()

# demande l'age               
age1 = demander_age(nom1)   
age2 = demander_age(nom2)  

afficher_info_personne(nom1, age1)
afficher_info_personne(nom2, age2)