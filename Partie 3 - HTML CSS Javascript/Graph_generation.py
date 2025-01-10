from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import sqlite3
from datetime import datetime

app = FastAPI()

# Fonction pour initialiser la connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('../Partie 1 - Base de donnee/logement.db')
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

# Route pour générer un graphique à partir des données
@app.get("/factures/conso_chart/", response_class=HTMLResponse)
async def generate_pie_chart():  # Conso_chart
    # Connexion à la base de données
    conn = get_db_connection()
    cursor = conn.cursor()

    # Récupérer les données agrégées par date et type de facture
    cursor.execute("""
        SELECT date_emission, type_facture, consommation
        FROM Factures
        ORDER BY date_emission
    """)
    data = cursor.fetchall()
    conn.close()

    if not data:
        return HTMLResponse(content="<p>Aucune donnée à afficher pour le graphique.</p>")

    # Regroupement des données par jour et par type de facture
    factures_par_jour = {}
    types_factures = ['Electricité', 'Eau', 'Gaz', 'Déchets', 'Téléphone', 'Internet']

    for row in data:
        date = row["date_emission"].split()[0]  # Extraire uniquement la date (sans l'heure)
        type_facture = row["type_facture"]
        consommation = row["consommation"]

        if date not in factures_par_jour:
            factures_par_jour[date] = {}

        if type_facture == "Déchets":
            # Pour les déchets, on incrémente de 1 pour chaque facture, même si la consommation est NULL
            consommation = 1
        elif consommation is None:
            consommation = 0  # Si la consommation est NULL pour d'autres factures, on met à 0

        # Ajouter la consommation à la date et au type de facture approprié
        if type_facture not in factures_par_jour[date]:
            factures_par_jour[date][type_facture] = 0

        factures_par_jour[date][type_facture] += consommation

    # Organiser les données pour Google Charts
    chart_data = [['Date'] + types_factures]  # Première ligne : en-tête des colonnes

    for date, factures in factures_par_jour.items():
        ligne = [date]
        for type_facture in types_factures:
            consommation = factures.get(type_facture, 0)  # Utiliser 0 si le type de facture n'existe pas pour ce jour
            ligne.append(consommation)
        chart_data.append(ligne)

    # Conversion des données en format JSON-compatible
    chart_data_json = str(chart_data).replace("'", '"')

    # HTML avec Google Charts
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
        google.charts.load('current', {{'packages':['corechart', 'line']}});  // Charge la bibliothèque Line pour les courbes
        google.charts.setOnLoadCallback(drawChart);

        function drawChart() {{
            var data = google.visualization.arrayToDataTable({chart_data_json});

            var options = {{
                title: 'Répartition des Consommations par Jour',
                hAxis: {{
                    title: 'Date',
                    format: 'yyyy.MM.dd',  // Formater les dates
                }},
                vAxis: {{
                    title: 'Consommation Total',
                    minValue: 0
                }},
                vAxes: {{
                    0: {{
                        title: 'Consommation (unités)',
                        minValue: 0
                    }},
                    1: {{
                        title: 'Déchets (Nombre de Factures)',
                        minValue: 0
                    }}
                }},
                series: {{
                    0: {{ targetAxisIndex: 0 }},
                    1: {{ targetAxisIndex: 0 }},
                    2: {{ targetAxisIndex: 0 }},
                    3: {{ targetAxisIndex: 1 }},
                    4: {{ targetAxisIndex: 0 }},
                    5: {{ targetAxisIndex: 0 }}
                }},
                isStacked: true,  // Empile les courbes pour une visualisation claire
                curveType: 'none', //'function',  // Courbes lissées pour les lignes
                legend: {{
                    position: 'top'
                }},
                height: 500
            }};

            var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
            chart.draw(data, options);
        }}
        </script>
    </head>
    <body>
        <div id="chart_div" style="width: 70%; height: 500px;"></div>
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