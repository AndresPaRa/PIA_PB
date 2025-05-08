import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=25.6751&longitude=-100.3185&hourly=temperature_2m&start_date=2025-02-23&end_date=2025-05-16"
respuesta=requests.get(url)

print(respuesta.status_code)
weather=respuesta.json()



lista = weather["hourly"]["temperature_2m"]
temperaturas = ''.join(str(lista))

archivo = r'C:\Users\Erick.Galaviz\OneDrive\FCFM\Python\SchoolWorks\PIA\temperaturas.txt'
archivo = open(archivo,'w')
archivo.write(temperaturas)
archivo.close()
