from src.dao.db_connection import DBConnection
from src.dao.utilisateur_dao import UtilisateurDao


def verifier_utilisateur_existe():
    """Vérifie s'il y a au moins un utilisateur dans la base de données"""
    try:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM projet_info.utilisateur"
                )
                res = cursor.fetchone()

        validite = False
        if res:
            validite = True

        return validite

    except Exception as e:
        print(f"Erreur lors de la vérification de l'utilisateur : {e}")
        return False


# Exemple d'appel de la fonction
if __name__ == "__main__":
    existe = verifier_utilisateur_existe()
    if existe:
        print("Un utilisateur existe dans la base de données.")
    else:
        print("Aucun utilisateur trouvé.")
    utilisateurdao = UtilisateurDao()
    utilisateurtest = utilisateurdao.trouver_par_id(1)
    utilisateur_list_test = utilisateurdao.lister_tous()
    print(utilisateur_list_test)
    print(utilisateurtest.pseudo)
