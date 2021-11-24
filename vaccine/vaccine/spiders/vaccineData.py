# -*- coding: utf-8 -*-
import scrapy


class VaccinedataSpider(scrapy.Spider):
    name = 'vaccineData'
    allowed_domains = ['vnexpress.net/covid-19']
    start_urls = ['https://vnexpress.net/covid-19/vaccine']

    def parse(self, response):
        pass
