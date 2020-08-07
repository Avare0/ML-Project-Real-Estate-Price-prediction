# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from cian.items import CianItem


class CianSpider(scrapy.Spider):
    name = 'cian_spider'
    allowed_domains = ['cian.ru']
    start_urls = [f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=1']
    i = 1

    def parse(self, response: HtmlResponse):

        links = response.css('.c6e8ba5398--header--1fV2A::attr(href)').extract()
        print(len(links))
        for link in links:
            yield response.follow(link, callback=self.parse_page)

        self.i += 1
        yield response.follow(f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={self.i}&region=1', callback=self.parse)

    def parse_page(self, response: HtmlResponse):
        loader = ItemLoader(item=CianItem(), response=response)
        loader.add_css('name', 'h1[data-name="OfferTitle"]::text')
        yield loader.load_item()
