# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JkSpider(CrawlSpider):
    name = 'jk'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://xiaohua.zol.com.cn/lengxiaohua/1.html']
    num = 1

    rules = (
        Rule(LinkExtractor(allow=r'.+/lengxiaohua/\d+\.html'),follow=True),
        Rule(LinkExtractor(allow=r'.+/detail\d+/\d+\.html'),callback='parse_item',follow=False),
    )

    def parse_item(self, response):
        print("="*50, self.num, "="*50)
        # li_list = response.xpath("//ul[@class='article-list']/li[@class='article-summary']")
        print(response.url)
        item = dict()
        item["title"] = response.xpath("//div[@class='article-header']/h1/text()").get()
        sp2 = response.xpath(".//div[@class='article-source']/span[2]/text()").get()
        if sp2:
            item["source"] = response.xpath(".//div[@class='article-source']/span[2]/text()").get()
        else:
            item["source"] = response.xpath(".//div[@class='article-source']/a/text()").get()

        item["content"] = "".join(response.xpath(".//div[@class='article-text']//text()").getall()).strip()

        print(item)
        self.num +=1
