## Descargo dependencias
!pip install openmeteo-requests
!pip install requests-cache retry-requests numpy pandas
import requests
from datetime import date, timedelta

## Clima histórico, recibe por fn parameter lat y lon
def clima_historico_json(lat=-34.61, lon=-58.38):
    """
    Consulta clima histórico (últimos 7 días) y devuelve un JSON
    con temperatura máx/mín, lluvia y chubascos.
    Por defecto usa Buenos Aires.
    """

    # calcular rango de fechas (últimos 7 días hasta ayer)
    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=6)

    # endpoint de Open-Meteo Archive
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min,rain_sum,showers_sum"
        f"&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # devolvemos el JSON crudo de la API
    else:
        return {
            "error": response.status_code,
            "mensaje": response.text
        }


if __name__ == "__main__":
    datos = clima_historico_json()
    print(datos)  # acá ves el JSON completo