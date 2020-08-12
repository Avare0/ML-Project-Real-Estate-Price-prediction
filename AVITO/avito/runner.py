from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

import avito.settings
from avito.spiders.avito_spider import AvitoSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(avito.settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(AvitoSpider)

    process.start()