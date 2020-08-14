from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

import settings
from cian.spiders.cian_spider import CianSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(CianSpider)

    process.start()