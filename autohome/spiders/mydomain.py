# -*- coding: utf-8 -*-
import scrapy

class MydomainItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()


class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    allowed_domains = ["dmoz.com"]
    start_urls = (
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    
    )

    def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
