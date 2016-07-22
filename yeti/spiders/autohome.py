# -*- coding: utf-8 -*-
import scrapy
# from items import AutohomeItem
from yeti.items import AutohomeItem
# from autohome.items import AutohomeItem
# from tutorial.items import DmozItem


class AutohomeSpider(scrapy.Spider):
    name = "autohome"
    allowed_domains = ["autohome.com.cn"]
    start_urls = (
		"http://club.autohome.com.cn/bbs/forum-c-3013-1.html",
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    
    )

# <a class="a_topic" target="_blank" href="/bbs/thread-c-3013-54488086-1.html">
# Yeti获2015中国小型SUV金方向盘奖            </a>
    def parse(self, response):
		# for sel in response.xpath('//ul/li'):
		for sel in response.selector.xpath('//dt/a'):
		# for sel in response.selector.xpath('//dt/a').extract():
		# for sel in response.selector.xpath('//dt/a/text()').extract():
#			print sel
			item = AutohomeItem()
			item['title'] = sel.xpath('//a/text()').extract()
			print item['title']
			item['link'] = sel.xpath('//a/@href').extract()
			print item['link']
#			item['desc'] = sel.xpath('text()').extract()
			yield item

		# filename = response.url.split("/")[-2] + '.html'
		# with open(filename, 'wb') as f:
			# f.write(response.body)
