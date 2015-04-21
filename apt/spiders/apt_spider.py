import scrapy

from apt.items import AptItem

class AptSpider(scrapy.Spider):
	name = "apt"
	allowed_domains = ["chicago.craigslist.org"]
	start_urls = [
			"https://chicago.craigslist.org/search/apa"
	]

	def parse(self,response):
		for listing in response.xpath('//span[@class="pl"]'):
			item = AptItem()
			item['title'] = listing.xpath('a/text()').extract()
			item['link'] = listing.xpath('a/@href').extract()
			item['price'] = listing.xpath('..//span[@class="l2"]/span[@class="price"]/text()').extract()
			item['location'] = listing.xpath('..//span[@class="l2"]/span[@class="pnr"]/small/text()').extract()
			yield item

# return as a JSON file: 
# scrapy crawl apt  -o items.json