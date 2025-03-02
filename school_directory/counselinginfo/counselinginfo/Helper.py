import logging
import re


class Helper:
    pattern_name_job = r"<p>(?P<name>[^,]+),\s*(?P<job>[^<]+)<br>"
    pattern_email = r"\n(Email:\s*)?(?P<mail>((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W]))"
    pattern_phone = r"\nPhone:\s*(?P<phone>[^<]+)"
    #  r"<p>(?P<name>[^,]+),\s*(?P<job>[^<]+)<br>\nEmail:\s*(?P<mail>[^<]+)(</p>|<br>\nPhone:\s*(?P<phone>"
    pattern_excessive_spaces = r"\s{2,}"
    pnj = re.compile(pattern_name_job)
    pe = re.compile(pattern_email)
    pp = re.compile(pattern_phone)
    pes = re.compile(pattern_excessive_spaces)

    @staticmethod
    def tokenize(line: str):

        line = line.replace("&amp;", "&")
        m1 = Helper.pnj.match(line)
        m2 = Helper.pe.search(line)
        m3 = Helper.pp.search(line)
        first_name, middle_name, last_name = Helper.token_names(m1.group('name'))

        job_title = m1.group('job')
        mail = phone = ""
        if m2 is not None:
            mail = m2.group('mail')
        else:
            logging.getLogger().warning(f"{first_name} {middle_name} {last_name}, {job_title}, has no e-mail")
        if m3 is not None:
            phone = m3.group('phone')
        return first_name, middle_name, last_name, job_title, mail, phone

    @staticmethod
    def token_names(full_name: str):
        treated_name = Helper.pes.sub(" ", full_name)
        all_names = treated_name.split(' ')
        name_len = len(all_names)
        if name_len <= 1:
            return "", "", ""
        if len(all_names) == 2:
            return all_names[0], "", all_names[1]

        if full_name.lower().find(" de la ") != -1:
            all_names[-3] = f"De La {all_names[-1]}"
            all_names.pop()
            all_names.pop()
        elif ["De", "Da", "Van", "Del"].count(all_names[-2]) > 0:
            all_names[-2] = f"{all_names[-2]} {all_names[-1]}"
            all_names.pop()
        if all_names[-1] == 'Jr' or all_names[-1] == "Jr.":
            all_names[-2] = f"{all_names[-2]} Jr"
            all_names.pop()
        if ["Mrs", "Mr.", "Mrs.", "Dr.", "Ms."].count(all_names[0]) > 0:
            all_names[1] = f"{all_names[0]} {all_names[1]}"
            all_names.pop(0)
        if len(all_names) > 2:
            return all_names[0], all_names[1], all_names[-1]
        return all_names[0], "", all_names[1]
