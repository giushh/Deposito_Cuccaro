"""Create un programma python che permette tramite le api di visualizzare le previsione
metereologiche della città scelta dall'utente.
L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni."""

import requests
import json
import datetime as dt
from termcolor import colored as c


while True:
    city = input("Inserisci il nome della città o 'esci' per uscire: ")
    
    if city.lower() == "esci":
        print("Arrivederci!")
        break

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=it&format=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")
        continue
    
    # response = requests.get(url)
    
    # print(f"Status Code: {response.status_code}")
    # time.sleep(2)
    
    data = response.json()
    data_diz = json.dumps(data, indent=4, sort_keys=True)
    print(data_diz)
    
    if len(data.get('results', [])) == 0:
        print("Città non trovata. Riprova.")
        continue
    else:
        #recupero latitudine e longitudine
        lat = data['results'][0]['latitude']
        lon = data['results'][0]['longitude']
    
    days = input("Quanti giorni di previsione vuoi visualizzare? (1, 3, 7): ")
    if days not in ['1', '3', '7']:
        print("Scelta non valida. Riprova.")
        continue
    

    url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&hourly=temperature_10m&hourly=windspeed_10m&hourly=precipitation&past_days=1&forecast_days={days}&timezone=auto"
    
    try:
        response2 = requests.get(url2)
        response2.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")
        continue

    # response2 = requests.get(url2)

    # print(f"Status Code: {response2.status_code}")
    # time.sleep(2)

    data2 = response2.json()
    data_diz2 = json.dumps(data2, indent=4, sort_keys=True)
    print(data_diz2)

    #estraggo le informazioni richieste
    days_forecast = data2.get('hourly', {}).get('time', [])
    days_forecast = [dt.datetime.strptime(d, '%Y-%m-%dT%H:%M').strftime('%d-%m-%Y %H:%M') for d in days_forecast]
    temperature = data2.get('hourly', {}).get('temperature_2m', [])
    wind_speed = data2.get('hourly', {}).get('windspeed_10m', [])
    precipitation = data2.get('hourly', {}).get('precipitation', [])

    # print(type(temperature), type(wind_speed), type(precipitation))
    # print(f"Temperature: {temperature}")
    # print(f"Wind Speed: {wind_speed}")
    # print(f"Precipitation: {precipitation}")

    for i in range(len(temperature)):
        if len(wind_speed) <= 0 or len(precipitation) <= 0:
            print(c(f"Giorno: {days_forecast[i]}, Temperatura: {temperature[i]}°C, Velocità del vento: N/A, Precipitazioni: N/A", "red"))
        else:
            print(
                    f"Giorno: {c(days_forecast[i], 'cyan')}, "
                    f"Temperatura: {c(str(temperature[i]) + '°C', 'red')}, "
                    f"Velocità del vento: {c(str(wind_speed[i]) + ' km/h', 'yellow')}, "
                    f"Precipitazioni: {c(str(precipitation[i]) + ' mm', 'blue')}"
                )

