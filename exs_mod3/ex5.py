import requests

url = 'https://api.covid19api.com/country/brazil'

covidData = requests.get(url).json()

for data in covidData: 
  if data['Confirmed'] > 0:
    year, month, day = data['Date'][:10].split('-')

    print(f"O primeiro caso de Covid-19 no Brasil foi registrado no dia {day}/{month}/{year}")
    
    break