## Descargo dependencias
!pip install openmeteo-requests
!pip install requests-cache retry-requests numpy pandas
import requests
from datetime import date, timedelta

# Cohsulto el tiempo actual
  def consultar_clima(lat, lon):
      # Endpoint de Open-Meteo con variables: temperatura, lluvia y chubascos
      url = (
          f"https://api.open-meteo.com/v1/forecast?"
          f"latitude={lat}&longitude={lon}"
          f"&current=temperature_2m,rain,showers,cloud_cover,relative_humidity_2m"
      )

      response = requests.get(url)

      if response.status_code == 200:
          data = response.json()
          clima = data["current"]
          print("\n📍 Coordenadas:", f"Lat {lat}, Lon {lon}")
          print("🌡️ Temperatura:", clima.get("temperature_2m"), "°C")
          print("🌧️ Lluvia:", clima.get("rain"), "mm")
          print("🌦️ Chubascos:", clima.get("showers"), "mm")
          print("🌦️ Humedad:", clima.get("relative_humidity_2m"), "%")
          print("🌦️ Cobertura Nubosa:", clima.get("cloud_cover"), "%")
      else:
          print("❌ Error en la petición:", response.status_code)


  if __name__ == "__main__":
      # pedir input al usuario
      lat = input("Ingrese la latitud: ")
      lon = input("Ingrese la longitud: ")

      consultar_clima(lat, lon)

# Consulto el clima histórico
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
    print(datos)  # salida en JSON

