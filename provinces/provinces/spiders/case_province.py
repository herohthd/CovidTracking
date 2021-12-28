import scrapy
from scrapy_splash import SplashRequest

class CaseProvinceySpider(scrapy.Spider):
    name = 'caseProvince'

    def start_requests(self):
        url = "https://vnexpress.net/covid-19/covid-19-viet-nam"

        yield SplashRequest(url=url,callback=self.parse)

    def parse(self, response):
        case_province = response.xpath('//div[@class="wrap-border"]/ul[@id="list-tinhthanh-v2"]/li')
        for case in case_province:
            yield{
                'province_name':case.xpath('.//div[@class="td"]/text()').get(),
                'case':case.xpath('.//div[@class="td black"]/b/text()').get(),
            }
                 
