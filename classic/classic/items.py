import scrapy

class WowClassicItem(scrapy.Item):
    topic = scrapy.Field()
    forum = scrapy.Field()
    comment = scrapy.Field()
    text_segments = scrapy.Field()
    quote = scrapy.Field()
    likes = scrapy.Field()
    date = scrapy.Field()


