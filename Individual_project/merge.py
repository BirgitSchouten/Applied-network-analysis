all_ecli_numbers = []

with open("ECLI/algemeen.txt", 'r') as infile:
    for line in infile:
        all_ecli_numbers.append([line.strip(), "algemeen"])

with open("ECLI/referenties_algemeen1.txt", 'r') as infile:
    for line in infile:
        number = line.strip()
        if number not in all_ecli_numbers:
            all_ecli_numbers.append([number.strip(), "algemeen_referenties"])

with open("ECLI/referenties_algemeen2.txt", 'r') as infile:
    for line in infile:
        number = line.strip()
        if number not in all_ecli_numbers:
            all_ecli_numbers.append([number.strip(), "algemeen_referenties2"])

with open("ECLI/algemeen_totaal.txt", 'w') as outfile:
    for numberloc in all_ecli_numbers:
        number, location = numberloc[0], numberloc[1]
        outfile.write(f"{number}, {location}\n")