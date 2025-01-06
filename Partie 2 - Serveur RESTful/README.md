# IoT - Logement Éco-Responsable

## 📽️​ Vidéo Démonstration
Une vidéo est disponible pour expliquer comment exécuter le serveur REST, interagir avec l’API pour remplir ou consulter la base de données, et visualiser les données sous forme de graphique : [`Video Demonstration Utilisation/Demonstration_Tuto_Partie_2_Serveur_REST.mp4`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Ressources_utiles_utilisees/Modele_Relationnel.png)

## 🗃️ Partie 2 : Serveur RESTful
Utilisation de GPT pour le débogage, le codage et la recherche d'informations. Les liens vus en CM ont été utilisés en majeure partie, cités ci-dessous.

### Exercice 2.1 remplissage de la base de données
L'implémentation du serveur REST avec des routes **GET et POST** pour interagir avec la base de données logement.db se trouve dans le fichier :
**📁 [`1_Serv_Fast_APi_GET_POST.py`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%202%20-%20Serveur%20RESTful/1_Serv_Fast_APi_GET_POST.py)**
- GET : Récupère les factures et les mesures enregistrées dans la base de données.
- POST : Permet d’ajouter de nouvelles factures et mesures en spécifiant les informations nécessaires (type, montant, consommation, etc.).

### Exercice 2.2 Génération de graphique en camembert
L'implémentation d'une fonctionnalité pour générer une page HTML contenant un graphique en camembert basé sur les factures enregistrées au chemin http://127.0.0.1:8000 **/factures/pie_chart/** se trouve dans le fichier :
**📁 [`2_Serv_PieChart_Factures.py`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%202%20-%20Serveur%20RESTful/2_Serv_PieChart_Factures.py)**
- Création dynamique d'une page HTML qui affiche la répartition des coûts par type de facture grâce à Google Charts.



Ressources internet utilisées :
https://fastapi.tiangolo.com/fr/tutorial/first-steps/
https://fastapi.tiangolo.com/fr/tutorial/query-params/#parametres-optionnels
https://www.w3schools.com/python/default.asp#gsc.tab=0&gsc.q=fastapi
https://www.w3schools.com/python/default.asp#gsc.tab=0&gsc.q=fastapi
https://chatgpt.com/

Remerciement pour le ReadMe source reutilisé : Ayoub LADJiCi et des fichiers de Daniel FERREIRA LARA 
Readapted with gpt

Aide rédactionnelle, au débogage, au code, soutien et remerciement : Daniel, Yulin, Maxime, Ayman, Victor, Quentin, Ayoub, Keryann, Nicolas, ChatGPT, HARIAN Elyoth, Benjamin et Thibault HILAIRE