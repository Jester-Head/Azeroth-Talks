import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from classic.items import WowClassicItem


class SodForumsSpider(CrawlSpider):
    name = 'forums_classic'
    allowed_domains = ['us.forums.blizzard.com']
    start_urls = [
        'https://us.forums.blizzard.com/en/wow/c/wow-classic/197']

    rules = (
        Rule(LinkExtractor(allow=('^https://us.forums.blizzard.com/en/wow/t/'),
             deny=('^https://worldofwarcraft.com/en-us/character/', '^https://us.forums.blizzard.com/en/wow/u/', 'https://us.forums.blizzard.com/en/wow/g/blizzard-tracker','https://us.forums.blizzard.com/en/wow/t/get-started-finding-people-here/215459','https://us.forums.blizzard.com/en/wow/c/wow-classic/wow-classic-lfg-lfm/201')), callback='parse_thread'),
        Rule(LinkExtractor(restrict_css="span > b", deny=('#suggested-topics',
             'div.topic-map', 'div.post-links-container', 'h3', 'div > aside')), follow=True)
    )

    def parse_thread(self, response):
        comments = response.xpath('//div[@class="post"]')

        title = response.xpath('//h1/a/text()').extract_first()
        forum = response.xpath('//*[@id="topic-title"]/div/span[2]/a/span[2]/span/text()').extract_first()

        for comment in comments:
            item = WowClassicItem()
            item['topic'] = title
            item['forum'] = forum  
            item['comment'] = {
                'text':' '.join(comment.xpath('.//p/text()').extract()),
                'likes':comments.xpath('//span[contains(text(),\'Likes\')]/text()').extract_first(),
                'date':comments.xpath('//span[@class="crawler-post-infos"]/time[@itemprop="datePublished"]/@datetime').extract_first()
            }
            yield item

