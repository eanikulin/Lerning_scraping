import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quotes.items import QuotesItem


class QuotesDetailSpider(CrawlSpider):
    name = 'quotes_detail'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com']
    item = QuotesItem()

    rules = (
        # Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), callback='parse_main', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='quote']/span[@class='text']/following-sibling::span/a"), callback='parse_about', follow=True),
    )

    def parse_main(self, response):
        # item = self.item
        item = {}
        quotes = response.xpath("//div[@class='quote']")
        # for quote in quotes:
        #     yield {
        #         'quote_text': quote.xpath(".//span[@class='text']/text()").get()[1:-1],
        #         'quotes_tags': [tag.get() for tag in quote.xpath(".//a[@class='tag']/text()")],
        #     }

        for quote in quotes:
            item['quote_text'] = quote.xpath('./span[@class="text"]/text()').extract_first()[1:-1],
            item['quotes_tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            yield item


    def parse_about(self, response):
        item = self.item
        item['author_name'] = ''.join(response.xpath("//div[@class='author-details']/h3[@class='author-title']/text()").get()).strip(),
        item['author_born'] = response.xpath("//div[@class='author-details']/h3[@class='author-title']/following-sibling::p/span[@class='author-born-date']/text()").get()
        item['author_description'] = ''.join(response.xpath("//div[@class='author-details']/div[@class='author-description']/text()").get()).strip()
        item['source'] = 'quotes.toscrape.com'
        return item
