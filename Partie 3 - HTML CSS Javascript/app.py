from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = FastAPI()

# Fonction pour initialiser la connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('../Partie 1 - Base de donnee/logement.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
CORS(app)

def get_mesures():
    # Connexion a la base de donnees SQLite
    conn = sqlite3.connect('../Partie 1 - Base de donnee/logement.db')
    conn.row_factory = sqlite3.Row  # Permet de recuperer les resultats sous forme de dictionnaires
    c = conn.cursor()

    # Execution de la requete SQL avec jointure pour extraire l unite (raccourci par le meme type et id de capteur)
    c.execute("""
        SELECT 
            Mesures.Identifiant_table_m,
            Mesures.valeur,
            Mesures.ref_id_capteur,
            Mesures.date_insertion,
            Types_Capteurs.unite_mesure
        FROM Mesures
        JOIN Types_Capteurs ON Mesures.ref_id_capteur = Types_Capteurs.Identifiant_table_t;
    """)
    rows = c.fetchall()  # Recupere toutes les lignes retournees par la requete

    mesures = []
    for row in rows:
        mesures.append({
            'Identifiant_table_m': row['Identifiant_table_m'],
            'valeur': row['valeur'],
            'ref_id_capteur': row['ref_id_capteur'],
            'date_insertion': row['date_insertion'],
            'unite_mesure': row['unite_mesure']  # Ajout de l unite de mesure
        })
    
    conn.close()  # Fermeture de la connexion a la base de donnees
    
    return mesures

# Connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('../Partie 1 - Base de donnee/logement.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route pour obtenir les factures avec cumul par type
@app.route('/factures/cumul', methods=['GET'])
def get_cumulative_factures():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = get_db_connection()
    cursor = conn.cursor()

    # Récupérer les données de facture triées par date
    query = """
        SELECT type, date, SUM(montant) AS montant
        FROM Factures
        WHERE date BETWEEN ? AND ?
        GROUP BY type, date
        ORDER BY date ASC
    """
    cursor.execute(query, (start_date, end_date))
    data = cursor.fetchall()
    conn.close()

    # Préparer les données pour un cumul par type
    cumulative_data = {}
    for row in data:
        facture_type = row["type"]
        if facture_type not in cumulative_data:
            cumulative_data[facture_type] = []

        montant_cumule = row["montant"]
        if cumulative_data[facture_type]:
            montant_cumule += cumulative_data[facture_type][-1]["montant"]

        cumulative_data[facture_type].append({
            "date": row["date"],
            "montant": montant_cumule
        })

    # Réponse JSON formatée
    return jsonify(cumulative_data)

@app.route('/mesures', methods=['GET'])
def mesures():
    return jsonify(get_mesures())  # Retourne les mesures en format JSON

if __name__ == '__main__':
    app.run(debug=True)
