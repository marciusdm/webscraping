
import re

############################################################
# en. Converts an english date in format MMMM,dd, where MMMM is a month in full version
# dd/mm/yyyy format e.g January 12, 1984 to 12/01/1984
####
# pt. Converte uma data no formato MMMM, dd (MMMMM: mês por extenso em inglês) para
# o formato dd/mm/aaaa
def convert_english_date(dt, year):
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
    date = "{}-{}-{}".format(year, dict_date[match.group(1)], match.group(2).zfill(2))
    return date




