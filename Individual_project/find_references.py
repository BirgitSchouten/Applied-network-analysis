import xml.etree.ElementTree as ET
from test2 import find_ECLI_in_string

# get all ECLI numbers because these are also the names of the files
ECLI_numbers = []
with open("ECLI/algemeen.txt", 'r') as infile:
    for line in infile:
        ECLI_numbers.append(line.strip())

# the info I want for each verdict:
# the ECLI_number, which is the name of the file so got that, will go into nodelist
# the law subtype the verdict is classified as, will go into nodelist
# which court made the verdict, which is part of the ECLI number, will go into nodelist
# all ECLI numbers it references, will go into edgelist

referenced_ECLI_numbers = set()
for ecli in ECLI_numbers:
    with open(f"output/algemeen/{ecli}.txt", 'r') as infile:
        whole_text = infile.read()

        # parse XML file
        tree = ET.fromstring(whole_text)

        # iterate over tree and branches to find actual verdict, only ECLI numbers in the verdict or footnotes are references
        for branch in tree:
            if 'uitspraak' in branch.tag:
                verdict = branch

        # filter out only referenced ECLI numbers, not the cleanest code but it works
        verdict_referenced_ECLI_numbers = []
        for child in verdict.iter():
            if child.text:
                line = child.text
                if "ECLI:" in line:
                    verdict_referenced_ECLI_numbers.extend(find_ECLI_in_string(line))
        
        for number in verdict_referenced_ECLI_numbers:
            referenced_ECLI_numbers.add(number)

with open("ECLI/referenties_algemeen1.txt", 'w') as outfile:
    for number in referenced_ECLI_numbers:
        outfile.write(f"{number}\n")