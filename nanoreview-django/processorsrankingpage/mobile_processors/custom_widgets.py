from django_filters.widgets import RangeWidget


class MyRangeWidget(RangeWidget):
    template_name = "my_range_widget.html"

    def __init__(self, from_attrs=None, to_attrs=None, attrs=None):
        super(MyRangeWidget, self).__init__(attrs)

        if from_attrs:
            self.widgets[0].attrs.update(from_attrs)
        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)