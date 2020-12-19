from pymongo import MongoClient


class Carte:
    """
    Modèle Carte. Pour effectuer les différentes transactions avec la base de données.
    """
    client = MongoClient("mongodb+srv://ali:ali221@cluster0.xie2q.mongodb.net/restaudb?retryWrites=true&w=majority")
    db = client.restaudb
    collection = db.carte

    def __init__(self, prenom, nom, solde, uid):
        self.prenom = prenom
        self.nom = nom
        self.solde = solde
        self.uid = uid

    def toJSON(self):
        return {
            "prenom": self.prenom,
            "nom": self.nom,
            "solde": self.solde,
            "uid": self.uid
        }

    @classmethod
    def get_student_by_uid(cls, uid):
        return cls.collection.find_one({
            "uid": uid
        })

    @classmethod
    def update_solde(cls, uid, solde):
        return cls.collection.find_one_and_update(
            {'uid': uid},
            {'$set': {"solde": solde}},
        )
    
    @classmethod
    def update_etudiant(cls, uid, prenom, nom, solde):
        return cls.collection.find_one_and_update(
            {'uid': uid},
            {'$set': {"solde": solde, "prenom": prenom, "nom": nom}},
        )
    
    @classmethod
    def register_student_to_bd(cls, student):
        return cls.collection.insert_one(student)
    
    
    @classmethod
    def liste_etudiant(cls):
        return cls.collection.find({})
    