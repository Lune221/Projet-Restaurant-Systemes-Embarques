from get_uid import get_uid
from leds_management import *
from models import Carte
from afficher_etudiant import afficher_etudiant

SOLDE_PETIT_DEJ = 50
SOLDE_REPAS = 100


def get_student_by_uid(uid):
    """
    C'est une fonction pour avoir l'étudiant correspondant à l'uid de la carte
    """
    for student in TEST_STUDENTS:
        if student["id_carte"] == uid:
            return student
    return None
    
def charger_carte():
    """
    C'est une fonction qui nous permet de recharger la carte de létudiant
    """
    while True:
        print("\n********* RECHARGEMENT DE CARTE **********\n")
        uid = get_uid()
        etudiant = Carte.get_student_by_uid(uid)
        afficher_etudiant(etudiant)
        if etudiant != None: 
            montant = int(input("Entrer le solde à ajouter: "))
            etudiant['solde'] += montant
            Carte.update_solde(uid, etudiant['solde'])
            turn_green_on()
            afficher_etudiant(etudiant)
            
            continue
        
        turn_red_on()
        print("uid inexistant!")


def debiter_carte():
    """
    C'est une fonction qui nous permet de débiter la carte de létudiant
    """
    while True:
        print("\n********* DEBITEMENT DE CARTE **********\n")
        uid = get_uid()
        etudiant = Carte.get_student_by_uid(uid)
        if etudiant != None:
            print("Etudiant Identifié!")
            afficher_etudiant(etudiant)
            print("Entrer le type de repas !")
            print("1. Petit-déjeuner")
            print("2. Repas")
            type_repas = int(input("Entrer 1 ou 2 : "))
            
            if type_repas !=1 and type_repas!=2:
                turn_red_on()
                print("Choix non pris en charge!")
                continue
            elif type_repas == 1 and etudiant["solde"] >=SOLDE_PETIT_DEJ :
                etudiant['solde'] -= SOLDE_PETIT_DEJ
                Carte.update_solde(uid, etudiant['solde'])
                
            elif type_repas == 2 and etudiant["solde"] >=SOLDE_REPAS:
                etudiant['solde'] -= SOLDE_REPAS
                Carte.update_solde(uid, etudiant['solde'])
            else:
                turn_red_on()
                print("*****Solde insuffisant!*****")
            
            turn_green_on()
            afficher_etudiant(etudiant)
            
            continue
        turn_red_on()
        print("****Etudiant inexistant!*****")