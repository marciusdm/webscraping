# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CounselinginfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    state_region = scrapy.Field()
    city = scrapy.Field()
    school = scrapy.Field()
    first_name = scrapy.Field()
    middle_name = scrapy.Field()
    last_name = scrapy.Field()
    job_title = scrapy.Field()
    mail=scrapy.Field()
    phone=scrapy.Field()
