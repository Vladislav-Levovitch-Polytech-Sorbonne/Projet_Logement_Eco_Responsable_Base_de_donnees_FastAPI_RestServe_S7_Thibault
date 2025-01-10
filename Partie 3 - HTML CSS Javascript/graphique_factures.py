import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from datetime import datetime

# Connexion à la base de données SQLite
conn = sqlite3.connect('logement.db')  # Assure-toi que 'logement.db' est dans ton répertoire
conn.row_factory = sqlite3.Row
c = conn.cursor()

# Récupérer les données des factures
c.execute('SELECT type_facture, montant, date_emission FROM Factures')
factures = c.fetchall()

# Structure de données pour stocker les factures par jour et par type de facture
factures_par_jour = defaultdict(lambda: defaultdict(float))  # {jour: {type_facture: montant_cumulé}}

# Parcourir toutes les factures pour les regrouper par jour et type
for facture in factures:
    # Récupérer les informations de chaque facture
    type_facture = facture['type_facture']
    montant = facture['montant']
    date_emission = facture['date_emission']
    
    # Extraire la date sous forme de jour
    date_obj = datetime.strptime(date_emission, '%Y-%m-%d %H:%M:%S')
    jour = date_obj.date()
    
    # Accumuler les montants par jour et par type de facture
    factures_par_jour[jour][type_facture] += montant

# Préparer les données pour le graphique
jours = sorted(factures_par_jour.keys())
types_factures = set(type_facture for facture in factures for type_facture in facture['type_facture'])
data = {type_facture: [] for type_facture in types_factures}

# Pour chaque jour, ajouter les montants cumulés pour chaque type de facture
for jour in jours:
    for type_facture in types_factures:
        data[type_facture].append(factures_par_jour[jour].get(type_facture, 0))

# Créer le graphique
plt.figure(figsize=(10, 6))
for type_facture, montants in data.items():
    plt.plot(jours, np.cumsum(montants), label=type_facture, marker='o')

# Personnaliser le graphique
plt.title('Montant cumulé des factures par type')
plt.xlabel('Jour')
plt.ylabel('Montant cumulé (€)')
plt.xticks(rotation=45)
plt.legend(title="Types de factures")
plt.grid(True)

# Afficher le graphique
plt.tight_layout()
plt.show()

# Fermeture de la connexion à la base de données
conn.close()
