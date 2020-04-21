# -*- coding: utf-8 -*-
import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles/']

    def parse(self, response):
        pass
