# JSON = fichier texte
# structure standardisée
# utilisé pour : échange de données entre applications   APIs  configs
# JSON = listes + dictionnaires

# json_basics.py
import json

personnes = [
    {"nom": "Toto", "age": 34, "salaire": 1250},
    {"nom": "Tata", "age": 43, "salaire": 2600}
]
# Sauvegarder  
with open("personnes.json", "w", encoding="utf-8") as f:
    json.dump(personnes, f, indent=2)
# charger 
with open("personnes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
