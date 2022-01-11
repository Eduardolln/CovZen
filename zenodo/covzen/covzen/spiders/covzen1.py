import scrapy


class Covzen1Spider(scrapy.Spider):
    name = 'covzen1'
    start_urls = ['http://https://zenodo.org/communities/covid-19/?page=1/']

    def parse(self, response):
        pass
