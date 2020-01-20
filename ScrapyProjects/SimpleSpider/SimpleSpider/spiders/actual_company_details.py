from pprint import pprint

import scrapy

filename = 'actual_company_details.txt'


class ActualCompanyDetails(scrapy.Spider):
    name = 'actual_company_details'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/sector/ms_technology']

    def parse(self, response):
        company_names_list = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[2]/text()').extract()
        company_price_list = response.xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[3]/span/text()').extract()

        # pprint(company_price_list)
        count = len(company_names_list)
        # print('count', count)

        with open(filename, 'a+') as file:
            for i in range(0, count):
                # print(company_names_list[i])
                # file.write("%d , %d\r\n" % company_names_list[i] % company_price_list[i])
                file.write(company_names_list[i] + ' , ' + company_price_list[i] +"\r\n")
