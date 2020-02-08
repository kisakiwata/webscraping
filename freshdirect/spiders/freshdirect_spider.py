from scrapy import Spider, Request
from freshdirect.items import FreshdirectItem
import re

#domain issue
#https://stackoverflow.com/questions/37857554/scrapy-do-not-crawl-links-on-other-domains-page

class FreshdirectSpider(Spider):
    name = 'freshdirect_spider'
    allowed_urls = ['https://www.freshdirect.com']
    start_urls = ['https://www.freshdirect.com/srch.jsp?pageType=search&searchParams=plant-based&pageSize=30&all=false&activePage=1&sortBy=Sort_PopularityUp&orderAsc=true&activeTab=product&brandFilterGroup=clearall&departmentFilterGroup=clearall']

    def parse(self, response):
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        text = response.xpath('//p[@class="pagination-text"]/text()').extract_first()
        text = list(map(lambda x: int(x), re.findall('\d+', text)))
        per_page, total = text[1], text[2]
        number_pages = (total // per_page)+1

        # List comprehension to construct all the urls
        result_urls = ['https://www.freshdirect.com/srch.jsp?pageType=search&searchParams=plant-based&pageSize=30&all=false&activePage={}&sortBy=Sort_PopularityUp&orderAsc=true&activeTab=product&brandFilterGroup=clearall&departmentFilterGroup=clearall'.format(x) for x in range(1,number_pages+1)]

        # Yield the requests to different search result urls, 
        # using parse_result_page function to parse the response.
        for url in result_urls:
            yield Request(url=url, callback=self.parse_result_page) 


    def parse_result_page(self, response):
        # This fucntion parses the search result page.
        
        # We are looking for url of the detail page.
        detail_urls = response.xpath('//div[@class="isHookLogic-false browse-sections-top-cont"]//a[@class="portrait-item-image-link"]/@href').extract()
        #40items instead of 30??

        # Yield the requests to the details pages, 
        # using parse_detail_page function to parse the response.
        for url in ['https://www.freshdirect.com{}'.format(x) for x in detail_urls]:
            
            i = 1
            for i in range(len(detail_urls)):
                pro_index = i
                i += 1

            if not detail_urls:
                pass

            yield Request(url=url, callback=self.parse_detail_page, meta={'pro_index': pro_index})

    def parse_detail_page(self, response):

        pro_index = response.meta['pro_index']
        
        # Product name
        try:
            product = response.xpath('//h1[@class="pdpTitle"]//span[@itemprop="name"]/text()').extract_first()

        except:
            product = ""

        # Brand name
        try:
            brand = response.xpath('//div[@class="pdp-productName"]//span[@itemprop="brand"]/text()').extract_first()
        except:
            brand = ""

        # Price
        try:
            price = response.xpath('//div[@class="span-8 prepend-1"]//div[@class="pdp-price"]/text()').extract_first()
            #price = response.xpath('//div[@class="subtotal  hasPrice"]//span[@class="subtotal-inner"]/text()').extract_first()
            price = re.findall('\d+.?\d+', price)
            price = float(price[0])
        except:
            price = ""

        #claims = response.xpath('//li[@class="pdp-accordion-description pdp-accordion-item"]/div/ul/li/text()').extract()
        
        # category1
        category1 = response.xpath('//div[@class="browse-breadcrumbs"]//li[@class="first"]/a/text()').extract_first()
        # category2
        category2 = response.xpath('//div[@class="browse-breadcrumbs"]//li[2]/a/text()').extract_first()

        # category3
        try:
            category3 = response.xpath('//div[@class="browse-breadcrumbs"]//li[3]/a/text()').extract_first()
        except:
            category3 = ""

        # category4
        try:
            category4 = response.xpath('//div[@class="browse-breadcrumbs"]//li[4]/a/text()').extract_first()
        except:
            category4 = ""


        item = FreshdirectItem()
        item['pro_index'] = pro_index
        item['product'] = product
        item['price'] = price
        item['brand'] = brand
        item['category1'] = category1
        item['category2'] = category2
        item['category3'] = category3
        item['category4'] = category4

        yield item



