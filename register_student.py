import time
from get_uid import get_uid
from models import Carte
from afficher_etudiant import afficher_etudiant, etudiant_existe, afficher_liste_etudiants


def register_student():
    """
    Fonction pour enregistrer un nouvel étudiant au niveau de la base de données.
    """
    i = 0
    while i < 2:
        afficher_liste_etudiants()
        print("*******ENREGISTREMENT D'UN NOUVEL ETUDIANT *********\n\n")
        prenom = input("Entrer le prénom de l'étudiant: ")
        nom = input("Entrer le nom de l'étudiant: ")
        solde = int(input("Entrer le solde de l'étudiant : "))
        id_carte = get_uid()
        
        
        if etudiant_existe(id_carte):
            Carte.update_etudiant(id_carte, prenom, nom, solde)
            print("\nMise à jour des informations ...")
            print("\n********Enregistrment terminé!*********")
        
        else:
            Carte.register_student_to_bd({
                "prenom": prenom,
                "nom": nom,
                "solde": solde,
                "uid": id_carte
            })
            
            print("\n********Enregistrment terminé!*********")
            
        afficher_etudiant(
            {
                "prenom": prenom,
                "nom": nom,
                "solde": solde,
                "uid": id_carte
            }
        )
        time.sleep(2)
    

register_student()