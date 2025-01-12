from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

# Initialisation de Flask
app = Flask(__name__)
CORS(app)

# Fonction pour initialiser la connexion à la base de données SQLite
def get_db_connection():
    conn = sqlite3.connect('../Partie 1 - Base de donnee/logement.db')
    conn.row_factory = sqlite3.Row
    return conn

# Récupération des mesures avec les types de capteurs et leur unité
def get_mesures():
    conn = get_db_connection()
    c = conn.cursor()

    # Requête SQL pour récupérer les mesures avec l'unité de mesure des capteurs
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
    rows = c.fetchall()

    mesures = []
    for row in rows:
        mesures.append({
            'Identifiant_table_m': row['Identifiant_table_m'],
            'valeur': row['valeur'],
            'ref_id_capteur': row['ref_id_capteur'],
            'date_insertion': row['date_insertion'],
            'unite_mesure': row['unite_mesure']
        })

    conn.close()
    return mesures

# Route pour obtenir les mesures
@app.route("/mesures", methods=["GET"])
def mesures():
    return jsonify(get_mesures())

# Route pour afficher les capteurs
@app.route('/capteurs', methods=['GET'])
def get_capteurs():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM Capteurs")
    capteurs = c.fetchall()
    conn.close()
    return jsonify([dict(capteur) for capteur in capteurs])

# Route pour ajouter un capteur
@app.route('/add-capteur', methods=['POST'])
def add_capteur():
    data = request.json
    reference_commerciale = data.get('reference_commerciale')
    port_COM = data.get('port_COM')
    ref_id_type_capteur = data.get('ref_id_type_capteur')
    ref_id_piece = data.get('ref_id_piece')

    conn = get_db_connection()
    conn.execute('''INSERT INTO Capteurs (reference_commerciale, port_COM, ref_id_type_capteur, ref_id_piece)
                    VALUES (?, ?, ?, ?)''', 
                    (reference_commerciale, port_COM, ref_id_type_capteur, ref_id_piece))
    conn.commit()
    conn.close()
    return jsonify({"message": "Capteur ajouté avec succès"}), 201

# Route pour récupérer les factures cumulées par type
@app.route('/factures/cumul', methods=['GET'])
def get_cumulative_factures():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = get_db_connection()
    cursor = conn.cursor()

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

    return jsonify(cumulative_data)

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Chat GPT et aide <!-- Avec l aide de Keryann, alias Pitit Chou --> et lien dans ReadME