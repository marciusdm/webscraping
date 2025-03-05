import scrapy
from time import sleep
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Join

from ..items import ProcessorsrankingItem
from ..items import ProcessorsrankingItemDetail

#from import ProcessorsrankingItem, ProcessorsrankingItemDetail

class MobileProcessorsSpider(scrapy.Spider):
    name = "mobile_processors"
    allowed_domains = ["nanoreview.net"]
    start_urls = ["https://nanoreview.net/en/soc-list/rating"]
    sequential = 0

    def parse(self, response):
        #TODO: remover o "[0:4]" Após teste
        processors = response.xpath("//table[1]/tbody/tr")
        for processor in processors[4:]:
                loader = ItemLoader(item=ProcessorsrankingItem(), selector=processor)
                loader.add_value("type", "summary")
                loader.add_xpath("model", "td[2]/div/a/text()", TakeFirst())
                loader.add_xpath("manufacturer", "td[2]/span/text()", TakeFirst())
                loader.add_xpath("nano_review_score", "td[3]/div/text()", TakeFirst())
                loader.add_xpath("nano_review_label", "td[3]/span/text()", TakeFirst())
                loader.add_xpath("antutu_score", "td[4]/div/div/text()", TakeFirst())
                loader.add_xpath("geekbench_score", "td[5]/div/div/text()", TakeFirst())
                loader.add_xpath("cores", "td[6]", TakeFirst())
                loader.add_xpath("clock", "td[7]/text()", TakeFirst())
                loader.add_xpath("gpu", "td[8]/div/text()", TakeFirst())
                yield loader.load_item()

                detail_url = processor.xpath("td[2]/div/a/@href").get()
                yield scrapy.Request(response.urljoin(detail_url), callback=self.parse_details)

    def parse_details(self, response, **kwargs):
        print("Entering details")
        if self.sequential > 0 and self.sequential % 10 == 0:
                print("Pausing for 10 seconds")
                sleep(10)
        detail_section = response.css("#the-app")
        loader = ItemLoader(item=ProcessorsrankingItemDetail(), selector=detail_section)
        loader.add_value("type", "detail")
        loader.add_value("source", response.url)
        loader.add_css("manufacturer_model", "h1::text")
        loader.add_css("nano_review_score", "div.card.pb span.score-bar-result-square-dark::text")
        loader.add_css("antutu_score", "div:nth-child(4) span.score-bar-result-number::text")
        loader.add_xpath("geek_bench_score_single",
                       "//div[contains(text(),'Single-Core Score')]/following-sibling::div[@class='score-bar-result']//span/text()")
        loader.add_xpath("geek_bench_score_gpu",
                       "//div[contains(text(),'Compute Score (GPU)')]/following-sibling::div[@class='score-bar-result']//span/text()")
        loader.add_xpath("geek_bench_score_multi",
                         "//div[contains(text(),'Multi-Core Score')]/following-sibling::div[@class='score-bar-result']//span/text()")
        loader.add_xpath("score_3d_mark",
                         "//h3[text()='3DMark']/ancestor::div[@class='card']//td[text()='Score']/following-sibling::td/text()")
        loader.add_xpath("fps_3d_mark",
                         "//h3[text()='3DMark']/ancestor::div[@class='card']//td[text()='Graphics test']/following-sibling::td/text()")
        loader.add_xpath("architecture",
                         "//h3[text()='CPU']/ancestor::div[@class='card']//td[text()='Architecture']/following-sibling::td/text()",
                         Join(separator=", "))
        loader.add_xpath("cores", "//td[text()='Cores']/following-sibling::td/text()")
        loader.add_xpath("cpu_frequency",
                         "//h3[text()='CPU']/ancestor::div[@class='card']//td[text()='Frequency']/following-sibling::td/text()")
        loader.add_xpath("l2_cache", "//td[text()='L2 cache']/following-sibling::td/text()")
        loader.add_xpath("l3_cache", "//td[text()='L3 cache']/following-sibling::td/text()")
        loader.add_xpath("process_nanometers", "//td[text()='Process']/following-sibling::td/text()")
        loader.add_xpath("tdp_watt", "//td[text()='TDP (Sustained Power Limit)']/following-sibling::td/text()")
        loader.add_xpath("gpu_name", "//td[text()='GPU name']/following-sibling::td/text()")
        loader.add_xpath("gpu_frequency",
                         "//h3[text()='Graphics']/ancestor::div[@class='card']//td[text()='GPU frequency']/following-sibling::td/text()")
        loader.add_xpath("gpu_pipelines",
                         "//h3[text()='Graphics']/ancestor::div[@class='card']//td[text()='Pipelines']/following-sibling::td/text()")
        loader.add_xpath("gpu_flops_gigaflops", "//td[text()='FLOPS']/following-sibling::td/text()")
        loader.add_xpath("memory_type", "//td[text()='Memory type']/following-sibling::td/text()")
        loader.add_xpath("memory_frequency", "//td[text()='Memory frequency']/following-sibling::td/text()")
        loader.add_xpath("memory_max_size", "//td[text()='Max size']/following-sibling::td/text()")
        loader.add_xpath("max_display_resolution",
                         "//td[text()='Max display resolution']/following-sibling::td/text()")
        loader.add_xpath("max_camera_resolution",
                         "//td[text()='Max camera resolution']/following-sibling::td/text()")
        loader.add_xpath("video_capture", "//td[text()='Video capture']/following-sibling::td/text()")
        loader.add_xpath("video_playbacks", "//td[text()='Video playback']/following-sibling::td/text()")
        loader.add_xpath("support_4g", "//td[text()='4G support']/following-sibling::td/text()")
        loader.add_xpath("support_5g", "//td[text()='5G support']/following-sibling::td/text()")
        loader.add_xpath("download_max_speed", "//td[text()='Download speed']/following-sibling::td/text()")
        loader.add_xpath("upload_max_speed", "//td[text()='Upload speed']/following-sibling::td/text()")
        loader.add_xpath("wifi_version", "//td[text()='Wi-Fi']/following-sibling::td/text()")
        loader.add_xpath("bluetooth_version", "//td[text()='Bluetooth']/following-sibling::td/text()")
        loader.add_xpath("announced", "//td[text()='Announced']/following-sibling::td/text()")
        loader.add_xpath("category", "//td[text()='Class']/following-sibling::td/text()")
        self.sequential += 1
        return loader.load_item()
