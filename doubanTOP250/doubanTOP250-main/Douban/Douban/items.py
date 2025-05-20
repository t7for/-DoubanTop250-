# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # 数据建模
    name = scrapy.Field()
    quote = scrapy.Field()
    score= scrapy.Field()
    info = scrapy.Field()
