# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.coom']
    start_urls = ['http://example.coom/']

    def parse(self, response):
        pass
