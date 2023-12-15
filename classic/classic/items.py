import scrapy

class WowClassicItem(scrapy.Item):
    topic = scrapy.Field()
    forum = scrapy.Field()
    comment = scrapy.Field()
    text = scrapy.Field()
    likes = scrapy.Field()
    date = scrapy.Field()


