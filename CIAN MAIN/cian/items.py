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

def get_sum_num_arr_from_str(s):
    word_list = s.split()
    num_list = [int(num) for num in filter(lambda num: num.isnumeric() , word_list)]
    return int(sum(num_list))

def get_sum_num_arr_from_str(s):
    word_list = s.split()
    num_list = [int(num) for num in filter(lambda num: num.isnumeric() , word_list)]
    return int(sum(num_list))

def parse_rooms_area(s):
    s = s.replace('м²', '').replace('-',' ').replace('+',' ').replace(',', '.')

    word_list = s.split()
    num_list = [float(num) for num in word_list]
    return float(sum(num_list))

class FlatItem(scrapy.Item): # Квартира
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    type = scrapy.Field(output_processor=TakeFirst())
    rooms_area = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(parse_rooms_area))
    bathroom = scrapy.Field(output_processor=TakeFirst(), input_processor = MapCompose(get_sum_num_arr_from_str))
    ceiling_height = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(delete_meters, float))
    repair = scrapy.Field(output_processor=TakeFirst())
    balcony = scrapy.Field(output_processor=TakeFirst(), input_processor = MapCompose(get_sum_num_arr_from_str, int))
    view_from_windows = scrapy.Field(output_processor=TakeFirst())
    finish = scrapy.Field(output_processor=TakeFirst())
    layout = scrapy.Field(output_processor=TakeFirst())

    price = scrapy.Field(input_processor=MapCompose(delete_symbols, delete_meters, float),output_processor=TakeFirst())
    price_per_meter = scrapy.Field(input_processor=MapCompose(delete_symbols, delete_meters, int),output_processor=TakeFirst())

    address = scrapy.Field(output_processor=TakeFirst())
    station = scrapy.Field(output_processor=TakeFirst())
    time = scrapy.Field(output_processor=TakeFirst())

    square = scrapy.Field(input_processor=MapCompose(delete_symbols, delete_meters, float),output_processor=TakeFirst())
    living_space = scrapy.Field(input_processor=MapCompose(delete_symbols, delete_meters, float), output_processor=TakeFirst())
    kitchen = scrapy.Field(input_processor=MapCompose(delete_symbols, delete_meters, float),output_processor=TakeFirst())
    floor = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(int))
    max_floor = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(int))
    deadline = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(take_last_4, int))
    built = scrapy.Field(output_processor=TakeFirst())

    link = scrapy.Field(output_processor=TakeFirst())
