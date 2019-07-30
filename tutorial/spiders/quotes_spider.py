import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'law-college'
    page_no = 2
    start_urls = [
        'https://nodesk.co/remote-companies/',
    ]

    def parse(self, response):
        for college in response.css(".b--blue"): 
            yield {
                
                'Company Name':college.css('.mt3::text').get(),
                'Description':college.css('.mt0::text').get(),
                'Logo': college.css("img::attr(data-src)").get(),
                }
                

 