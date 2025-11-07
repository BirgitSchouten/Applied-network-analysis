import xml.etree.ElementTree as ET
from test2 import find_ECLI_in_string

ecli_id_dictionary = {}
with open("output/nodelist.csv", 'r') as infile:
    next(infile)
    for line in infile:
        id, ecli, rechtsgebied, subrechtsgebied = line.split(", ")
        ecli_id_dictionary[ecli] = id

ecli_location_dictionary = {}
with open("ECLI/algemeen_totaal.txt", 'r') as infile:
    for line in infile:
        ecli, location = line.strip().split(", ")
        ecli_location_dictionary[ecli] = location

with open("output/edgelist.csv", 'w') as outfile:
    # loop through all nodes
    for key in ecli_id_dictionary.keys():
        # open verdict file, ignore ecli numbers with only metadata
        if ecli_location_dictionary[key] != "algemeen_referenties2":
            with open(f"output/{ecli_location_dictionary[key]}/{key}.txt", 'r') as infile:
                whole_text = infile.read()

                # parse XML file
                tree = ET.fromstring(whole_text)

                # iterate over tree and branches to find actual verdict
                for branch in tree:
                    if 'uitspraak' in branch.tag:
                        verdict = branch
                
                # filter only referenced ECLI number
                verdict_referenced_ECLI_numbers = []
                for child in verdict.iter():
                    if child.text:
                        line = child.text
                        if "ECLI:" in line:
                            verdict_referenced_ECLI_numbers.extend(find_ECLI_in_string(line))
                
                # print to edgelist if there are connections
                if verdict_referenced_ECLI_numbers:

                    # filter out wrong ECLI numbers

                    for number in range(0, len(verdict_referenced_ECLI_numbers)):
                        try:
                            specific_ECLI_number = verdict_referenced_ECLI_numbers[number]
                            outfile.write(f"{ecli_id_dictionary[key]},{ecli_id_dictionary[specific_ECLI_number]}\n")
                        except:
                            pass
                
                # clean reference list
                verdict_referenced_ECLI_numbers = []