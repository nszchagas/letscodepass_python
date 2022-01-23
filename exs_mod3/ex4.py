from dataclasses import dataclass
import requests

url = 'https://swapi.dev/api/people/4/'
print('Requesting data...')
darthVader = requests.get(url).json()
print(f"\nName: {darthVader['name']}\nHeight: {darthVader['height']}\nMass:{darthVader['mass']}\nBirth Year:{darthVader['birth_year']} ")

