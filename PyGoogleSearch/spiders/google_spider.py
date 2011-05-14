from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import time

from PyGoogleSearch.items import PyGSItem
import sys

class PyGSSpider(CrawlSpider):
    '''
    docstring for PyGSSpider
    '''
    name = 'google.com'
    allowed_domains = ['google.com']
    #start_urls = [
    #    'http://www.google.fr/search?sclient=psy&hl=fr&source=hp&q=sexe&btnG=Rechercher'
    #    ]
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths='//a[@id="pnnext"]',
        ), 
        callback='parse_item',
        follow=True),
        )

    def parse_item(self, response):
        time.sleep(3)
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="ires"]/ol/li')
        items = []
        for site in sites:
            item = PyGSItem()
            
            item['title'] = site.select('h3[@class="r"]/a/text() | \
            h3[@class="r"]/a/em/text()').extract()
            item['desc'] = site.select('div/text()').extract()
            item['link'] = site.select('h3[@class="r"]/a/@href').extract()
            items.append(item)
        return items

        
