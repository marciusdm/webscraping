from mobile_processors.models import MobileProcessor
from itemadapter import ItemAdapter
from mobile_processors.bridge.BooleanHelper import convert_yesno_to_bool

def insert_or_update_summary(adapter):
    p = MobileProcessor.objects.filter(manufacturer=adapter["manufacturer"],
                                       model=adapter["model"])
    if p:
        print("model " + adapter["model"] +" already in database")
        return

    the_model = adapter["model"]
    if the_model == "Apple A18":
        the_model = "A18"
    p = MobileProcessor(
        model=the_model,
        manufacturer=adapter["manufacturer"],
        antutu_score=adapter["antutu_score"],
        nano_review_score=adapter["nano_review_score"],
        nano_review_label=adapter["nano_review_label"],
        clock=adapter["clock"],
        cores_summary=adapter["cores"]
    )
    p.save()


def insert_or_update_detail(adapter):
    manufacturer, model = adapter["manufacturer_model"].split(" ", 1)
    p = MobileProcessor.objects.filter(manufacturer__iexact= manufacturer,
                                       model= model)
    if not p:
        p = MobileProcessor.objects.filter(model=adapter["manufacturer_model"])
    if p:
        p[0].geek_bench_score_single = get_key_or_null(adapter, "geek_bench_score_single")
        p[0].geek_bench_score_multi = get_key_or_null(adapter, "geek_bench_score_multi")
        p[0].geek_bench_score_gpu = get_key_or_null(adapter, "geek_bench_score_gpu")
        p[0].score_3d_mark = get_key_or_null(adapter, "score_3d_mark")
        p[0].fps_3d_mark = get_key_or_null(adapter, "fps_3d_mark")
        p[0].cpu_frequency = get_key_or_null(adapter, "cpu_frequency")
        p[0].architecture = get_key_or_null(adapter, "architecture")
        p[0].cores = get_key_or_null(adapter, "cores")
        p[0].l2_cache = get_key_or_null(adapter, "l2_cache")
        p[0].l3_cache = get_key_or_null(adapter, "l3_cache")
        p[0].process_nanometers = get_key_or_null(adapter, "process_nanometers")
        p[0].tdp_watt = get_key_or_null(adapter, "tdp_watt")
        p[0].gpu_name = get_key_or_null(adapter, "gpu_name")
        p[0].gpu_frequency = get_key_or_null(adapter, "gpu_frequency")
        p[0].gpu_flops_gigaflops = get_key_or_null(adapter, "gpu_flops_gigaflops")
        p[0].gpu_pipelines = get_key_or_null(adapter, "gpu_pipelines")
        p[0].memory_type = get_key_or_null(adapter, "memory_type")
        p[0].memory_frequency = get_key_or_null(adapter, "memory_frequency")
        p[0].memory_max_size = get_key_or_null(adapter, "memory_max_size")
        p[0].max_display_resolution = get_key_or_null(adapter, "max_display_resolution")
        p[0].max_camera_resolution = get_key_or_null(adapter, "max_camera_resolution")
        p[0].video_capture = get_key_or_null(adapter, "video_capture")
        p[0].video_playbacks = get_key_or_null(adapter, "video_playbacks")
        p[0].support_4g = get_key_or_null(adapter, "support_4g")
        p[0].support_5g = convert_yesno_to_bool(get_key_or_null(adapter, "support_5g"))
        p[0].download_max_speed = get_key_or_null(adapter, "download_max_speed")
        p[0].upload_max_speed = get_key_or_null(adapter, "upload_max_speed")
        p[0].wifi_version = get_key_or_null(adapter, "wifi_version")
        p[0].bluetooth_version = get_key_or_null(adapter, "bluetooth_version")
        p[0].announced = get_key_or_null(adapter, "announced")
        p[0].category = get_key_or_null(adapter, "category")
        p[0].source = get_key_or_null(adapter, "source")
        p[0].save()

def get_key_or_null(adapter, key):
    if key in adapter.keys():
        return adapter[key]
    return None

class ProcessorPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        for item_adapter in adapter.keys():
            adapter[item_adapter] = adapter[item_adapter][0]
            
        if adapter["type"] == "summary":
            insert_or_update_summary(adapter)
        else:
            insert_or_update_detail(adapter)
        return item
