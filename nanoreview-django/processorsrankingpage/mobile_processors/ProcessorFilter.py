import django_filters
from .custom_widgets import MyRangeWidget
from .models import MobileProcessor
from .custom_filters import FilterIntervalYears
from django.utils.translation import gettext as _
class MobileProcessorFilter(django_filters.FilterSet):
    antutu_score = django_filters.RangeFilter(label=_("Antutu score"),
                                              widget=MyRangeWidget(from_attrs={'placeholder': _('Minimum Score')},
                                                                   to_attrs={'placeholder': _('Maximum score')}))
    category = django_filters.ChoiceFilter(label=_("Category"), choices=MobileProcessor.Category.choices)
    manufacturer = django_filters.AllValuesFilter(label=_("Manufacturer"), field_name='manufacturer')
    announced = FilterIntervalYears(label= _("Announced date"))

    class Meta:
        model = MobileProcessor
        fields = []
