-- REINITIALISATION : commandes de destruction des tables
DROP TABLE IF EXISTS Logements;
DROP TABLE IF EXISTS Factures;
DROP TABLE IF EXISTS Pieces;
DROP TABLE IF EXISTS Capteurs;
DROP TABLE IF EXISTS Mesures;
DROP TABLE IF EXISTS Types_Capteurs;

-- Tables de la Base de donnee
       -- Table des logements
CREATE TABLE Logements 
(
    Identifiant_table_l INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque logement
    adresse_physique TEXT NOT NULL, -- Adresse du logement voir a ajouter eventuellement une autre table si utilisation plus dense de la bdd
    numero_tel TEXT NOT NULL, -- Numero de telephone du responsable du logement  
    adresse_internet TEXT NOT NULL, -- Adresse Internet du logement
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date d insertion automatique au format TIMESTAMP type 2024-11-15 10:45:23
);

       -- Table des pieces
CREATE TABLE Pieces 
(
    Identifiant_table_p INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque piece
    nom TEXT NOT NULL,
    localisation_3D TEXT NOT NULL, -- Coordonnees dans une matrice 3D

    ref_id_logement INTEGER NOT NULL, -- Reference au logement auquel appartient la piece
    FOREIGN KEY (ref_id_logement) REFERENCES Logements(Identifiant_table_l)
);

       -- Table des capteurs/actionneurs
CREATE TABLE Capteurs 
(
    Identifiant_table_c INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque capteur
    reference_commerciale TEXT NOT NULL, -- Reference commerciale du capteur
    port_COM TEXT NOT NULL, -- Port de communication avec le serveur
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date d insertion automatique

    ref_id_type_capteur INTEGER NOT NULL, -- Reference aux specificites du type de releve (temperature, electricite, etc.)
    ref_id_piece INTEGER NOT NULL, -- Reference à la pièce où est installé le capteur
    FOREIGN KEY (ref_id_type_capteur) REFERENCES Types_Capteurs (Identifiant_table_t)
    FOREIGN KEY (ref_id_piece) REFERENCES Pieces(Identifiant_table_p)
);

       -- Table des types de capteurs/actionneurs
CREATE TABLE Types_Capteurs 
(
    Identifiant_table_t INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque type
    unite_mesure TEXT NOT NULL, -- Unite de mesure (°C, kWh, etc.)
    plage_precision TEXT, -- Plage de precision (par exemple : 0.5°C)
    grandeur_mesure TEXT NOT NULL -- Grandeur ou unite de la mesure
);

       -- Table des mesures
CREATE TABLE Mesures 
(
    Identifiant_table_m INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque mesure
    valeur NUMERIC NOT NULL, -- Valeur de la mesure
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date d insertion automatique

    ref_id_capteur INTEGER NOT NULL, -- Reference au capteur ayant effectue la mesure
    FOREIGN KEY (ref_id_capteur) REFERENCES Capteurs(Identifiant_table_c)
);

       -- Table des factures
CREATE TABLE Factures 
(
    Identifiant_table_f INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque facture
    type_facture TEXT NOT NULL, -- Type de facture (eau, electricite, dechets, etc.)
    montant NUMERIC NOT NULL, -- Montant de la facture
    consommation NUMERIC, -- Valeur consommee associee a la facture, peut etre null en cas de consomation au forfait
    ref_id_logement INTEGER NOT NULL, -- Reference au logement associe

    date_emission TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date d emission de la facture
    FOREIGN KEY (ref_id_logement) REFERENCES Logements(Identifiant_table_l)
);

-- Insertion donnees

-- Insertion donnees Logements
INSERT INTO Logements (adresse_physique, numero_tel, adresse_internet) VALUES
       ('4 rue du Moulin, 12002 FRANCE', '0605040302', '145.97.00.155');

-- Insertion donnees Pieces
INSERT INTO Pieces (nom, localisation_3D, ref_id_logement) VALUES
       ('Salon', '1,5,1', 1),
       ('Cuisine', '1,7,3', 1),
       ('Chambre_1', '4,1,1', 1),
       ('Entre', '0,0,1', 1);

-- Insertion donnees Types_Capteurs
INSERT INTO Types_Capteurs (unite_mesure, plage_precision, grandeur_mesure) VALUES
       ('°C', '0.5', 'Temperature'),
       ('%', '5', 'Humidite'),
       ('V', '1', 'Tension_Voltage'),
       ('Lux', '10', 'Luminosite');

-- Insertion Capteur
INSERT INTO Capteurs (reference_commerciale, port_COM, ref_id_type_capteur, ref_id_piece) VALUES
       ('ThermoSense-100', 'COM1', 1, 1),        -- Capteur de temperature dans Salon
       ('HygroCheck-50', 'COM2', 2, 1),          -- Capteur d humidite dans Salon
       ('VoltMonitor-200', 'COM3', 3, 2),        -- Capteur de tension dans Cuisine
       ('LightPro-300', 'COM4', 4, 3);           -- Capteur de luminosite dans Chambre_1

-- Insertion donnees de Mesures
INSERT INTO Mesures (valeur, ref_id_capteur) VALUES
       (22.3, 1), -- Mesure n°1 de la temperature par le capteur 1 (ThermoSense-100)
       (23.0, 1), -- Mesure n°1 de la temperature par le capteur 2 (ThermoSense-100)
       (22.8, 1), -- Mesure n°1 de la temperature par le capteur 3 (ThermoSense-100)
       (22.5, 1), -- Mesure n°1 de la temperature par le capteur 4 (ThermoSense-100)

       (45.5, 2), -- Mesure n°1 de l humidite par le capteur 2 (HygroCheck-50)
       (47.0, 2), -- Mesure n°2 de l humidite par le capteur 2 (HygroCheck-50)
       (93.5, 2), -- Mesure n°1 de l humidite par le capteur 2 (HygroCheck-50)
       (92.1, 2), -- Mesure n°2 de l humidite par le capteur 2 (HygroCheck-50)
       (89.2, 2), -- Mesure n°1 de l humidite par le capteur 2 (HygroCheck-50)

       (230.0, 3), -- Mesure de tension par le capteur 3 (VoltMonitor-200)
       (228.5, 3), -- Deuxieme mesure de tension

       (700.0, 4), -- Mesure de luminosite par le capteur 4 (LightPro-300)
       (750.0, 4); -- Deuxieme mesure de luminosité

-- Insertion donnees de Factures
INSERT INTO Factures (type_facture, montant, consommation, ref_id_logement) VALUES
       ('Electricite', 76.8, 290, 1),  -- Facture de electricite pour le logement 1
       ('Eau', 40.50, 120, 1), -- Facture d eau pour le logement 1
       ('Gaz', 65.80, 180, 1), -- Facture de gaz pour le logement 1
       ('Déchets', 25.00, NULL, 1); -- Facture de gestion des dechets, montant en mode forfait (pas de consommation associee, non relevable)

-- Co redigee avec ChatGPT apres avoir compris le principe et essaye les concepts avec plusieurs exemples