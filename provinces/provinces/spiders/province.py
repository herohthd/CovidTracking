import scrapy
from scrapy_splash import SplashRequest
from scrapy.crawler import CrawlerProcess
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

# process = CrawlerProcess(settings={
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
#     "FEEDS": {
#         "province.json": {"format": "json"},
#     },
# })

# process.crawl(ProvinceSpider)
# process.start()

