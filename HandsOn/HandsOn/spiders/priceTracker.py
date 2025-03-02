import scrapy
from ..items import PricetrackerItem

class PriceTracker(scrapy.Spider):
    name = 'priceTracker'
    start_urls = ['https://hammeronline.in/collections/truly-wireless-earbuds']

    def parse(self,response):
        item = PricetrackerItem()
        for product in response.css('div.grid-product__content'):
            item['title'] = product.css('div.grid-product__title.grid-product__title--body::text').get().strip()
            item['price'] = product.css('div.grid-product__price::text').get().strip()
            item['description'] = product.css('div.collection_tags::text').get().strip()
            yield item