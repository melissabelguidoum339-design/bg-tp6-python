# Structure d'un programme Python : imports, fonctions, point d'entree (vu dans le slide 55)
# Indentation obligatoire (vu dans le slide 22)
# Commentaires avec # (vus dans le slide 23)

# Liste C (slide 26) de comptes : chaque compte est un dictionnaire "nom"/"solde" (slides 31-32)
C = [
    {"nom": "compte1", "solde": 3000},
    {"nom": "compte2", "solde": 500},
    {"nom": "compte3", "solde": 1000},
]


# Depot : fonction (slide 40) avec typage (slide 41)
def deposer(c: dict, somme: float) -> dict:
    # Validation du montant : condition (slides 35-36) avec operateurs (slide 34)
    if not isinstance(somme, (int, float)) or somme <= 0:
        return {"erreur": "montant invalide"}
    # Modification d'un dictionnaire (slide 31)
    c["solde"] = c["solde"] + somme
    # Retour d'un resultat JSON (slide 33)
    return {"compte": c["nom"], "solde": c["solde"]}


# Retrait : fonction (slide 40) avec typage (slide 41)
def retirer(c: dict, somme: float) -> dict:
    # Validation du montant : condition (slides 35-36)
    if not isinstance(somme, (int, float)) or somme <= 0:
        return {"erreur": "montant invalide"}
    # Validation du solde suffisant : condition (slides 35-36)
    if somme > c["solde"]:
        return {"erreur": "solde insuffisant"}
    c["solde"] = c["solde"] - somme
    # Retour d'un resultat JSON (slide 33)
    return {"compte": c["nom"], "solde": c["solde"]}


# Solde total : fonction (slide 40) avec typage (slide 41)
def afficher(c: list) -> dict:
    total = 0
    # Boucle for sur une liste (slide 37)
    for compte in c:
        total = total + compte["solde"]
    print("Solde total :", total)
    # Retour d'un resultat JSON (slide 33)
    return {"total": total}


# Comptes avec solde >= 1000 : fonction (slide 40) avec typage (slide 41)
def filtre1000(c: list) -> list:
    # List comprehension (slide 39) avec condition (slide 35)
    return [{"compte": x["nom"], "solde": x["solde"]} for x in c if x["solde"] >= 1000]


# Tri par solde decroissant : fonction (slide 40) avec typage (slide 41)
def trier(c: list) -> list:
    # Fonction lambda (slide 42) utilisee comme cle de tri
    tries = sorted(c, key=lambda x: x["solde"], reverse=True)
    # List comprehension (slide 39) -> liste de dictionnaires JSON (slide 33)
    return [{"compte": x["nom"], "solde": x["solde"]} for x in tries]


# Point d'entree du programme (slide 55)
if __name__ == "__main__":
    print(deposer(C[0], 500))
    print(retirer(C[1], 100))
    print(retirer(C[1], 99999))
    print(afficher(C))
    print(filtre1000(C))
    print(trier(C))
