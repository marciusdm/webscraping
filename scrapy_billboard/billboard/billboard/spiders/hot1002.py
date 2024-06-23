import scrapy


class Hot1002Spider(scrapy.Spider):
    name = "hot1002"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1959"]

    def parse(self, response):
        pass
