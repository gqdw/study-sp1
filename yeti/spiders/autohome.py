# -*- coding: utf-8 -*-
import scrapy
# from items import AutohomeItem
from yeti.items import AutohomeItem
import datetime
# from autohome.items import AutohomeItem
# from tutorial.items import DmozItem


class AutohomeSpider(scrapy.Spider):
    name = "autohome"
    allowed_domains = ["autohome.com.cn"]
    start_urls = (
		"http://club.autohome.com.cn/bbs/forum-c-3013-1.html",
		"http://club.autohome.com.cn/bbs/forum-c-3013-2.html",
		"http://club.autohome.com.cn/bbs/forum-c-3013-3.html",
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    
    )
# <a class="a_topic" target="_blank" href="/bbs/thread-c-3013-54488086-1.html">
# Yeti获2015中国小型SUV金方向盘奖            </a>
#	def parse(self, response):
#		print response.selector.xpath('//dt/a').extract()
    def parse(self, response):
		today = datetime.datetime.today()
		filename = 'yeti-' + today.strftime('%Y%m%d-%H%S') + '.log'
		website = 'http://club.autohome.com.cn'
		f = open(filename, 'a')
		for sel in response.selector.xpath('//dt/a'):
#			print sel.xpath('text()').extract()[0]
			f.write(sel.xpath('text()').extract()[0].encode('utf-8'))
			# type =  unicode
#			print sel.xpath('@href').extract()[0]
			#print type(sel.xpath('@href').extract()[0])
			
			f.write(website + sel.xpath('@href').extract()[0].encode('utf-8'))
		f.close()
