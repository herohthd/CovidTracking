import scrapy
from scrapy_splash import SplashRequest

class DoseSpider(scrapy.Spider):
    name = 'dose'

    def start_requests(self):
        url = "https://covidvax.live/location/vnm"

        yield SplashRequest(url=url,callback=self.parse)

    def parse(self, response):
        doses = response.xpath('//tbody[@id="dateTable"]/tr')
        for dose in doses:
            yield{
                'date':dose.xpath('.//td[@scope="row" and @class="headcol"]/text()').get(),
                'total_doses':dose.xpath('.//td[2]/text()').get(),
                'daily_doses':dose.xpath('.//td[4]/text()').get()
            }
