import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = "special_offers"
    allowed_domains = ["web.archive.org"]
    start_urls = [
        "https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html"
    ]

    def parse(self, response):
        for product in response.xpath(
            "//ul[contains(@class, 'productlisting-ul')]/div/li"
        ):
            yield {
                "url": response.urljoin(
                    product.xpath(".//a[contains(@class, 'p_box_title')]/@href").get()
                ),
                "title": response.xpath(
                    ".//a[contains(@class, 'p_box_title')]/text()"
                ).get(),
                "normal_price": response.xpath(
                    ".//div[contains(@class, 'p_box_price')]/span[2]/text()"
                ).get(),
                "sale_price": response.xpath(
                    ".//div[contains(@class, 'p_box_price')]/span[1]/text()"
                ).get(),
            }

        next_page = response.xpath('.//a[contains(@class, "nextPage")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
