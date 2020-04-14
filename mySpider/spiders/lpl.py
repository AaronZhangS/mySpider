# -*- coding: utf-8 -*-
import scrapy


class LplSpider(scrapy.Spider):
    name = 'lpl'
    start_urls = ['https://tiyu.baidu.com/match/LPL/tab/%E6%8E%92%E5%90%8D/from/baidu_aladdin']

    def parse(self, response):
        div_list = response.xpath("//div[@class='wa-tiyu-rank-basketball']//div[@class='wa-tiyu-rank-basketball-record c-row']")
        for div in div_list:
            item = {}
            item['rank'] = div.xpath(".//div[@class='c-span4']//div[@class='c-row']//div[@class='c-span2']/text()").extract_first()
            item['name'] = div.xpath(".//div[@class='c-span4']//div[@class='c-row']//div[@class='c-span7 c-line-clamp1']/text()").extract_first()
            item['src'] = div.xpath(".//div[@class='c-span4']//div[@class='c-row']//div[@class='c-span2']//img/@src").extract_first()
            item['session'] = div.xpath(".//div[@class='c-span2']//span/text()")[0].extract()
            item['victory'] = div.xpath(".//div[@class='c-span2']//span/text()")[1].extract()
            item['loss'] = div.xpath(".//div[@class='c-span2']//span/text()")[2].extract()
            item['scroe'] = div.xpath(".//div[@class='c-span2']//span/text()")[3].extract()
            yield item