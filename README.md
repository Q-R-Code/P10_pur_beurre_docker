[![Build Status](https://travis-ci.com/Q-R-Code/P10_pur_beurre_docker.svg?branch=main)](https://travis-ci.com/Q-R-Code/P10_pur_beurre_docker)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
<img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>

# Pur Beurre dénicheur

Ce site permettra à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras, trop sucré, trop
salé".

--------------------------------------------

## Installation & lancement ##

Télécharger et décompresser le repository puis créer un VENV. Installer ensuite le requirements.

    pip install -r requirements.txt

Pour paramétrer la base de données il faut modifier les réglages dans Pur_beurre_project_app settings.py > DATABASE.

Pour peupler la base de données "Product" :

    python manage.py fill_db

La BDD sera peuplée de 200 produits grace à un appel API OpenFoodFacts. Vous pouvez modifier ça dans catalogue >
management > commands > fill_db.py

Pour démarrer l'application :

    python manage.py runserver 

--------------------------------------------

## Applications  ##

### Account : ###

Gère la partie : inscription, connexion et déconnexion du site grace au système d'authentification de Django.
(django.contrib.auth).

### Catalogue : ###

Cette application s'occupe de toutes les autres fonctionnalités du site. La génération des différentes vues ( index,
mentions légales, mes produits, mon compte ...)

Et des actions comme :

- La recherche de produits dans la BDD.
- La recherche de substituts.
- La sauvegarde d'un substitut.
- La suppression d'un substitut sauvegardé par un utilisateur.

--------------------------------------------

## Tests ##

Coverage report 2021-04-13 15:35 -- 93%
Coverage created at 2021-05-20 11:30 -- 94%

### Account > tests.py ###

Des tests unitaires pour les vues : register et login.

Un test fonctionnel pour le parcours d'un utilisateur de la création de compte à la connexion.

### Catalogue ###

Des tests unitaires pour les vues : index, mentions légales, search.

Trois tests d'integrations : La recherche d'un produit en particulier, la sauvegarde d'un substitut et la suppression d'
un substitut sauvegardé par un utilisateur.

Un test fonctionnel pour :

Utilisateur connecté grace à force_login.

- Lancement d'une recherche
- Recherche de substitut sur ce produit
- Sauvegarde d'un substitut
- Affichage de la page "mes produits".

--------------------------------------------

## Version : ##

- 1.0 : Premiere version stable de l'application. En ligne sur : https://purbeurre-denicheur.herokuapp.com/
- 1.5 : Ajout d'une nouvelle fonctionnalité : Historique des 10 dernières recherches.