import xml.etree.ElementTree as ET

# # parse XML file
# tree = ET.fromstring(response.text)

# # iterate over tree and branches to find actual verdict and skip extra info for now
# for branch in tree:
#     if 'uitspraak' in branch.tag:
#         uitspraak = branch

# # filter out only other ECLI numbers, not the cleanest code but it works
# ECLI_numbers = []
# for child in uitspraak.iter():
#     if child.text:
#         line = child.text
#         if "ECLI:" in line:
#             words = line.split()
#             ECLI_numbers.extend([word for word in words if "ECLI:" in word])

# # clean ECLI numbers of possible interpuction
# clean_ECLI_numbers = []
# for number in ECLI_numbers:
#     if not number[-1].isnumeric():
#         clean_ECLI_numbers.append(number[:-1])
#     else:
#         clean_ECLI_numbers.append(number)
# print(clean_ECLI_numbers)