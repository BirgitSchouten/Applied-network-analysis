import requests
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

# for importing data from the courts, see documentation on: https://www.rechtspraak.nl/SiteCollectionDocuments/Technische-documentatie-Open-Data-van-de-Rechtspraak.pdf
# on URIs: https://en.wikipedia.org/wiki/Uniform_Resource_Identifier

# get relevant ECLI numbers
base_url = "http://data.rechtspraak.nl/uitspraken/zoeken?"

# define search parameters
search_params = {
    "type": "uitspraak",
    "return": "DOC",
    "max": "1000",
    "sort": "DESC"
}

# encode difficult chars in string to %xx for a url
search_string = urlencode(search_params, safe = ':/')

# get ECLI numbers from API
response = requests.get(base_url, params = search_string)

#translate to string type
response_string = response.text

# read xml in nice format to get a vibe of the structure
# dom = minidom.parseString(response_string)
# pretty_string = dom.toprettyxml()
# print(pretty_string)

# clean string to excluse namespace for more easy extraction of the ECLI numbers
start = " xmlns"
end = "</updated>"

string1, string2 = response_string.split(start)
string3, string4 = string2.split(end, 1)
clean_string = string1 + ">" + string4

# parse xml format
root = ET.fromstring(clean_string)

ECLI_numbers = []

# iterate through all ECLI numbers to retrieve documents later
for child in root.iter('id'):
    ECLI_numbers.append(child.text)

# save ECLI in file to extract verdicts
with open('ECLI/algemeen.txt', 'w') as output:
    for number in ECLI_numbers:
        output.write(f"{number}\n")