import scrapy
from ..items import DreamItem


class ViseroSpider(scrapy.Spider):
    name = "viseRo"
    allowed_domains = ["vise.ro"]
    letter = 'a'
    start_urls = ["http://www.vise.ro/dictionar?letter=" + letter]

    propertyFN = "vise" + letter.upper() + ".json"

    custom_settings = {
        "FEEDS": {
            propertyFN: {"format": "json"}
        }
    }

    def parse(self, response):

        items = response.css("a.list-group-item")

        for item in items:
            item_data = DreamItem()

            item_data['title'] = item.css("b::text").get()
            item_data['content'] = item.css(
                "p.list-group-item-text::text").get()

            yield item_data

        next_page = response.css("ul.pager").css('a[rel="next"]')

        if next_page is not None:
            next_page_url = "http://www.vise.ro" + next_page.attrib["href"]
            yield response.follow(next_page_url, callback=self.parse)
