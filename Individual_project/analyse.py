import xml.etree.ElementTree as ET

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
# create class to store this info
class Node:
    def __init__(self, ecli_number, main_subject, subtopic, references):
        self.ecli_number = ecli_number
        self.main_subject = main_subject
        self.subtopic = subtopic
        self.court = self.find_court()
        self.references = references
    
    def find_court(self):
        first_selection = self.ecli_number.removeprefix('ECLI:NL:')
        location = first_selection.find(':')
        return first_selection[:location]


for ecli in ECLI_numbers:
    with open(f"output/algemeen/{ecli}.txt", 'r') as infile:
        whole_text = infile.read()

        # parse XML file
        tree = ET.fromstring(whole_text)

        # iterate over tree and branches to find actual verdict, only ECLI numbers in the verdict or footnotes are references
        for branch in tree:
            if 'RDF' in branch.tag:
                rdf = branch
            if 'uitspraak' in branch.tag:
                verdict = branch

        # filter law subtype from rdf
        for child in rdf.iter():
            if 'subject' in child.tag:
                main_subject, subtopic = child.text.split('; ')

        # filter out only referenced ECLI numbers, not the cleanest code but it works
        referenced_ECLI_numbers = []
        for child in verdict.iter():
            if child.text:
                line = child.text
                if "ECLI:" in line:
                    words = line.split()
                    referenced_ECLI_numbers.extend([word for word in words if "ECLI:" in word])

        # clean ECLI numbers of possible interpuction
        clean_referenced_ECLI_numbers = []
        for number in referenced_ECLI_numbers:
            if not number[-1].isnumeric():
                clean_referenced_ECLI_numbers.append(number[:-1])
            else:
                clean_referenced_ECLI_numbers.append(number)

