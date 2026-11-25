
import json
def deposer(c: dict, somme: float) -> str:
    
    if somme > 0:
        
        c["solde"] += somme
        
    
    resultat = {"compte": c["nom"], "solde": c["solde"]}
    
    return json.dumps(resultat)


def retirer(c: dict, somme: float) -> str:
    
    if somme > 0 and c["solde"] >= somme:
        
        c["solde"] -= somme
        
    
    resultat = {"compte": c["nom"], "solde": c["solde"]}
    
    return json.dumps(resultat)


def afficher(c: list) -> str:

    total = 0
    
    
    for compte in c:
        total += compte["solde"]
        
    
    print(f"Solde total de tous les comptes : {total}")
    # Retour du résultat encodé en JSON (Slide 33)
    return json.dumps({"total": total})


def filtre1000(c: list) -> str:
    
    comptes_filtres = [
        {"compte": compte["nom"], "solde": compte["solde"]}
        for compte in c
        if compte["solde"] >= 1000
    ]
    
    return json.dumps(comptes_filtres)

# 5. Fonction de tri des comptes par solde décroissant retournant un JSON (Slide 33, 40 & 42)
def trier_comptes(c: list) -> str:
    
    comptes_tries = sorted(c, key=lambda x: x["solde"], reverse=True)
    
    
    resultat = [{"compte": compte["nom"], "solde": compte["solde"]} for compte in comptes_tries]
    # Encodage en JSON (Slide 33)
    return json.dumps(resultat)

if __name__ == "__main__":
    
    C = [
        {"nom": "compte1", "solde": 500},
        {"nom": "compte2", "solde": 1500},
        {"nom": "compte3", "solde": 2500},
        {"nom": "compte4", "solde": 800}
    ]
    
    
    print(deposer(C[0], 500))
    print(retirer(C[1], 300))
    print(afficher(C))
    print(filtre1000(C))
    print(trier_comptes(C))
