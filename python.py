# print("Bonjour le monde!")

# # concept de base de la programmation en Python

# # nom = "koffi"
# # print("Je m'appelle " + nom + ".") # CONCATENER

# # nom = input ("quel est ton nom ?")

# # print("Vous vous appellez" + nom + ".")

# # print("Vous vous appelez toto, vous avez 30 ans")
# # nom = input("Quel est votre nom ? ")
# # age = input("Quel est votre âge ? ")
# # print("Vous vous appellez "+ nom, ", vous avez " + age + " ans.")
# # age = 31
# # str_age = str(age) # convertir un entier en chaine de caractere
# # print(type(str_age))
# """
# nom = input("Quel est votre nom ? ")
# age = input("Quel est votre âge ? ")

# try:
#     age_prochain = int(age) + 1
# except:
#     print("Erreur : L'âge doit être un nombre entier."
#           )    
# else:
#     print("Vous vous appelez "+ nom, ", vous avez " + str(age) + " ans.")
#     print("l'an prochain vous aurez "+ str(age_prochain) + " ans.")

# # age = 31
# # int_age = int(age) # convertir un entier en chaine de caractere
# # print(type(int_age) """

# """Boucle while tant que """

# n = 0  
# # print(n)
# # n = 1  
# # print(n)
# # n = n + 1
# # print(n)
# # print("Début de la boucle")
# # while n < 4 :
# #     print("valeur de n: " + str(n))
# #     n = n + 1

# # mot_de_passe = ""
# # while not mot_de_passe =="TOTO":
# #     mot_de_passe  = input("Quel est votre mot de passe ? ")

# # print("Mot de passe correct, vous avez acces au compte")

# # nom = input("Quel est votre nom ? ")








    








# # demande de nom  
# nom = ""
# while nom =="":
#     nom_str = input("Quel est votre nom ? ")
    
    
# # demande l'age     
# age = 0 
# while age == 0:   
#     age_str = input("Quel est votre âge ? ") 
#     try:
#         nom = int(age_str)
#     except:
#         print("Erreur : Vous devez entrer un nom pour l'age."
#             )    
# print("fin de la boucle")        
        
# # else:
# # Afficher les resultats
# print("Vous vous appelez "+ nom, ", vous avez " + str(age) + " ans.")
# # print("l'an prochain vous aurez "+ str(age+1) + " ans.")



def demander_age():
    age = 0 
    while age == 0:   
        age_str = input("Quel est votre âge ? ") 
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
        

                
age = demander_age()   
nom = demander_nom()

print("Vous vous appelez "+ nom, ", vous avez " + str(age) + " ans.")
print("l'an prochain vous aurez "+ str(age+1) + " ans.")
         
         
# Variable globale parametre         