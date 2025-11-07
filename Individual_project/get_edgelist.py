import xml.etree.ElementTree as ET

ECLI_numbers = []
with open("output/nodelist.csv", 'r') as infile:
    for line in infile:
        id, ecli, rechtbank, rechtsgebied, subrechtsgebied = line.split(", ")
        print(id, ecli, rechtsgebied, subrechtsgebied)