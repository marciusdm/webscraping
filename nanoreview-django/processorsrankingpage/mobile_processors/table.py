import django_tables2 as tables
from .models import  MobileProcessor
from django.utils.translation import gettext_lazy as _

from django.utils import dateformat
class MobileProcessorTable(tables.Table):

    def __init__(self, *args, **kwargs):
        super(MobileProcessorTable, self).__init__(*args, **kwargs)

    manufacturer = tables.Column(verbose_name=_("Manufacturer"))
    model = tables.Column(verbose_name=_("Model"), linkify=("mobile_processors:detail", [tables.A("pk")]))
    #nano_review_label = tables.Column(visible=False)
    category = tables.Column(verbose_name=_("Category"))
    nano_review_score = tables.Column(verbose_name=_("Short NanoReview Score"))
    antutu_score = tables.Column(verbose_name=_("Antutu Score"))
    clock = tables.Column(verbose_name=_("Clock"))
    cores = tables.Column(verbose_name=_("Cores"))
    announced = tables.DateTimeColumn(verbose_name=_("Announced"), format='m/Y')

    def render_nano_review_score(self, value, record):
        return f"{value} [{record.nano_review_label}]"

    class Meta:
        attrs = {"class": "table table-responsive table-striped table-hover"}
        model = MobileProcessor
        template_name = 'django_tables2/bootstrap5.html'
        fields = ("manufacturer","model","category","nano_review_score",
                "antutu_score","clock","cores","announced")

