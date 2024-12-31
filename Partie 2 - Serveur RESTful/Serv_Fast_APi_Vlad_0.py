from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Fonction pour initialiser la connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('logement.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route pour récupérer toutes les factures
@app.get("/factures/")
async def get_factures():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Factures")
    factures = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"factures": factures}

# Route pour ajouter une nouvelle facture
@app.post("/factures/")
async def create_facture(type_facture: str, montant: float, ref_id_logement: int, date_emission: str, consommation: float = None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO Factures (type_facture, montant, consommation, ref_id_logement, date_emission) VALUES (?, ?, ?, ?, ?)",
            (type_facture, montant, consommation, ref_id_logement, date_emission),
        )
        conn.commit()
    except sqlite3.Error as e:
        conn.close()
        raise HTTPException(status_code=400, detail=str(e))

    conn.close()
    return {"message": "Facture ajoutée avec succès"}

# Route pour récupérer toutes les mesures
@app.get("/mesures/")
async def get_mesures():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Mesures")
    mesures = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"mesures": mesures}

# Route pour ajouter une nouvelle mesure
@app.post("/mesures/")
async def create_mesure(valeur: float, ref_id_capteur: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO Mesures (valeur, ref_id_capteur) VALUES (?, ?)",
            (valeur, ref_id_capteur),
        )
        conn.commit()
    except sqlite3.Error as e:
        conn.close()
        raise HTTPException(status_code=400, detail=str(e))

    conn.close()
    return {"message": "Mesure ajoutée avec succès"}

# Tres Chat GPT comprehension moderement limitee