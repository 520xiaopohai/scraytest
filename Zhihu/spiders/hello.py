# -*- coding: utf-8 -*-
import scrapy
import re

class HelloSpider(scrapy.Spider):
    name = 'hello'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112812/']

    def parse(self, response):


        """
        获取文章列表的URL 并交给解析函数进行具体字段的解析
        获取下一页的URL 交给scrapy下载

        :param response:
        :return:
        """

        re_selector = response.xpath('//*[@id="post-112812"]/div[1]/h1/text()')
        re2_selector = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1/text()')
        re3_selector = response.xpath('//div[@class="entry-header"]/h1/text()')
        title = re_selector.extract()[0]
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace("·","").strip()
        post_up = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]

        # fav_nums = response.xpath('//span[contains(@class,"bookmark-btn")]/text()')
        # match_re = re.match(r".*(\d+).*",fav_nums)
        # if match_re:
        #     fav_nums = match_re.group(1)
        # else:
        #     fav_nums = 0
        #
        # comment_nums = response.xpath('//a[@href="#article-comment"]/span/text()')
        # match2_re = re.match(r".*(\d+).*", fav_nums)
        # if match2_re:
        #     comment_nums = match2_re.group(1)
        # else:
        #     comment_nums = 0

        content = response.xpath('//div[@class = "entry"]').extract()[0]
        tag_list = create_date = response.xpath('//a[@href="article-comment"]/span').extract()

        #通过css选择器提取字段
        # title=  response.css(".entry-header h1::text").extract()[0]
        #create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·","").strip()
        # vote-post-up = response.css(".vote-post-up h10").extract()[0]

        pass
