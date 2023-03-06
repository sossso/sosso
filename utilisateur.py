import utilisateur as user
def creer_user( ):

    nom = input("entrez votre nom")
    prenom = input("entrez votre prenom")
    age = input("entrez votre age")
    adresse = input("donner votre adresse")
    telephone = input("entrez votre numero de telephone")
    user1 = user.Utilisateurs(nom,prenom,age,adresse,telephone)

def creer(self)