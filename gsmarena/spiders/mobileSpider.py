import scrapy
import logging


class MobileSpider(scrapy.Spider):
	name = 'gsmMobile'
	start_urls = [
		'http://www.gsmarena.com/oneplus-phones-95.php',
	]

	def parse(self, response):
		for link in response.css('#review-body > div > ul > li > a::attr(href)'):
			yield response.follow(link, callback=self.parse_mobile)

	def parse_mobile(self, response):
		score = response.css('.specs-fans strong::text').extract_first()
		name = response.css('.specs-phone-name-title::text').extract_first()
		specs = {}
		logging.info(str(score))
		for spec_table in response.css('#specs-list table'):
			spec_category = spec_table.css('th::text').extract_first()
			spec_category = spec_category if spec_category is not None else ''
			for spec_row in spec_table.css('tr'):
				spec_key = spec_row.css('.ttl a::text').extract_first()
				spec_key = spec_row.css('.ttl::text').extract_first() if spec_key is None else spec_key
				spec_key = spec_key if spec_key is not None else ''
				try:
					spec_key = str(spec_category) + '_' + str(spec_key)
					spec_value = spec_row.css('.nfo a::text').extract_first()
					spec_value = spec_row.css('.nfo::text').extract_first() if spec_value is None else spec_value
					if spec_key is not None and len(spec_key) > 0 and spec_value is not None:
						specs[spec_key] = spec_value
				except:
					pass
		if score is None:
			raise ValueError('BOT FOUND!! Empty body returned')
		return {
			'score': score,
			'specs': specs,
			'name': name
		}
