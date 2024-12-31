-- sqlite3 bibli.db
--.read bibli.sql

-- REINITIALISATION : commandes de destruction des tables
DROP TABLE IF EXISTS Logements;
DROP TABLE IF EXISTS Factures;
DROP TABLE IF EXISTS Pieces;
DROP TABLE IF EXISTS Capteurs;
DROP TABLE IF EXISTS Mesures;
DROP TABLE IF EXISTS Types_Capteurs;

-- commandes de creation des tables

CREATE TABLE Document (id INTEGER PRIMARY KEY AUTOINCREMENT, Titre TEXT NOT NULL);
CREATE TABLE Auteur (id  INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, Prenom TEXT NOT NULL);
CREATE TABLE Bibliotheque (id  INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, Localisation TEXT NOT NULL);
CREATE TABLE Etudiant (id  INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, Prenom TEXT NOT NULL, idAd INTEGER NOT NULL, FOREIGN KEY (idAd) REFERENCES Adresse(id));
CREATE TABLE Adresse (id  INTEGER PRIMARY KEY AUTOINCREMENT, Numero INTEGER NOT NULL, Voie TEXT NOT NULL, Nom_voie TEXT NOT NULL, Code INTEGER NOT NULL, FOREIGN KEY (Code) REFERENCES Ville(Code));
CREATE TABLE Ville (Code INTEGER PRIMARY KEY, Nom TEXT NOT NULL);

-- insertion de données
INSERT INTO Document (Titre) VALUES ("Bases de données concepts, utilisation et développement");
INSERT INTO Document (Titre) VALUES ("Python les fondamentaux du langage, la programmation pour les scientifiques");
INSERT INTO Document (Titre) VALUES ("Programmer en Java");

INSERT INTO Auteur (Nom, Prenom) VALUES
       ("Brucher", "Matthieu"),
       ("Hainaut", "Jean-Luc"),
       ("Delannoy", "Claude");

INSERT INTO Bibliotheque (Nom, Localisation) VALUES
       ("Bibliothèque des Licences", "Tour 43 RDC"),
       ("L1 - L2 scientifique", "Patio 45-46");

INSERT INTO Etudiant (Nom, Prenom, idAd) VALUES
       ("Cover", "Harry", 1),
       ("Deuf", "John", 2),
       ("Onette", "Marie", 3),
       ("Onette", "Camille", 3),
       ("Theblues", "Agathe", 4);

INSERT INTO Adresse (Numero, Voie, Nom_voie, Code) VALUES
       (4, "allée", "des groseilliers", 92140),
       (14, "rue", "Berthelot", 94200),
       (18, "rue", "d Estrée", 75007),
       (56, "rue", "Arthur Rimbaud", 93300);

INSERT INTO Ville VALUES (92140, "Clamart"),
       (94200, "Ivry sur Seine"),
       (75007, "Paris"),
       (93300, "Aubervilliers");

-- Associations
CREATE TABLE Emprunte (idEtu INTEGER NOT NULL, idDoc INTEGER NOT NULL, Date TEXT NOT NULL, FOREIGN KEY (idEtu) REFERENCES Etudiant(id), FOREIGN KEY (idDoc) REFERENCES Document(id), PRIMARY KEY (idEtu,idDoc));
CREATE TABLE Possede (idBibli INTEGER NOT NULL, idDoc INTEGER NOT NULL, Ref TEXT NOT NULL, FOREIGN KEY (idBibli) REFERENCES Bibliotheque(id), FOREIGN KEY (idDoc) REFERENCES Document(id), PRIMARY KEY (idBibli,idDoc));
CREATE TABLE Redige (idAut INTEGER NOT NULL, idDoc INTEGER NOT NULL, Date TEXT NOT NULL, FOREIGN KEY (idAut) REFERENCES Auteur(id), FOREIGN KEY (idDoc) REFERENCES Document(id), PRIMARY KEY (idAut,idDoc));

INSERT INTO Emprunte VALUES (2, 3, "23/10/2020");
INSERT INTO Emprunte (idEtu, idDoc, Date)
   SELECT
      (SELECT id FROM Etudiant WHERE Nom = "Onette" AND Prenom = "Marie") as idEtu,
      (SELECT id FROM Document WHERE Titre = "Bases de données concepts, utilisation et développement") as idDoc,
      "14/10/2020" as Date;

INSERT INTO Possede VALUES (1, 1, "BRU 5.2");
INSERT INTO Possede VALUES (1, 2, "HAI 7.4");
INSERT INTO Possede VALUES (2, 3, "DEL 2.3");

INSERT INTO Redige VALUES (1, 1, "2008");
INSERT INTO Redige VALUES (2, 3, "2010");
INSERT INTO Redige VALUES (3, 3, "2013");

-- les étudiants qui ont emprunté un document
SELECT Nom, Prenom FROM Etudiant  INNER JOIN Emprunte ON Etudiant.id = Emprunte.idEtu;
