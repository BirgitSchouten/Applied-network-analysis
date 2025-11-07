import xml.etree.ElementTree as ET

ecli_id_dictionary = {}
with open("output/nodelist.csv", 'r') as infile:
    for line in infile:
        id, ecli, rechtsgebied, subrechtsgebied = line.split(", ")
        ecli_id_dictionary[ecli] = id

