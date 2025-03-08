from datetime import timedelta, datetime
from django.utils.timezone import now
from django_filters.filters import DateRangeFilter
from django.utils.translation import gettext_lazy as _



def _truncate(dt):
    return dt.date()


def _get_date_from_delta_years(date, years_delta):
    return datetime(date.year - years_delta, date.month, 1)


class FilterIntervalYears(DateRangeFilter):
    choices = [
        ("last_1_year", _("Last 12 months")),
        ("last_2_years", _("Last 2 years")),
        ("last_3_years", _("Last 3 years")),
        ("last_4_years", _("Last 4 years")),
        ("last_5_years", _("Last 5 years")),
    ]

    filters = {
        "last_1_year": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(_get_date_from_delta_years(now(), 1)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
        "last_2_years": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(_get_date_from_delta_years(now(), 2)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
        "last_3_years": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(_get_date_from_delta_years(now(), 3)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
        "last_4_years": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(_get_date_from_delta_years(now(), 4)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
        "last_5_years": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(_get_date_from_delta_years(now(), 5)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
    }
