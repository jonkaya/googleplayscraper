
__author__ = 'can'


from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings

from scraper.googleplay.top_500_free_apps_spider import Top500FreeAppsSpider

class GooglePlayScraperRunner():


    def run(self):

        spider = Top500FreeAppsSpider()
        settings = get_project_settings()
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start()
        reactor.run()

    def task_id(self):
        return "HourlyGooglePlayScraper"




