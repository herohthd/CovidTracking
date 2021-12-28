import scrapy
from scrapy_splash import SplashRequest

class CaseByDaySpider(scrapy.Spider):
    name = 'caseByDay'

    def start_requests(self):
        url = "https://covidlive.com.au/country/vietnam"

        yield SplashRequest(url=url,callback=self.parse)

    def parse(self, response):
        cases = response.xpath('//table[@class="DAILY-CASES-WORLDWIDE"]/tbody/tr[not(contains(@class,"TH"))]')
        for case in cases:
            yield{
                'date':case.xpath('string(.//td[@class="COL1 DATE"])').get(),
                'cases':case.xpath('.//td[@class="COL4 NET"]/span/text()').get(),
            }
                 
