DROP SCHEMA IF EXISTS projet_info CASCADE;
CREATE SCHEMA projet_info;

--------------------------------------------------------------
-- Utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS projet_info.utilisateur CASCADE ;
CREATE TABLE projet_info.utilisateur (
    id_utilisateur serial PRIMARY KEY,
    pseudo VARCHAR(30) UNIQUE,
    mdp VARCHAR(250)
);