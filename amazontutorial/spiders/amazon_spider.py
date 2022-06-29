import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/b?node=17938598011&pf_rd_r=KEW495H06QPN6QSS4TY1&pf_rd_p=e5b0c85f-569c-4c90-a58f-0c0a260e45a0&pd_rd_r=a8b886cb-aa80-4a43-907f-fa156ef70fd9&pd_rd_w=GybFK&pd_rd_wg=TtDmn&ref_=pd_gw_unk']

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css(".a-text-normal::text").extract() 
        product_image = response.css('.s-image::attr(src)').extract()

        items['product_name']=product_name
        # items['product_price']= product_price
        items['product_image']= product_image
        yield items

