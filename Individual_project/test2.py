def check_ECLI_number(country_code, court_code, year, identifying_number):
    if country_code != "NL":
        return False
    if not court_code.strip().isalpha():
        return False
    if year < 1900:
        return False
    if not identifying_number.strip().isalnum():
        return False
    return True
    

def find_ECLI_in_string(line):
    ecli_numbers = []
    line_end = len(line)
    # start after ECLI:
    location = 0
    while location <= line_end:
        start = line[location:].find("ECLI:")
        if start == -1:
            break
        # print("location: ", location)
        # print("line end is ", line_end)
        location += start + 5
        # loop through country code until next :
        country_code = ""
        while line[location] != ':':
            country_code += line[location]
            location += 1
        # skip : after country code
        # print("country code: ", country_code)
        location += 1
        # loop through court code until next :
        court_code = ""
        while line[location] != ':':
            court_code += line[location]
            location += 1
        # print("court code: ", court_code)
        location += 1
        # get year
        year = 0
        try:
            year = int(line[location:location+4])
        except:
            year = 1
        # print("year: ", year)
        if (location + 5) < line_end:
            location += 5
        else:
            break
        # get unique identifying number
        identifying_number = ""
        while line[location].isalnum():
            identifying_number += line[location]
            if (location + 1) < line_end:
                location += 1
            else:
                break
        if check_ECLI_number(country_code, court_code, year, identifying_number):
            found_ECLI = "ECLI:" + country_code + ":" + court_code + ":" + str(year) + ":" + identifying_number
            ecli_numbers.append(found_ECLI)
        location += 1
        country_code = ""
        court_code = ""
        year = 0
        identifying_number = ""
    return(ecli_numbers)