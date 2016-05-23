# -*- coding: utf-8 -*-
import scrapy
from autohome.items import AutohomeItem



class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    allowed_domains = ["dmoz.com"]
    start_urls = (
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    
    )

    def parse(self, response):
		for sel in response.xpath('//ul/li'):
			item = AutohomeItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item

		# filename = response.url.split("/")[-2] + '.html'
		# with open(filename, 'wb') as f:
			# f.write(response.body)
