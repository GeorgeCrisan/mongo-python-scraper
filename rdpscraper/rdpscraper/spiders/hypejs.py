import scrapy


class HypejsSpider(scrapy.Spider):
    name = "hypejs"
    # To limit the spider to specific domain(s)
    allowed_domains = ["hypejs.com"]
    start_urls = ["http://hypejs.com/"]

    def parse(self, response):
        # mainArticle = response.css("h3.leading-tight::text")
        articles = response.css("h3.leading-snug")
        # allArticles = [*mainArticle, *articles]
        url = "http://hypejs.com"

        for article in articles:
            yield {
                "title": article.css("a::text").get(),
                "path": url + article.css("a").attrib["href"]
            }
