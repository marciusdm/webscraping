from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from django.db import models


# Create your models here.
class MobileProcessor(models.Model):
    class Category(models.TextChoices):
        FLAGSHIP = "Flagship", _("Flagship")
        MID_RANGE = "Mid range", _("Mid range")
        LOW_END = "Low end", _("Low end")

    model = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=30)
    nano_review_score = models.IntegerField()
    nano_review_label = models.CharField(max_length=10)
    antutu_score = models.IntegerField()
    clock = models.IntegerField(null=True)
    cores_summary=models.CharField(max_length=20, null=True)
    geek_bench_score_single = models.IntegerField(null=True)
    geek_bench_score_multi = models.IntegerField(null=True)
    geek_bench_score_gpu = models.IntegerField(null=True)
    score_3d_mark = models.IntegerField(null=True)
    fps_3d_mark = models.IntegerField(null=True)
    cpu_frequency = models.IntegerField(null=True)
    architecture = models.CharField(max_length=200, null=True)
    cores = models.IntegerField(null=True)
    l2_cache = models.CharField(max_length=30, null=True)
    l3_cache = models.CharField(max_length=30, null=True)
    process_nanometers = models.IntegerField(null=True)
    tdp_watt = models.IntegerField(null=True)
    gpu_name = models.CharField(max_length=200, null=True)
    gpu_frequency = models.IntegerField(null=True)
    gpu_flops_gigaflops = models.IntegerField(null=True)
    gpu_pipelines = models.IntegerField(null=True)
    memory_type = models.CharField(max_length=20, null=True)
    memory_frequency = models.IntegerField(null=True)
    memory_max_size = models.IntegerField(null=True)
    max_display_resolution = models.CharField(max_length=60, null=True)
    max_camera_resolution = models.CharField(max_length=60, null=True)
    video_capture = models.CharField(max_length=60, null=True)
    video_playbacks = models.CharField(max_length=60, null=True)
    support_4g = models.CharField(max_length=30, null=True)
    support_5g = models.BooleanField(null=True)
    download_max_speed = models.IntegerField(null=True)
    upload_max_speed = models.IntegerField(null=True)
    wifi_version = models.IntegerField(null=True)
    bluetooth_version = models.DecimalField(decimal_places=1, max_digits=4, null=True)
    announced = models.DateField(null=True)
    category = models.CharField(choices=Category.choices, max_length=20,null=True)
    source = models.CharField(null=True, max_length=255)