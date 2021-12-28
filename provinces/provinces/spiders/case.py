import scrapy
from scrapy_splash import SplashRequest

class CaseSpider(scrapy.Spider):
    name = 'case'

    def start_requests(self):
        url = "https://vnexpress.net/covid-19/covid-19-viet-nam"

        yield SplashRequest(url=url,callback=self.parse)

    def parse(self, response):
        cases = response.xpath('//div[@id="total-all"]')
        for case in cases:
            yield{
                'total_cases':case.xpath('.//div[contains(@class,"item-count-vietnam item-nhiem")]/span[@class="number-item"]/text()').get(),
                'today_cases':case.xpath('.//div[contains(@class,"item-count-vietnam item-nhiem")]/span[@class="today-item"]/text()').get(),
                'total_recover':case.xpath('.//div[contains(@class,"item-count-vietnam item-khoi")]/span[@class="number-item"]/text()').get(),
                'today_recover':case.xpath('.//div[contains(@class,"item-count-vietnam item-khoi")]/span[@class="today-item"]/text()').get(),
                'total_death':case.xpath('.//div[contains(@class,"item-count-vietnam item-tuvong")]/span[@class="number-item"]/text()').get(),
                'today_death':case.xpath('.//div[contains(@class,"item-count-vietnam item-tuvong")]/span[@class="today-item"]/text()').get(),
                'total_treated':case.xpath('.//div[contains(@class,"item-count-vietnam item-dangdieutri")]/span[@class="number-item"]/text()').get(),
                'today_treated':case.xpath('.//div[contains(@class,"item-count-vietnam item-dangdieutri")]/span[@class="today-item"]/text()').get(),
            }
