import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from arbolCategoria.items import ArbolcategoriaItem
from scrapy.exceptions import CloseSpider

class ArbolCategoriaSpider(CrawlSpider):
    name='arbolCategoria'
    allowed_domain=['https://www.6pm.com/']
    start_urls=["https://www.6pm.com/null/.zso?s=isNew%2Fdesc%2FgoLiveDate%2Fdesc%2FrecentSalesStyle%2Fdesc%2F"]
    cont=0

    rules={
        Rule(LinkExtractor(allow=(), restrict_xpaths=('(//div[@class="NT"]/ul)[1]/li/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('(//div[@class="NT"]/ul)[1]/li/a')),
        callback="parse_item",follow=True),
    #//section[@class="FU undefined"]/div/ul/li/a}
    #//section[@class="FU undefined WU"]/div/ul/li/a
    #//section[@class="FU undefined"]/div/ul/li/a

    }
    def parse_item(self,response):
        camposArbol=ArbolcategoriaItem()
        size=response.xpath('//*[@id="searchFilters"]/div[1]/div[2]/section[1]/h3/button/text()').extract()
        rutaFinal=response.xpath('//*[@id="searchSelectedFilters"]/div/ul/li//text()').extract()
        branAndSize=response.xpath('//*[@id="searchFilters"]/div[1]/div[2]/section[1]/div[2]/ul/li/a//text()').extract()
        isSize=size[0]
        haySize=isSize.find("Size")
        hayBrand=isSize.find("Brand")
        
        if haySize != -1 or hayBrand != -1:
            for a in branAndSize:
                if a in rutaFinal:
                    return
            camposArbol['url']=response.url
            camposArbol['ruta']=response.xpath('//*[@id="searchSelectedFilters"]/div/ul/li//text()').extract()
            camposArbol['categoria']=response.xpath('//h1/text()').extract()
            camposArbol['is_final']='True'
            print(camposArbol)
            self.cont=0
            yield camposArbol
        
       
        
            