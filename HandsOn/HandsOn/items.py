import scrapy

class PricetrackerItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()


class ArticlesItem(scrapy.Item):
    def __init__(self):
        super().__init__()
        self.fields['URL'] = scrapy.Field()
        self.fields['title'] = scrapy.Field()
        self.fields['meta_description'] = scrapy.Field()
        self.fields['body'] = scrapy.Field()
        self.fields['internal_links'] = scrapy.Field()