import re


def strip_non_numeric(value):
    pattern = r"\D"
    return re.sub(pattern, "", value)


def strip_non_alpha_numeric(value):
    return (value.replace("\t", "")
            .replace("\n", "")
            .replace("–","-")
            .strip())


def replace_br_char(value):
    return (value.replace("\n", "")
            .replace("<br>", ", ")
            .strip())
