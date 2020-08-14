# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from avito.items import FlatItem
from avito.constants import fields


class AvitoSpider(scrapy.Spider):
    name = 'avito_spider'
    allowed_domains = ['avito.ru']
    i = 1
    start_urls = [f'https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=2&p={i}']


    def parse(self, response: HtmlResponse):
        links = response.css('a[itemprop="url"]::attr(href)').extract()
        if response.status == 302:
            print(self.i, '\nREDIRECTED.STOPPING PIPELINE')
            return None
        
        for link in links:
            yield response.follow(link, callback=self.parse_page)

        self.i += 1

        if self.i == 101:
            return None

        yield response.follow(f'https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=2&p={self.i}',meta={'dont_redirect': True,"handle_httpstatus_list": [302]}, callback=self.parse)

    def parse_page(self, response: HtmlResponse):
        loader = ItemLoader(item=FlatItem(), response=response)

        # Общая информация
        for item in response.xpath('//ul[@class="item-params-list"]/li'):
            field_name = item.xpath('./span[@class="item-params-label"]').extract_first()
            field_data = item.xpath('./text()').extract()
            del field_data[0]
            if 'Этаж' in field_name:
                f = field_data[0].split()
                print(f)
                loader.add_value(fields['Кол-во этажей'], f[2])
                field_data = f[0]

            if field_name.split(':')[0].split('>')[1] in fields.keys():
                loader.add_value(fields[field_name.split(':')[0].split('>')[1]], field_data)

        # Цена
        loader.add_css(fields['Цена'], 'span[itemprop="price"]::text')

        #Название и адрес
        loader.add_css('name', '.title-info-title-text::text')
        addr = response.xpath('//span[@class="item-address__string"]/text()').extract()
        addr[0] = addr[0][2:-2]
        loader.add_value(fields['Адрес'], addr)

        # Метро
        stations = response.xpath('//span[@class="item-address-georeferences-item__content"]/text()').extract()
        time = response.xpath('//span[@class="item-address-georeferences-item__after"]/text()').extract()
        time = [i.replace(' ','').replace(',', '.') for i in time]
        print(time, stations)

        fastest_station = self.parse_stations(stations, time)
        loader.add_value(fields['Метро'], fastest_station[0])
        loader.add_value(fields['Время до метро'], fastest_station[1])


        loader.add_value('link', response.url)
        loader.add_value('source', 'Avito')

        yield loader.load_item()


    def parse_stations(self, stations, times):

        if stations == [] and times == []:
                return None, None

        for i in range(len(times)):
            times[i] = self.get_num_from_str(times[i])

        index = times.index(min(times))

        return stations[index], times[index]


    def get_num_from_str(self, s):
        flag = 0
        if 'км' in s:
            flag = 1
        word_list = s.split()
        if flag:
            return round(float(word_list[0]) / 5 * 60, 2)
        return round(float(word_list[0]) / 1000 / 5 * 60, 2)

