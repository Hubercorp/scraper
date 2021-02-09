

import scrapy

class Lva_spider(scrapy.Spider):
    name = "lva"

    def start_requests(self):
        urls = [
            'https://www.lva-auto.fr/cote.php?src=menu',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')