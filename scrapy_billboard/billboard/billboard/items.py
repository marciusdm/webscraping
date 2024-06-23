# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BillboardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sequential_no=scrapy.Field()
    artist = scrapy.Field()
    song = scrapy.Field()
    year = scrapy.Field()
    date = scrapy.Field()
