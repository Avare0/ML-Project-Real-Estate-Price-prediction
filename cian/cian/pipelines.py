# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class CianPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.cian

    def process_item(self, item, spider):
        coll = self.mongo_base['flats']
        coll.insert_one(item)
        return item
