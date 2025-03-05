from time import sleep

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django_tables2 import SingleTableView
from . import ProcessorFilter
from .ProcessorFilter import MobileProcessorFilter
from .models import MobileProcessor
from .table import MobileProcessorTable
from mobile_processors.bridge.get_processors_from_nanoreview import start_crawler
from django_tables2 import RequestConfig
from django.urls import reverse


# Create your views here.
def index(request):
    mobile_processors_list = MobileProcessor.objects.all()
    f = MobileProcessorFilter(request.GET, queryset=mobile_processors_list)
    table = MobileProcessorTable(f.qs)
    #table.paginate(page=request.GET.get("page", 1), per_page=10)
    RequestConfig(request, paginate={"page": request.GET.get("page", 1), "per_page": 10}).configure(table)
    context = {
        "table": table,
        'filter': f,
#        'redirect_to': request.path
    }
    return render(request, "mobile_processors/index.html", context)


def detail(request, processor_id):
    processor = get_object_or_404(MobileProcessor, pk=processor_id)
    return render(request, "mobile_processors/detail.html", {"processor": processor})


def load_processors(request):
    if request.method == "POST":
        start_crawler()
        # sleep(10)
    return HttpResponse("OK", status=200)
