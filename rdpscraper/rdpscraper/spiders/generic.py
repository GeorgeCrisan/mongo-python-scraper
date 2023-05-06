import scrapy
from ..items import DreamItem
from scrapy_playwright.page import PageMethod


class ViseroSpider(scrapy.Spider):
    name = "generic"
    allowed_domains = ["vise.ro"]
    letter = 'a'
    # start_urls = ["http://www.vise.ro/dictionar?letter=" + letter]

    def start_requests(self):
        url = "http://www.vise.ro/dictionar?letter=" + self.letter

        yield scrapy.Request(url, meta=dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods=[PageMethod(
                'wait_for_selector', 'a.list-group-item')],
            errback=self.errback,
        ))

    propertyFN = "vise" + letter.upper() + ".json"

    # custom_settings = {
    #     "FEEDS": {
    #         propertyFN: {"format": "json"}
    #     }
    # }

    async def parse(self, response):

        page = response.meta["playwright_page"]
        await page.close()

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
            yield scrapy.Request(next_page_url, meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[PageMethod(
                    'wait_for_selector', 'a.list-group-item')],
                errback=self.errback,
            ))

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
