import scrapy
from scrapy_djangoitem import DjangoItem
from quotes.models import Quote


class QuoteItem(DjangoItem):
    """Define Scrapy Items utilizando Django models"""
    django_model = Quote
    tags = scrapy.Field()
