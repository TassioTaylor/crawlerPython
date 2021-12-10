import scrapy

class Sp1Spider(scrapy.Spider):
    name = 'sp1'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']


    def parse(self, response):
        titulos = response.css ('.titleColumn ::text').getall()
        for titulo in titulos:
            yield {
                'title': response.css ('.titleColumn a ::text').get(),
                'ano': response.css('.secondaryInfo::text').get(),                 
            }
