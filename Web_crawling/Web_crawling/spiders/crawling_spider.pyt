#Use scrapy as a bass class and rules of extraction 
from scrapy.spiders import CrawlSpider, Rule

#Extraction of links
from scrapy.linkextractors import LinkExtractor

#Custom spider class
class CrawlingSpider(CrawlSpider):
    name = "web-crawler"