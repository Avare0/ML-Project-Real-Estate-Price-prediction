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
    type = scrapy.Field()
    rooms_area = scrapy.Field()
    bathroom = scrapy.Field()
    ceiling_height = scrapy.Field()
    repair = scrapy.Field()
    balcony = scrapy.Field()
    view_from_windows = scrapy.Field()
    finish = scrapy.Field()
    layout = scrapy.Field()
