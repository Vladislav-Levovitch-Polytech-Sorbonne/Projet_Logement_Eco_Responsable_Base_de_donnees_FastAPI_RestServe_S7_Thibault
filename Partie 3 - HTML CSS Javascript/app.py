from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_mesures():
    conn = sqlite3.connect('../Partie 1 - Base de donnee/logement.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM Mesures")
    rows = c.fetchall()

    mesures = []
    for row in rows:
        mesures.append(
        {
            'Identifiant_table_m': row['Identifiant_table_m'],
            'valeur': row['valeur'],
            'ref_id_capteur': row['ref_id_capteur'],
            'date_insertion': row['date_insertion']
        })
    
    conn.close()
    
    return mesures

@app.route('/mesures', methods=['GET'])
def mesures():
    return jsonify(get_mesures())

if __name__ == '__main__':
    app.run(debug=True)