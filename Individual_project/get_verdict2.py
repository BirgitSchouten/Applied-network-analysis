import requests
from urllib.parse import urlencode

# define base_url for retrieving verdict
base_url = "https://data.rechtspraak.nl/uitspraken/content?"

search_params = {
    "id": "ECLI:NL:RBDHA:2025:20814",
}

# encode difficult chars in string to %xx for a url
search_string = urlencode(search_params, safe = ':/')

# get verdict from API
response = requests.get(base_url, params = search_string)

# print to output file for analysing how to edit and select relevant data
with open('output/full_XML_response.txt', 'w') as outfile:
    outfile.write(response.text)