import scrapy
from ..items import ArticlesItem
from urllib.parse import urljoin,urlparse




class articles_spider(scrapy.Spider):
    name = 'articles_spider'
    start_urls = ['https://www.geeksforgeeks.org/python-programming-language-tutorial/',
                'https://www.geeksforgeeks.org/getting-started-with-python-programming/?ref=next_article']
    
    def parse(self,response):
        items = ArticlesItem()
        if response:
            items['URL'] = response.url
            items['title'] = response.css('div.article-title h1::text').get()
            items['meta_description'] = response.css('meta[name="description"]::attr(content)').get()
            items['body'] = response.css('div.text span::text').getall()
            # Extract internal links
            internal_links = response.css('a::attr(href)').getall()
            internal_links = [urljoin(response.url, link) for link in internal_links if self.is_internal_link(link)]
            items['internal_links'] = internal_links
            yield items
    
    def is_internal_link(self, link):
        # Parse the current domain
        current_domain = urlparse(self.start_urls[0]).netloc

        # Parse the link
        parsed_link = urlparse(link)

        # Check if the link is internal
        return (parsed_link.netloc == '' or parsed_link.netloc == current_domain)