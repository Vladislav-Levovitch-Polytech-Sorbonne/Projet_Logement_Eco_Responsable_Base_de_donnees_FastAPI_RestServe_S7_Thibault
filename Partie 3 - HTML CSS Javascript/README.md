# IoT - Logement Éco-Responsable

## 📽️​ Vidéo Démonstration
Une vidéo est disponible pour expliquer comment exécuter le serveur, interagir avec l’API et visualiser les données via le site web : [`Video Demonstration Utilisation/Demonstration_Tuto_Partie_3_Web.mp4`](https://github.com/Vladislav-Levovitch-Polytech-Sorbonne/Projet_Logement_Eco_Responsable_Base_de_donnees_FastAPI_RestServe_S7_Thibault/blob/main/Ressources_utiles_utilisees/Modele_Relationnel.png)

![Illustration Partie 3 - Graphique sur site web](../Ressources_utiles_utilisees/Images_ReadME/Read_ME_3.png)

Pour voir la démonstration, **il vous suffit d'ouvrir le fichier `index.html`** dans un navigateur depuis le dossier de la Partie 3 avec l'ensemble des fichiers du projet.

## 🗃️ Partie 3 : Partie 3 : Frontend - Site Web
Utilisation de GPT pour le débogage, le codage et la recherche d'informations. Les liens vus en CM ont été utilisés en majeure partie, cités ci-dessous. D'autres ressources comme les codes de divers site internet ont été repris et l'apprentissage à été réalisé par mini module sur la plateforme d'openclassrooms.

### Dépendances à installer

1. Assurez-vous que Flask et FastAPI sont installés. Si ce n'est pas le cas, installez-le avec la commande suivante, si besion flaskcors et enfin lancez python app.py et Graph_generation.py :
   ```bash
   python -m venv env
   .\env\Scripts\Activate.ps1
   pip install "fastapi[standard]"
   pip install flask
   pip install flask-cors
   pip install matplotlib numpy
   python '.\Partie 3 - HTML CSS Javascript\app.py'    
   fastapi dev '.\Partie 3 - HTML CSS Javascript\Graph_generation.py'

Enfin ouvrir dans un navigateur le fichier **index.html**
http://127.0.0.1:5000/mesures pour voir les donnees du site (ou encore http://127.0.0.1:8000/factures pour les factures en adaptant au port utilisé )

**📁 app.py ( Serveur Flask )**
Le fichier app.py contient la logique du serveur qui sert les données à la page web.

**📁 index.html ( Frontend )**
Le fichier index.html présente l'interface web où les données des mesures sont affichées dans une table HTML.


Ressources internet utilisées :
**https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3**
**https://openclassrooms.com/fr/courses/6691451-codez-un-site-web-accessible-avec-html-css**
**https://openclassrooms.com/fr/paths/942-bootcamp-introduction-html-css-et-javascript**
https://chatgpt.com/
https://openclassrooms.com/fr/
https://developers.google.com/chart/interactive/docs/gallery?hl=fr
https://www.w3schools.com/bootstrap/default.asp

Remerciement pour le ReadMe source reutilisé : Ayoub LADJiCi et des fichiers de Daniel FERREIRA LARA 
Readapted with gpt

Aide rédactionnelle, au débogage, au code, soutien et remerciement : Daniel, Yulin, Maxime, Ayman, Victor, Quentin, Ayoub, Keryann, Nicolas, ChatGPT, HARIAN Elyoth, Benjamin et Thibault HILAIRE