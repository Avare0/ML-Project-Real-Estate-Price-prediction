# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

class FlatItem(scrapy.Item): # Квартира
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())

