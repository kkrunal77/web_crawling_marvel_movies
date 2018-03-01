# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class MarvelSpiderSpider(scrapy.Spider):
    name = 'marvel_spider'
    allowed_domains = ['http://marvel.com']
    start_urls = ['https://marvel.com/movies/all']

    def parse(self, response):
        # characters=response.css('[class*="JCAZList-list"] a::text').extract()
        main_page = BeautifulSoup(response.body, "lxml")
        # for c in characters:
        #     yield {'Character_Name':c}
        name  = main_page.find_all('a',{"class":"meta-title"})
        date  = main_page.find_all('p',{"class":"media-item-meta"})

        name = [i.text if len(i.text) else "None" for i in name]
        date = [i.text if len(i.text) else "None" for i in date]

        for a, b in zip(name, date):
            out_dict ={
            "Movie_name" : a,
	        "Movie_date" : b
	        }
            yield out_dict