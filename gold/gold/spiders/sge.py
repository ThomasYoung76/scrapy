# -*- coding: utf-8 -*-
import scrapy
from gold.items import *
import re

class SgeSpider(scrapy.Spider):
    name = 'sge'
    allowed_domains = ['http://www.sge.com.cn']
    start_urls = ['http://www.sge.com.cn']

    def start_requests(self):
        url = 'http://www.sge.com.cn/sjzx/mrhqsj'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        # item = GoldItem()
        data = response.css('a.title.fs14.color333.clear::attr(href)').extract()
        page_num = response.css('div.btn.border_ea.noLeft_border::attr(onclick)').extract_first()

        for ele in data:
            # /sjzx/mrhqsj/5142535?top=789398439266459648
            day_url = re.findall(r'\/\d*\?\w*\=\d*', ele)[0]
            url = response.urljoin(day_url)
            print(url)
        yield scrapy.Request(url, callback=self.parse)

    # def day_parse(self, response):
    #     print('aaa')
    #     print(response.xpath("//td[contains(., 'Au99.99']").extract())
    #     next_page_url = self.start_urls[0] + '?p=' + re.findall("\'(\d)\'", page_num)[0]
    #     yield scrapy.Request(next_page_url, callback=self.parse)
