import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'law-college'
    page_no = 20
    start_urls = [
        "https://targetstudy.com/colleges/colleges-in-delhi.html?recNo=10",
    ]

    def parse(self, response):
        for college in response.css(".panel.panel-custom"): 
            yield {
                
                'link': college.css(".heading1::attr(href)").get(),
                # 'Company Name':college.css('.mt3::text').get(),
                # 'Description':college.css('.mt0::text').get(),
                # 'Logo': college.css("img::attr(data-src)").get(),
                }
            next_page="https://targetstudy.com/colleges/colleges-in-delhi.html?recNo="+str(QuotesSpider.page_no)
            if QuotesSpider.page_no < 1100:
                QuotesSpider.page_no += 10
                yield response.follow(next_page, self.parse)
                

 