# TP IoT - Logement Éco-Responsable
//ReadMe reutilise de Ayoub LADJICI

## 🗃️ Partie 1 : Modèle Relationnel de la Base de Données
Utilisation de GPT pour le débogage, essentiellement et surtout du code fourni dans le cours et disponible dans le répertoire "Ressources_utiles_utilisées"
### 1.1 Spécifications de la base de données
**Question 1 :** Le modèle relationnel de la base de données se trouve dans le fichier :  
**📁 [`Ressources_utiles_utilisees/Modele_Relationnel.png.png`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Ressources_utiles_utilisees/Modele_Relationnel.png)**
- Il a été construit en respectant les **spécifications données dans le sujet**.
- Les **rectangles bleus** contiennent les **entités** ( les tables ) et leurs **attributs associés**.

**Question 2 :** Les ordres SQL permettant de détruire toutes les tables existantes dans notre base se trouve dans le fichier :
**📁 [`logement.sql`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/logement.sql)** ```lignes 2 à 7```
- Cela est possible grâce à la commande ```DROP TABLE IF EXISTS nom_table;```

**Question 3 :** Les ordres SQL permettant de créer toutes les tables de notre base se trouve dans le fichier :
**📁 [`logement.sql`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/logement.sql)** ```lignes 11 à 76```
- Cela est possible grâce à la commande ```CREATE TABLE nom_table(id_nom_table INTEGER PRIMARY KEY AUTOINCREMENT, nom_champ type_champ,..., FOREIGN KEY (id_Ad) REFERENCES Adresse(id_autre_table)); ```

**Question 4 :** Les ordres SQL permettant de créer un logement avec 4 pièces :
**📁 [`logement.sql`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/logement.sql)** ```lignes 81 à 89```
- Cela est possible grâce à la commande ```INSERT INTO Pieces(nom, localisation_3D, ref_id_logement) VALUES ```

- J'ai crée un logement avec 4 pièces distinces : Chambre_1, Salon, Cuisine, Entree

**Question 5 :** Les ordres SQL permettant de créer au moins 4 types de capteurs/actionneurs :
**📁 [`logement.sql`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/logement.sql)** ```lignes 92 à 96```
- Cela est possible grâce à la commande ```INSERT INTO Types_Capteurs (unite_mesure, plage_precision, grandeur_mesure) VALUES ```
- J'ai crée 4 types de capteurs (Temperature, Humidite, Tension_Voltage, Luminosite )

**Question 6 :** Les ordres SQL permettant de créer au moins 2 capteurs/actionneurs :
**📁 [`logement.sql`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/logement.sql)** ```lignes 99 à 103```
- Cela est possible grâce à la commande ```INSERT INTO Capteurs (reference_commerciale, port_COM, ref_id_type_capteur, ref_id_piece) VALUES```
- J'ai crée un capteur/actionneur pour chaque type de capteur/actionneur.

**Question 7 :** Les ordres SQL permettant de créer au moins 2 mesures par capteur/actionneur :
**📁 [`logement.sql`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/logement.sql)** ```lignes 106 à 122```
- Cela est possible grâce à la commande ```INSERT INTO Mesures (valeur, ref_id_capteur) VALUES```
- J'ai ajouté 2 à 5 mesures par capteur/actionneur dans notre base de donnee

**Question 8 :** Les ordres SQL permettant de créer au moins 4 factures :
**📁 [`logement.sql`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/logement.sql)** ```lignes 105 à 129```
- Cela est possible grâce à la commande ```INSERT INTO Factures (type_facture, montant, consommation, ref_id_logement) VALUES```
- J'ai crée 4 factures de types différents (Electricite, Eau, Gaz, Déchets)

### 🐍 1.2 Remplissage de la base de données
Utilisation de GPT pour le débogage et beaucoup pour le commentaire, essentiellement et surtout du code fourni dans le cours et disponible dans le répertoire "Ressources_utiles_utilisées"
La fonction de remplissage se trouve dans le fichier : **📁 [`remplissage.py`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Partie%201%20-%20Base%20de%20donnee/remplissage.py)**

J ai utilise cette commande pour l insertion de nouvelle donnee de maniere plus automatisable qu avec le code en sqlite3 : ``` c.executemany('INSERT INTO Factures (type_facture, montant, consommation, ref_id_logement, date_emission) VALUES (?, ?, ?, ?, ?)', values)```

Les generations de donnees ont ete en partie tiree au sort dans une plage de coherence bornee pour chaque donnees voir fixees pour les consommations au forfait par exemple avec les commandes : ```elif type_facture in ['Electricité', 'Eau']:```
      ```montant = round(random.uniform(45.0, 60.0), 2)      # Montant dans une plage plus elevee ```
      ```consommation = round(random.uniform(120, 300), 2)   # Consommation moyenne - haute```


Ressources internet utilisées :
https://fastapi.tiangolo.com/fr/tutorial/first-steps/
https://fastapi.tiangolo.com/fr/tutorial/query-params/#parametres-optionnels
https://www.w3schools.com/python/default.asp#gsc.tab=0&gsc.q=fastapi
https://www.w3schools.com/python/default.asp#gsc.tab=0&gsc.q=fastapi
https://chatgpt.com/

Remerciement pour le ReadMe source reutilisé : Ayoub LADJiCi et des fichiers de Daniel FERREIRA LARA 
Readapted with gpt

Aide rédactionnelle, au débogage, au code, soutien et remerciement : Daniel, Yulin, Maxime, Ayman, Victor, Quentin, Ayoub, Keryann, Nicolas, ChatGPT, HARIAN Elyoth, Benjamin et Thibault HILAIRE