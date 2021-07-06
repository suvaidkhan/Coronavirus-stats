import scrapy
from ..items import WorkItem


class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread']

    def parse(self, response):
        items = WorkItem()
        for row in response.xpath("//table//tr"):
            name = row.xpath(".//td[1]/text()").get()
            number_of_cases = row.xpath(".//td[2]/text()").get()
            deaths = row.xpath(".//td[3]/text()").get()
            continent = row.xpath(".//td[4]/text()").get()

            items['name'] = name
            items['number_of_cases'] = number_of_cases
            items['deaths'] = deaths
            items['continent'] = continent
            yield items
