from scrapy.crawler import CrawlerProcess

from billboard.spiders.hot100 import Hot100Spider


def start_crawler():
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
            "ITEM_PIPELINES" : {
                "billboard.pipelines.BillboardPipeline": 300,
            }
        }
    )
    process.crawl(Hot100Spider)
    process.start()
