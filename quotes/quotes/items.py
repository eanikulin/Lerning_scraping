# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    quote_text = scrapy.Field()
    quotes_tags = scrapy.Field()
    author_name = scrapy.Field()
    author_born = scrapy.Field()
    author_description = scrapy.Field()
    source = scrapy.Field()
