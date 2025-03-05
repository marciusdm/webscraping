from django.utils.translation import gettext as _
def convert_yesno_to_bool(value):
    if value is None:
        return None
    if str(value).lower() == "yes":
        return True
    return False


def convert_bool_to_yes_no(value):
    if value is not None:
        if value is True:
            return _("Yes")
        return _("No")
    return ""
