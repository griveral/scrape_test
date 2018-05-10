import scrapy

from provinces.items import *
from scrapy import log

class QuotesSpider(scrapy.Spider):
    name = "provinces"

    def start_requests(self):
        urls = [
            'http://nap.psa.gov.ph/activestats/psgc/listprov.asp',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # filename = 'provinces_output.html'
        # with open(filename, 'wb') as f:
            # f.write(response.body)
        # self.log('Saved file %s' % filename)

        log.msg('parse(%s)' % response.url, level = log.DEBUG)
        # provinces =
        provinces = response.xpath("//p[contains(@class, 'dataCellp')]")
        for province in provinces:
            item = ProvinceItem()
            item['name'] = province.xpath('a/text()').extract()
            item['code'] = str(province.xpath('a/@href').extract())[43:52]
            yield item
