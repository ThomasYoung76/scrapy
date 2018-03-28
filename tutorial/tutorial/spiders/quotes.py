# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import *

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = TutorialItem()
            item['text'] = quote.css(".text::text").extract_first()
            item['tags'] = quote.css(".tag::text").extract()
            item['author'] = quote.css(".author::text").extract_first()
            yield item
        next_page_url = response.css('li.next a::attr(href)').extract_first()
        url = response.urljoin(next_page_url)
        yield scrapy.Request(url, callback=self.parse)
