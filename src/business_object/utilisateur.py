class Utilisateur:
    """
    Classe représentant un utilisateur

    Attributs
    ----------
    id_utilisateur : int
        identifiant
    pseudo : str
        pseudo de l'utilisateur
    mdp : str
        le mot de passe de l'utilisateur
    liste_eclaireurs : 
        la liste des eclaireurs qu'il suit
    liste_films_favoris : 
        la liste de ses films favoris
    """

    def __init__(self, pseudo, mdp=None, liste_eclaireurs=[], liste_films_favoris=[], id_utilisateur=None):
        """Constructeur"""
        self.id_utilisateur = id_utilisateur
        self.pseudo = pseudo
        self.mdp = mdp
        self.liste_eclaireurs = liste_eclaireurs
        self.liste_films_favoris = liste_films_favoris

    def __str__(self):
        """Permet d'afficher les informations du joueur"""
        return f"Utilisateur({self.pseudo})"

    def as_list(self) -> list[str]:
        """Retourne les attributs du joueur dans une liste"""
        return [self.id_utilisateur, self.pseudo, self.mdp, self.liste_eclaireurs, self.liste_films_favoris]