import scrapy
from ..items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        items = QuoteItem()
        # acessa o titulo, autor e tags da div
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            text = quote.css('span.text::text').get()
            author = quote.css('.author::text').get()
            tags = quote.css('.tag::text').getall()

            items['quote'] = text
            items['author'] = author
            items['tags'] = tags

            yield items

        # faz scrape de todas as paginas do site
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            print(next_page)
            yield response.follow(next_page, callback=self.parse)
