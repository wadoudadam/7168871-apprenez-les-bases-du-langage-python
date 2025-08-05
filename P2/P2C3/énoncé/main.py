def salaire_mensuel(salaire_annuel):
    mens=salaire_annuel/12

    return mens

def salaire_hebdomadaire(mens):
    heb=mens/4

    return heb

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    hor=salaire_hebdomadaire/heures_travaillees
    return hor




salaire_an= (input("Entrez votre salaire: "))
heure= (input("Entrez le nombre d'heure de travail par semaine: "))
salaire_an=float(salaire_an)
heure=float(heure)
print(salaire_an, heure)
print(f" Votre salaire horaire est de {salaire_horaire(salaire_hebdomadaire(salaire_mensuel(salaire_an)), heure)} FCFA")

