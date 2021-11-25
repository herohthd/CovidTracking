import scrapy
from scrapy_splash import SplashRequest

class VaccineSpider(scrapy.Spider):
    name = 'vaccine'

    def start_requests(self):
        url = "https://vnexpress.net/covid-19/vaccine"

        yield SplashRequest(url=url,callback=self.parse)

    def parse(self, response):
        vaccines = response.xpath("//div[@id='vaccine_province']/ul[@data-weight]")
        for vaccine in vaccines:
            yield{
                'province_name':vaccine.xpath(".//li[1]/text()").get(),
                'province_vaccinated_population':vaccine.xpath(".//li[2]/text()").get().replace("\n", "").strip(),
                'province_vaccinated_percentage':vaccine.xpath(".//li[3]/div/div/span/text()").get(),
                'province_two_dose_population':vaccine.xpath(".//li[4]/text()").get().replace("\n", "").strip(),
                'province_two_dose_percentage':vaccine.xpath(".//li[5]/div/div/span/text()").get(),
            }
