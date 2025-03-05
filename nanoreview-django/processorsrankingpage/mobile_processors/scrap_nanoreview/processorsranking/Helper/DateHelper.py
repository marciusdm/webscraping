import re


############################################################
# en. Converts an english date in format MMMM,yyyy, where MMMM is a month in full version
# mm/yyyy format e.g January 2024 to 01/06/2024
####
# pt. Converte uma data no formato MMMM, dd (MMMMM: mês por extenso em inglês) para
# o formato aaaa-mm-dd
def convert_english_date(dt):
    dict_date = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    token_date = r"(\w+)\D+(\d+)"
    match = re.match(token_date, dt)
    date = "{}-{}-01".format(match.group(2), dict_date[match.group(1)])
    return date
