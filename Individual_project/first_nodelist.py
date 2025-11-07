import xml.etree.ElementTree as ET

# get all ECLI numbers because these are also the names of the files
ECLI_numbers = []
with open("ECLI/algemeen_totaal.txt", 'r') as infile:
    for line in infile:
        number, location = line.strip().split(", ")
        ECLI_numbers.append([number, location])

counter = 1
with open("output/nodelist.csv", 'w') as outfile:
    outfile.write("id, ECLI, rechtsgebied, subrechtsgebied\n")
    for ecliloc in ECLI_numbers:
        ecli, location = ecliloc[0], ecliloc[1]
        with open(f"output/{location}/{ecli}.txt", 'r') as infile:
            whole_text = infile.read()

            # parse XML file
            tree = ET.fromstring(whole_text)

            # iterate over tree and branches to find actual verdict, only ECLI numbers in the verdict or footnotes are references
            for branch in tree:
                if 'RDF' in branch.tag:
                    rdf = branch

            # filter law subtype from rdf
            for child in rdf.iter():
                if 'subject' in child.tag:
                    try:
                        main_subject, subtopic = child.text.split('; ')
                    except:
                        main_subject = child.text
                        subtopic = ""
                elif 'creator' in child.tag:
                    rechtbank = child.text

            outfile.write(f"{counter}, {ecli}, {main_subject}, {subtopic}\n")
        counter += 1