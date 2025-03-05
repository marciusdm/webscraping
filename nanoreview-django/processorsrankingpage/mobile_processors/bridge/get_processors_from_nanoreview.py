# Inicia o processo de web-scraping no site nanoreview

from scrapy.crawler import CrawlerProcess

from ..scrap_nanoreview.processorsranking.spiders.mobile_processors import  MobileProcessorsSpider

def start_crawler():
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
            "ITEM_PIPELINES": {
                "mobile_processors.bridge.processor_pipeline.ProcessorPipeline": 300,
            }
        }
    )
    process.crawl(MobileProcessorsSpider)
    print("starting crawler")
    process.start(install_signal_handlers=False)

