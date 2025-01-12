import pandas as pd
from datetime import datetime, timedelta

# Exemple de données brutes simulées (corrigez pour qu'elles proviennent de votre API)
hourly_data = pd.DataFrame({
    "datetime": pd.date_range(start="2025-01-12 00:00:00", periods=24*5, freq='H'),
    "temperature_2m": [1.917 + i * 0.1 for i in range(24*5)],
    "weathercode": [3] * (24*5)
})

# Conversion au format datetime
hourly_data["datetime"] = pd.to_datetime(hourly_data["datetime"])

# Arrondi des températures au degré entier tronqué
hourly_data["temperature_2m"] = hourly_data["temperature_2m"].apply(int)

# Extraire uniquement les données à 8h
hourly_data["hour"] = hourly_data["datetime"].dt.hour
hourly_data["date"] = hourly_data["datetime"].dt.date  # On extrait la date sans l'heure
data_at_8h = hourly_data[hourly_data["hour"] == 8]

# Mapper les descriptions de weathercode (simplifié)
weathercode_mapping = {
    0: "Clair",
    1: "Principalement clair",
    2: "Partiellement nuageux",
    3: "Nuageux",
    45: "Brouillard",
    48: "Brouillard givrant",
    51: "Bruine légère",
    61: "Pluie légère",
    71: "Chute de neige légère",
    95: "Orage"
}
data_at_8h["weather_description"] = data_at_8h["weathercode"].map(weathercode_mapping)

# Associer les jours J0, J1, ..., J4
start_date = data_at_8h["date"].min()
data_at_8h["day_label"] = data_at_8h["date"].apply(lambda x: f"J{x.toordinal() - start_date.toordinal()}")

# Filtrer les 5 jours
forecast = data_at_8h[["day_label", "temperature_2m", "weather_description"]].head(5)

# Si des jours manquent, remplir avec "Non disponible"
days = [f"J{i}" for i in range(5)]
forecast = pd.DataFrame(days, columns=["day_label"]).merge(
    forecast, on="day_label", how="left"
)
forecast.fillna({"temperature_2m": "Non disponible", "weather_description": "Non disponible"}, inplace=True)

# Affichage final
print("\nPrévisions météo pour les 5 prochains jours à 8h :")
print(forecast)

#Gpt ed et code du site en readme