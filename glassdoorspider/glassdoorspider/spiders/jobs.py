import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os
import datetime
import re

class jobspider(CrawlSpider):
    name = 'jobsearch'
    start_urls = ['https://www.glassdoor.com/job-listing/senior-data-scientist-farfetch-JV_IC1132348_KO0,21_KE22,30.htm?jl=2849832848&ctt=1535578607303']
   # ['https://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14.htm']



    def parse(self, response):
        print('##########################################################')
        try:
            job_description = response.xpath('//script[type="application/ld+json"]').extract()
            id = random.int(1000000000, 9999999999)
            filename = 'jobs_id_' + id + '.json'
            with open('../../../corpus/' + filename, 'w') as f:
                f.write(job_description)
        except:
            print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOps')
        





class Product(scrapy.Item):
    job_description = scrapy.Field
    last_updated = scrapy.Field(serializer=str)
