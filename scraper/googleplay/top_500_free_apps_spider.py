from datetime import datetime
from mongo import get_connection

__author__ = 'can'

import time
import re
from scrapy import Spider, Field, Item, Request


db = get_connection()

class FreeAppItem(Item):
    title = Field()
    link = Field()
    stars = Field()
    review_count = Field()
    release_date = Field()



class Top500FreeAppsSpider(Spider):

    name, start_urls = 'Top500FreeAppsSpider', \
                       ['https://play.google.com/store/apps/collection/topselling_free?hl=en&start=0&num=100',
                        'https://play.google.com/store/apps/collection/topselling_free?hl=en&start=100&num=100',
                        'https://play.google.com/store/apps/collection/topselling_free?hl=en&start=200&num=100',
                        'https://play.google.com/store/apps/collection/topselling_free?hl=en&start=300&num=100',
                        'https://play.google.com/store/apps/collection/topselling_free?hl=en&start=400&num=100',
                        ]

    base_url = 'https://play.google.com'

    def parse(self, response):

        free_app_list = [FreeAppItem(title=e.xpath("text()").extract(), link=e.xpath("@href").extract()) for e in response.css("h2 a")]

        for free_app in free_app_list:
            request = Request(self.base_url + free_app['link'][0], self.parse_detail)
            request.meta['item'] = free_app
            yield request

    def parse_detail(self, response):

        item = response.meta['item']

        item['review_count'] = response.css('.reviews-num').xpath("text()").extract()
        item['stars'] = response.css('.score').xpath("text()").extract()
        item['release_date'] = response.css('.document-subtitle').xpath("text()").extract()


        #Collect information from parsed fields and update database

        id, title = re.split(r'\.\s+', item['title'][0])

        # in format "- January 8, 2015"
        time_struct = time.strptime(item['release_date'][2], "- %B %d, %Y")

        release_date = datetime(year=time_struct.tm_year,
                                       month=time_struct.tm_mon,
                                       day=time_struct.tm_mday)

        db.freeapps.update(
            { 'id': int(id) },
            {
                "$set": {
                    'id': int(id),
                    'title': title,
                    'review_count': int(item['review_count'][0].replace(',', '')),
                    'star_count': float(item['stars'][0]),
                    'release_date': release_date,
                    'last_update': datetime.now()
                }
            },
            upsert=True
        )

        return item








