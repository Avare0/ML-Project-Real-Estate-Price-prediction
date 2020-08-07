# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def delete_symbols(addr):
    return addr.replace(u'\xa0', u'')


class FlatItem(scrapy.Item): # Квартира
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    type = scrapy.Field(output_processor=TakeFirst())
    rooms_area = scrapy.Field(output_processor=TakeFirst())
    bathroom = scrapy.Field(output_processor=TakeFirst())
    ceiling_height = scrapy.Field(output_processor=TakeFirst())
    repair = scrapy.Field(output_processor=TakeFirst())
    balcony = scrapy.Field(output_processor=TakeFirst())
    view_from_windows = scrapy.Field(output_processor=TakeFirst())
    finish = scrapy.Field(output_processor=TakeFirst())
    layout = scrapy.Field()

    price = scrapy.Field(input_processor=MapCompose(delete_symbols),output_processor=TakeFirst())
    price_per_meter = scrapy.Field(input_processor=MapCompose(delete_symbols),output_processor=TakeFirst())

    address = scrapy.Field(output_processor=TakeFirst())
    station = scrapy.Field(output_processor=TakeFirst())
    time = scrapy.Field(output_processor=TakeFirst())

    square = scrapy.Field(input_processor=MapCompose(delete_symbols),output_processor=TakeFirst())
    living_space = scrapy.Field(input_processor=MapCompose(delete_symbols), output_processor=TakeFirst())
    kitchen = scrapy.Field(input_processor=MapCompose(delete_symbols),output_processor=TakeFirst())
    floor = scrapy.Field(output_processor=TakeFirst())
    max_floor = scrapy.Field(output_processor=TakeFirst())
    deadline = scrapy.Field(output_processor=TakeFirst())
    built = scrapy.Field(output_processor=TakeFirst())

    link = scrapy.Field(output_processor=TakeFirst())
