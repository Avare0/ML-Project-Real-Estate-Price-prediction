# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from cian.items import FlatItem
from constants import fields


class CianSpider(scrapy.Spider):
    name = 'cian_spider'
    allowed_domains = ['cian.ru']
    start_urls = [f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=1']
    i = 1

    def parse(self, response: HtmlResponse):
        links = response.css('.c6e8ba5398--header--1fV2A::attr(href)').extract()
        
        for link in links:
            yield response.follow(link, callback=self.parse_page)

        self.i += 1
        yield response.follow(f'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={self.i}&region=1', callback=self.parse)

    def parse_page(self, response: HtmlResponse):
        loader = ItemLoader(item=FlatItem(), response=response)

        # Общая информация
        loader.add_xpath('type', '//ul[@class=\'a10a3f92e9--list--2M4V-\']/li[1]/span[2]/text()')
        for item in response.xpath('//ul[@class=\'a10a3f92e9--list--2M4V-\']/li'):
            field_name = item.xpath('./span[1]/text()').extract_first()
            field_data = item.xpath('./span[2]/text()').extract_first()
            loader.add_value(fields[field_name], field_data)

        # Цена
        loader.add_css(fields['Цена'], 'span[itemprop="price"]::text')
        loader.add_css(fields['Цена за метр'], '.a10a3f92e9--price_per_meter--hKPtN::text')

        #Название и адрес
        loader.add_css('name', 'h1[data-name="OfferTitle"]::text')
        addr = response.xpath('//address/a/text()').extract()
        loader.add_value(fields['Адрес'], ','.join(addr))

        # Метро
        stations = response.xpath('//a[@class="a10a3f92e9--underground_link--AzxRC"]/text()').extract()
        time = response.xpath('//span[@class="a10a3f92e9--underground_time--1fKft"]/text()').extract()
        time = [i for i in time if i != ' ' and i != '⋅']
        fastest_station = self.parse_stations(stations, time)
        loader.add_value(fields['Метро'], fastest_station[0])
        loader.add_value(fields['Время до метро'], fastest_station[1])

        # Блок под фотками
        for item in response.xpath('//div[@class="a10a3f92e9--info--3XiXi"]'):
            field_name = item.xpath('./div[2]/text()').extract_first()
            field_data = item.xpath('./div[1]/text()').extract_first()
            if field_name == 'Этаж':
                f = field_data.split()
                loader.add_value(fields['Кол-во этажей'], f[2])
                field_data = f[0]
            loader.add_value(fields[field_name], field_data)

        loader.add_value('link', response.url)

        yield loader.load_item()


    def parse_stations(self, stations, times):
        for i in range(len(times)):
            times[i] = self.get_num_from_str(times[i])

        index = times.index(min(times))

        return stations[index], times[index]


    def get_num_from_str(self, str):
        word_list = str.split()
        num_list = [num for num in filter(lambda num: num.isnumeric(), word_list)]
        return int(''.join(num_list))
