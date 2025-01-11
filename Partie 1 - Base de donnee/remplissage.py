import sqlite3, random
random.seed()

# ouverture/initialisation de la base de donnee 
conn = sqlite3.connect('logement.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# affichage d une table
# lecture dans la base avec un select
c.execute("SELECT * FROM Factures")

# parcourt initial ligne a ligne des Factures
for raw in c.execute('SELECT * FROM Factures'):
	print (raw.keys())
	print (raw["type_facture"])
	print (raw["montant"])

# insertion de plusieurs donnees 
# Rappel pour une valeur insertion c.execute("INSERT INTO Emprunte VALUES (4,1,'23/10/2020')")

values = []

for i in range(4):
    type_facture = random.choice(['Electricité', 'Eau', 'Gaz', 'Déchets', 'Téléphone', 'Internet'])
    
    if type_facture == 'Déchets':
        montant = 25.00  # Montant fixe de charge forfaitaire pour les dechets
        consommation = None  # Pas de consommation pour les dechets
    elif type_facture in ['Electricité', 'Eau']:
        montant = round(random.uniform(45.0, 60.0), 2)      # Montant dans une plage plus elevee
        consommation = round(random.uniform(120, 300), 2)   # Consommation moyenne - haute
    elif type_facture in ['Gaz', 'Téléphone', 'Internet']:
        montant = round(random.uniform(10.0, 30.0), 2)      # Montant dans une plage plus basse
        consommation = round(random.uniform(50, 170), 2)    # Consommation basse - moyenne
    else:
        montant = round(random.uniform(30.0, 150.0), 2)     # Par defaut, montant general
        consommation = round(random.uniform(100, 500), 2)   # Consommation par defaut

    ref_id_logement = 1  # Reference au 1er logement ( logement 1 )
    date_emission = f"2025-0{random.randint(1, 1)}-{random.randint(13, 13):02} {random.randint(7, 24):02}:{random.randint(0, 60):02}:{random.randint(2, 49):02}"
    values.append((type_facture, montant, consommation, ref_id_logement, date_emission))
c.executemany('INSERT INTO Factures (type_facture, montant, consommation, ref_id_logement, date_emission) VALUES (?, ?, ?, ?, ?)', values)

valeur = []
for _ in range(3):  # Generer 20 mesures
    ref_id_capteur = random.choice([1, 2, 3, 4])

    if   ref_id_capteur == 1:  # Capteur de temperature
        valeur_mesure = round(random.uniform(5.0, 34.0), 1)        # Plage realiste pour °C
    elif ref_id_capteur == 2:  # Capteur d humidite
        valeur_mesure = round(random.uniform(20.0, 100.0), 1)      # Plage realiste pour %
    elif ref_id_capteur == 3:  # Capteur de tension
        valeur_mesure = round(random.uniform(200.0, 240.0), 1)     # Plage realiste pour tension en V
    elif ref_id_capteur == 4:  # Capteur de luminosite
        valeur_mesure = round(random.uniform(500.0, 1000.0), 1)    # Plage realiste pour Lux
    
    # Ajouter la mesure avec le ref_id_capteur correspondant
    valeur.append((valeur_mesure, ref_id_capteur))
c.executemany('INSERT INTO Mesures (valeur, ref_id_capteur) VALUES (?, ?)', valeur)

#for raw in c.execute('SELECT * FROM Mesures'):
#    print(raw.keys())
#    print(raw["valeur"])
#    print(raw["ref_id_capteur"])
#    print(raw["date_insertion"])

# Affiche les colonnes une seule fois
for raw in c.execute('SELECT * FROM Mesures'):
    print(raw.keys())  # Affiche les colonnes une seule fois
    break  # S'arrête après la première ligne

# Affiche les données sous la forme souhaitée
for raw in c.execute('SELECT * FROM Mesures'):
    print(f"{raw['Identifiant_table_m']}\t    {raw['valeur']}  \t {raw['date_insertion']}\t {raw['ref_id_capteur']}") #GPT ed 


# fermeture
conn.commit()
conn.close()
