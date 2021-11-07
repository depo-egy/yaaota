# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item , Field


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # sku = scrapy.Field()
    URL = scrapy.Field()
    TITLE = scrapy.Field()
    MAIN_CATEGORY= scrapy.Field()
    
