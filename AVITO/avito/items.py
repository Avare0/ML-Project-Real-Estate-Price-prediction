# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def delete_symbols(addr):
    return addr.replace(u'\xa0', u'')

def delete_meters(s):
    return s.replace('м', '').replace(',', '.').replace('²', '').replace(' ', '').replace('₽', '').replace('/', '')

def take_last_4(s):
    return s[-4:]

def takesecond(a):
    return a[1]

class FlatItem(scrapy.Item): # Квартира
    _id = scrapy.Field()
    source = scrapy.Field(output_processor = TakeFirst())


    name = scrapy.Field(output_processor = TakeFirst())
    type = scrapy.Field(output_processor = TakeFirst())
    rooms_area = scrapy.Field()
    bathroom = scrapy.Field()
    ceiling_height = scrapy.Field()
    repair = scrapy.Field()
    balcony = scrapy.Field()
    view_from_windows = scrapy.Field()
    finish = scrapy.Field()
    layout = scrapy.Field()

    price = scrapy.Field(output_processor = TakeFirst(), input_processor = MapCompose(delete_symbols, delete_meters, float))
    price_per_meter = scrapy.Field()

    address = scrapy.Field(output_processor = TakeFirst())
    station = scrapy.Field(output_processor = TakeFirst())
    time = scrapy.Field(output_processor = TakeFirst())

    square = scrapy.Field(output_processor = TakeFirst(), input_processor = MapCompose(str,delete_symbols, delete_meters, float))
    living_space = scrapy.Field()
    kitchen = scrapy.Field()
    floor = scrapy.Field(output_processor = TakeFirst())
    max_floor = scrapy.Field(output_processor = TakeFirst())
    deadline = scrapy.Field()
    built = scrapy.Field()

    link = scrapy.Field(output_processor = TakeFirst())
    trash = scrapy.Field()