import logging

from business_object.gestion_personne.utilisateur import Utilisateur
from dao.db_connection import DBConnection
from src.utils.singleton import Singleton


class UtilisateurDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Utilisateurs 
    de la base de données"""

    def creer(self, utilisateur: Utilisateur) -> bool:
        """Creation d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet_info.utilisateur(pseudo, mdp) VALUES "
                        "(%(pseudo)s, %(mdp)s)             "
                        "  RETURNING id_utilisateur;               ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise e

        created = False
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True

        return created


    def trouver_par_id(self, id_utilisateur) -> Utilisateur:
        """trouver un utilisateur grace à son id

        Parameters
        ----------
        id_utilisateur : int
            numéro id du utilisateur que l'on souhaite trouver

        Returns
        -------
        utilisateur : Utilisateur
            renvoie le utilisateur que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet_info.utilisateur                      "
                        " WHERE id_utilisateur = %(id_utilisateur)s;  ",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            print(e)
            raise e

        utilisateur = None
        if res:
            utilisateur = Utilisateur(
                pseudo=res["pseudo"],
                id_utilisateur=res["id_utilisateur"],
            )

        return utilisateur


    def lister_tous(self) -> list[Utilisateur]:
        """lister tous les utilisateurs

        Parameters
        ----------
        None

        Returns
        -------
        liste_utilisateurs : list[Utilisateur]
            renvoie la liste de tous les utilisateurs dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM projet_info.utilisateur;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            print(e)
            raise

        liste_utilisateurs = []

        if res:
            for row in res:
                utilisateur = Utilisateur(
                    id_utilisateur=row["id_utilisateur"],
                    pseudo=row["pseudo"],
                    mdp=row["mdp"]
                )

                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs


    def modifier(self, utilisateur : Utilisateur) -> bool:
        """Modification d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE utilisateur                            "
                        "   SET pseudo      = %(pseudo)s,                   "
                        "       mdp         = %(mdp)s,                      "
                        " WHERE id_utilisateur = %(id_utilisateur)s;                  ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1


    def supprimer(self, utilisateur) -> bool:
        """Suppression d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur
            utilisateur à supprimer de la base de données

        Returns
        -------
            True si le utilisateur a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un utilisateur
                    cursor.execute(
                        "DELETE FROM utilisateur                  "
                        " WHERE id_utilisateur=%(id_utilisateur)s      ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0


    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """se connecter grâce à son pseudo et son mot de passe

        Parameters
        ----------
        pseudo : str
            pseudo de l'utilisateur que l'on souhaite trouver
        mdp : str
            mot de passe de l'utilisateur

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM utilisateur                      "
                        " WHERE pseudo = %(pseudo)s         "
                        "   AND mdp = %(mdp)s;              ",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        utilisateur = None

        if res:
            utilisateur = Utilisateur(
                pseudo=res["pseudo"],
                mdp=res["mdp"],
                id_utilisateur=res["id_utilisateur"],
            )

        return utilisateur


if __name__ == "__main__": 
    Oui = Utilisateur(pseudo="Oui")
    createur = UtilisateurDao()
    print(createur.creer(Oui))


