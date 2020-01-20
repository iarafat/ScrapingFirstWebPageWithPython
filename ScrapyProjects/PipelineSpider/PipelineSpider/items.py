import scrapy


class CompanyDetailsItem(scrapy.Item):
    company_name = scrapy.Field()
    company_price_interaday = scrapy.Field()
