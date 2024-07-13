# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from itemloaders.processors import MapCompose
from w3lib.html import remove_tags


def strip_quotes(value):
     return (value.replace("\"", "")
             .replace("\n", "")
             .replace("†", "")
             .replace("&amp;", "&")
             .strip())

def strip_reference(value):
    pattern = r"\[[^\]]+?\]"
    return re.sub(pattern,"",value)

class BillboardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sequential_no=scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_quotes, strip_reference)
    )
    artist = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_quotes, strip_reference)
    )
    song = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_quotes, strip_reference)
    )
    date = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_quotes, strip_reference)
    )
    year = scrapy.Field()
