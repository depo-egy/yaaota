import scrapy

class ComputerSpider(scrapy.Spider):
    name="ecommerce"

    start_urls = ['https://2b.com.eg/en/computers.html' , 'https://2b.com.eg/en/mobile-tablet.html' ,
     'https://2b.com.eg/en/home-appliances.html', 'https://2b.com.eg/en/accessories.html', 'https://2b.com.eg/en/gaming.html']
    
    

    def parse(self, response):
        product_selector = 'a.product-item-link'
        for item in response.css(product_selector):
            URL_SELECTOR = 'a ::attr(href)'
            TITLE_SELECTOR = 'a::text'

            yield {
                'URL': item.css(URL_SELECTOR).get(),
                'TITLE': (item.css(TITLE_SELECTOR).get())[2:].strip(),
                'MAIN_CATEGORY': response.xpath("//ul[@class='items']//li[2]//strong//text()").get(),
            }

        next_page = response.css('li.pages-item-next a::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        

    # def parse(self, response):
    #     self.logger.info('Hello Yaaota !')
    #     ol = response.xpath("//ol").get()
    #     for li in ol:
    #         yield {
    #              'URL': response.css('a.product-item-link::attr(href)').get(),
    #              'TITLE': (response.css('a.product-item-link::text').get())[2:].strip(),
    #              'MAIN_CATEGORY': response.xpath("//ul[@class='items']//li[2]//strong//text()").get(),
    #          }
        
        # yield {
        #         'URL': response.css('a.product-item-link::attr(href)').get(),
        #         'TITLE': (response.css('a.product-item-link::text').get())[2:].strip(),
        #         'MAIN_CATEGORY': response.xpath("//ul[@class='items']//li[2]//strong//text()").get(),
        #     }
        # elif self.start_urls[1]:
        #     yield {
        #         'URL': response.css('a.product-item-link::attr(href)').get(),
        #         'TITLE': (response.css('a.product-item-link::text').get())[2:].strip(),
        #         'MAIN_CATEGORY': response.xpath("//ul[@class='items']//li[2]//strong//text()").get(),
        #     }


# class MobileSpider(scrapy.Spider):
#     name="mobile"

#     # start_urls = ['https://2b.com.eg/en/computers.html' , 'https://2b.com.eg/en/mobile-tablet.html' ,
#     #  'https://2b.com.eg/en/home-appliances.html', 'https://2b.com.eg/en/accessories.html', 'https://2b.com.eg/en/gaming.html']
#     start_urls = ['https://2b.com.eg/en/mobile-tablet.html']

#     def parse(self, response):
#         self.logger.info('Hello Yaaota !')
#         # ol = response.xpath("//ol").get()
#         # for li in ol:
#         #     yield {
#         #         'URL': response.css('a.product-item-link::attr(href)').get(),
#         #         'Title': (response.css('a.product-item-link::text').get())[2:].strip(),
#         #          'Main Category': 'Mobile',
#         #     }
#         yield {
#                 'URL': response.css('a.product-item-link::attr(href)').get(),
#                 'TITLE': (response.css('a.product-item-link::text').get())[2:].strip(),
#                  'MAIN_CATEGORY': 'Mobile',
#             }

# class MobileSpider(scrapy.Spider):
#     name="mobile"

#     # start_urls = ['https://2b.com.eg/en/computers.html' , 'https://2b.com.eg/en/mobile-tablet.html' ,
#     #  'https://2b.com.eg/en/home-appliances.html', 'https://2b.com.eg/en/accessories.html', 'https://2b.com.eg/en/gaming.html']
#     start_urls = ['https://2b.com.eg/en/mobile-tablet.html']

#     def parse(self, response):
#         self.logger.info('Hello Yaaota !')
#         # ol = response.xpath("//ol").get()
#         # for li in ol:
#         #     yield {
#         #         'URL': response.css('a.product-item-link::attr(href)').get(),
#         #         'Title': (response.css('a.product-item-link::text').get())[2:].strip(),
#         #          'Main Category': 'Mobile',
#         #     }
#         yield {
#                 'URL': response.css('a.product-item-link::attr(href)').get(),
#                 'TITLE': (response.css('a.product-item-link::text').get())[2:].strip(),
#                  'MAIN_CATEGORY': 'Mobile',
#             }


# class MobileSpider(scrapy.Spider):
#     name="mobile"

#     # start_urls = ['https://2b.com.eg/en/computers.html' , 'https://2b.com.eg/en/mobile-tablet.html' ,
#     #  'https://2b.com.eg/en/home-appliances.html', 'https://2b.com.eg/en/accessories.html', 'https://2b.com.eg/en/gaming.html']
#     start_urls = ['https://2b.com.eg/en/mobile-tablet.html']

#     def parse(self, response):
#         self.logger.info('Hello Yaaota !')
#         # ol = response.xpath("//ol").get()
#         # for li in ol:
#         #     yield {
#         #         'URL': response.css('a.product-item-link::attr(href)').get(),
#         #         'Title': (response.css('a.product-item-link::text').get())[2:].strip(),
#         #          'Main Category': 'Mobile',
#         #     }
#         yield {
#                 'URL': response.css('a.product-item-link::attr(href)').get(),
#                 'TITLE': (response.css('a.product-item-link::text').get())[2:].strip(),
#                  'MAIN_CATEGORY': 'Mobile',
#             }


# class MobileSpider(scrapy.Spider):
#     name="mobile"

#     # start_urls = ['https://2b.com.eg/en/computers.html' , 'https://2b.com.eg/en/mobile-tablet.html' ,
#     #  'https://2b.com.eg/en/home-appliances.html', 'https://2b.com.eg/en/accessories.html', 'https://2b.com.eg/en/gaming.html']
#     start_urls = ['https://2b.com.eg/en/mobile-tablet.html']

#     def parse(self, response):
#         self.logger.info('Hello Yaaota !')
#         # ol = response.xpath("//ol").get()
#         # for li in ol:
#         #     yield {
#         #         'URL': response.css('a.product-item-link::attr(href)').get(),
#         #         'Title': (response.css('a.product-item-link::text').get())[2:].strip(),
#         #          'Main Category': 'Mobile',
#         #     }
#         yield {
#                 'URL': response.css('a.product-item-link::attr(href)').get(),
#                 'TITLE': (response.css('a.product-item-link::text').get())[2:].strip(),
#                  'MAIN_CATEGORY': 'Mobile',
#             }