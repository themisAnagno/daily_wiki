# -*- coding: utf-8 -*-
import scrapy
import random

from daily_wiki.items import DailyWikiItem


class ArticlesSpider(scrapy.Spider):
    name = "articles"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Wikipedia:Featured_articles"]

    # Enable Feed storage
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "file:///tmp/results.json"}

    def parse(self, response):

        host = response.url.split("/wiki")[0]

        content_list = response.css(".hlist > *")
        looking_for_header = True
        category = None
        for element in content_list:
            if looking_for_header and element.css("h3"):
                # Get the category of the article by the header
                looking_for_header = False
                category = element.css("span::text").get()
            elif not looking_for_header and element.css("ul"):
                # Get the article title
                # Get the list of the articles
                article_list = element.css("li")
                # Get a random article
                article_index = random.randrange(len(article_list) - 1)
                title = article_list[article_index].css("a::attr(title)").get()
                link = host + article_list[article_index].css("a::attr(href)").get()
                yield DailyWikiItem(category=category, title=title, link=link)
                category = None
                looking_for_header = True
            else:
                continue
