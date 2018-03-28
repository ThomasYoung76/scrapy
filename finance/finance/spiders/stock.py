import scrapy
from finance.items import *
import re

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://quote.eastmoney.com/stocklist.html#sh']

    def parse(self, response):
        item = FinanceItem()
        sh = response.xpath('//div[@class="qox"]/div[@class="quotebody"]/div/ul')[0].extract()

        for ele in re.findall(r'<li>.*?<a.*?target=.*?>(.*?)</a>', sh):
            item["stock_name"] = ele.split("(")[0]
            item["stock_code"] = ("sh" + ele.split("(")[1][:-1])
            yield item

        sz = response.xpath('//div[@class="qox"]/div[@class="quotebody"]/div/ul')[1].extract()
        for ele in re.findall(r'<li>.*?<a.*?target=.*?>(.*?)</a>', sz):
            item["stock_name"] = ele.split("(")[0]
            item["stock_code"] ='sz' + ele.split("(")[1][:-1]
            yield item
