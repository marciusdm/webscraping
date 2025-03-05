# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from itemloaders.processors import MapCompose
from w3lib.html import remove_tags
from .Helper.ItemHelper import strip_non_numeric, strip_non_alpha_numeric, replace_br_char
from .Helper.DateHelper import convert_english_date



class ProcessorsrankingItemDetail(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        type = scrapy.Field()
        manufacturer_model = scrapy.Field()
        nano_review_score = scrapy.Field()
        antutu_score = scrapy.Field()
        geek_bench_score_single = scrapy.Field()
        geek_bench_score_multi = scrapy.Field()
        geek_bench_score_gpu = scrapy.Field()
        score_3d_mark = scrapy.Field()
        fps_3d_mark = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        cpu_frequency = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        architecture = scrapy.Field()
        cores = scrapy.Field()
        l2_cache = scrapy.Field()
        l3_cache = scrapy.Field()
        process_nanometers = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        tdp_watt = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        gpu_name = scrapy.Field()
        gpu_frequency = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        gpu_flops_gigaflops = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        gpu_pipelines = scrapy.Field()
        memory_type = scrapy.Field()
        memory_frequency = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        memory_max_size = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        max_display_resolution = scrapy.Field()
        max_camera_resolution = scrapy.Field()
        video_capture = scrapy.Field()
        video_playbacks = scrapy.Field()
        support_4g = scrapy.Field()
        support_5g = scrapy.Field()
        download_max_speed = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        upload_max_speed = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
        wifi_version = scrapy.Field()
        bluetooth_version = scrapy.Field()
        announced = scrapy.Field(input_processor=MapCompose(convert_english_date))
        category = scrapy.Field()
        source = scrapy.Field()

class ProcessorsrankingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    model = scrapy.Field()
    manufacturer = scrapy.Field()
    nano_review_score = scrapy.Field()
    nano_review_label = scrapy.Field()
    antutu_score = scrapy.Field()
    input_processor = MapCompose(strip_non_numeric)
    geekbench_score = scrapy.Field()
    cores = scrapy.Field(input_processor=MapCompose(remove_tags, strip_non_alpha_numeric))
    clock = scrapy.Field(input_processor=MapCompose(strip_non_numeric))
    gpu = scrapy.Field()
