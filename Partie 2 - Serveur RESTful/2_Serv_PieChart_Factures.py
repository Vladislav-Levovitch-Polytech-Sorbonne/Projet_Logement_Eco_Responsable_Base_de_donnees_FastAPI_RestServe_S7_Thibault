from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
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

@app.get("/factures/pie_chart/", response_class=HTMLResponse)
async def generate_pie_chart():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT type_facture, SUM(montant) as total FROM Factures GROUP BY type_facture")
    data = cursor.fetchall()
    conn.close()

    # Vérification des données dans la console
    print(data)

    if not data:
        return HTMLResponse(content="<p>Aucune donnée à afficher pour le graphique.</p>")

    # Conversion des résultats SQL en un format compatible avec Google Charts
    donnees = [["type_facture", "total"]]  # En-têtes des colonnes
    for row in data:
        # Chaque 'row' est un objet sqlite3.Row, donc on doit accéder à chaque colonne par son nom
        donnees.append([row["type_facture"], row["total"]])

    # Conversion en chaîne JSON-compatible (remplacement des apostrophes par des guillemets)
    donnee_convertie = str(donnees).replace("'", '"')

    # HTML avec Google Charts
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
            google.charts.load('current', {{'packages':['corechart']}}); 
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {{
                var data = google.visualization.arrayToDataTable({donnee_convertie});
                var options = {{
                    title: 'Répartition des couts globaux par consommation',
                    pieHole: 0.4,
                }};
                var chart = new google.visualization.PieChart(document.getElementById('piechart'));
                chart.draw(data, options);
            }}
        </script>
    </head>
    <body>
        <div id="piechart" style="width: 1200px; height: 600px;"></div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

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