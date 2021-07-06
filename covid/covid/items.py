import scrapy


class WorkItem(scrapy.Item):
    name = scrapy.Field()
    number_of_cases = scrapy.Field()
    deaths = scrapy.Field()
    continent = scrapy.Field()
