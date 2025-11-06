import requests
from urllib.parse import urlencode

# define base_url for retrieving verdict
base_url = "https://data.rechtspraak.nl/uitspraken/content?"

# define search params from retrieved ECLI numbers
with open("ECLI/bestuursrecht_algemeen.txt", 'r') as input:
    for line in input:
        ecli = line.strip()

        search_params = {
            "id": ecli
        }

        # encode difficult chars in string to %xx for a url
        search_string = urlencode(search_params, safe = ':/')

        # get verdict from API
        response = requests.get(base_url, params = search_string)

        # print to output file for analysing how to edit and select relevant data
        with open(f"output/{ecli}.txt", 'w') as outfile:
            outfile.write(response.text)