from scrapy.item import Item, Field


class DreamItem(Item):
    title = Field()
    content = Field()
