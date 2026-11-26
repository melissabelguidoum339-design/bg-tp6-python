# Structure d'un programme Python : imports, fonctions, point d'entree (vu dans le slide 55)
# Indentation obligatoire (vu dans le slide 22)
# Commentaires avec # (vus dans le slide 23)

# Liste (slide 26) de tuples (slide 28) : (mat, nom, prenom, note, autre)
students = [
    (1000, "JOHN", "DOE", 14, 5),
    (2000, "BOB", "CARLTON", 7, 1),
    (3000, "RAYANE", "SMITH", 13, 3),
]


# Fonction B : definition de fonction (slide 40) avec typage (slide 41)
def B(note: float) -> bool:
    # Operateur de comparaison (slide 34) dans une condition (slide 35)
    return note >= 10


# Fonction A : appelle B et retourne une liste de dictionnaires JSON
# Fonction (slide 40) avec typage (slide 41)
def A(students: list) -> list:
    result = []
    # Boucle for (slide 37) avec deballage de tuple (slide 28)
    for mat, nom, prenom, note, autre in students:
        # Appel de la fonction B (slide 40) dans une condition if/else (slides 35-36)
        if B(float(note)):
            statut = "ADMIS"
        else:
            statut = "AJOURNE"
        # Dictionnaire (slide 31) ajoute a une liste de dictionnaires (slides 32-33)
        result.append({"mat": mat, "result": statut})
    return result


# Fonction C : appelle B puis affiche les resultats avec print()
# Fonction (slide 40)
def C():
    # Boucle for (slide 37) avec deballage de tuple (slide 28)
    for mat, nom, prenom, note, autre in students:
        # Appel de B (slide 40) dans une condition if/else (slides 35-36)
        if B(float(note)):
            print(f"{mat}: ADMIS")
        else:
            print(f"{mat}: AJOURNE")


# Point d'entree du programme (slide 55)
if __name__ == "__main__":
    print(A(students))
    C()
