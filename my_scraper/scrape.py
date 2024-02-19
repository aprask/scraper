import scrapy
from my_scraper.models import ScrapedItem
class Spider(scrapy.Spider):
    name = 'spider'

    def start_requests(self):
        urls = ['https://www']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        items = []
        prices = response.css('.price::text').extract()
        links = response.css('a::attr(href)').extract()
        names = response.css('.name::text').extract()
        descriptions = response.css('.description::text').extract()

        for price, link, name, description in zip(prices, links, names, descriptions):
            item = ScrapedItem()
            item.url = response.url
            item.price = price
            item.item_link = link
            item.name = name
            item.description = description
            items.append(item)

        for item in items:
            item.save()

        return items