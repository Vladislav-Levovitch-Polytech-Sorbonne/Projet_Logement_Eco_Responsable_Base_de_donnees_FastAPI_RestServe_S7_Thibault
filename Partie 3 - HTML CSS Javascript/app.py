from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_mesures():
    # Connexion à la base de donnees SQLite
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

@app.route('/mesures', methods=['GET'])
def mesures():
    return jsonify(get_mesures())  # Retourne les mesures en format JSON

if __name__ == '__main__':
    app.run(debug=True)
