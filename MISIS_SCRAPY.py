class PycoderSpider(scrapy.Spider):
    name = "pycoder"
    start_urls = ['https://misis.ru/university/struktura-universiteta/instituty/',]
    visited_urls = []

def parse(self, response):
    if response.url not in self.visited_urls:
        self.visited_urls.append(response.url)
        for post_link in response.xpath('//div[@class="institute-item-head"]/h3/a/@href').extract():
            url = urljoin(response.url, post_link)
            yield response.follow(url, callback=self.parse_post)



def parse_post(self, response):
    item = PycoderItem()
    title = response.xpath('//div[contains(@class, "col-xs-4")]/h1/text()').extract()
    item['title'] = title

    yield item
