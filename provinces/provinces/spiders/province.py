import scrapy
from scrapy_splash import SplashRequest

class ProvinceSpider(scrapy.Spider):
    name = 'province'

    def start_requests(self):
        url = "https://e.vnexpress.net/covid-19/vaccine"

        yield SplashRequest(url=url,callback=self.parse)

    def parse(self, response):
        provinces = response.xpath("//div[@id='total_vaccine_province']/ul[@data-weight]")
        for province in provinces:
            yield{
                'province_name':province.xpath(".//li[1]/text()").get(),
                'province_population':province.xpath(".//li[2]/text()").get(),
                'province_expected_distribution':province.xpath(".//li[3]/text()").get(),
                'province_actual_distribution':province.xpath(".//li[4]/text()").get(),
                'province_distribution_percentage':province.xpath(".//li[5]/div/div/span/text()").get(),
            }
