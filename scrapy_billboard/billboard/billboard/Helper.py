import re


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
    date = "{}/{}/{}".format(match.group(2).zfill(2), dict_date[match.group(1)], year)
    return date


def is_note_or_empty(text):
    pattern = r"(\[\d+\]+|^$)"
    return re.search(pattern, text)


def strip_html_and_quotes(text):
    regex = r"<[^>]+>"
    stripped_text = (re.sub(regex, "", text).replace("\"", "")
                     .replace("\n", "")
                     .replace("&amp;","&"))
    return stripped_text





def strip_song_of_the_year_mark(text):
    return text.replace("†", "")
