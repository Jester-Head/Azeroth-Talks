"""
This script contains a Scrapy spider for crawling the WoW Classic section of the Blizzard forums.
It extracts data from forum threads, excluding certain domains and forums.
"""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from classic.items import WowClassicItem


class ClassicForumsSpider(CrawlSpider):
    """
    Spider for crawling WoW Classic forum threads on the Blizzard forum.
    The spider starts from a given URL and follows the links based on defined rules.
    """
    name = 'forums_classic'
    allowed_domains = ['us.forums.blizzard.com']
    start_urls = [
        'https://us.forums.blizzard.com/en/wow/c/wow-classic/197']

    rules = (
        Rule(LinkExtractor(allow=('^https://us.forums.blizzard.com/en/wow/t/'),
             deny=('^https://worldofwarcraft.com/en-us/character/', '^https://us.forums.blizzard.com/en/wow/u/', 'https://us.forums.blizzard.com/en/wow/g/blizzard-tracker', 'https://us.forums.blizzard.com/en/wow/t/get-started-finding-people-here/215459', 'https://us.forums.blizzard.com/en/wow/c/wow-classic/wow-classic-lfg-lfm/201')), callback='parse_thread'),
        Rule(LinkExtractor(restrict_css="span > b", deny=('#suggested-topics',
             'div.topic-map', 'div.post-links-container', 'h3', 'div > aside')), follow=True)
    )

    def parse_thread(self, response):
        """
        Parses a forum thread and extracts data from each comment.
        The method skips extraction if the forum is 'WoW Classic New Guild Listings'.
        Each comment's text, quotes, likes, and date are extracted and stored in WowClassicItem.
        """
        comments = response.xpath('//div[@class="post"]')

        title = response.xpath('//h1/a/text()').extract_first()
        forum = response.xpath(
            '//*[@id="topic-title"]/div/span[2]/a/span[2]/span/text()').extract_first()

        if forum == "WoW Classic New Guild Listings":
            return

        for comment in comments:
            item = WowClassicItem()
            item['topic'] = title
            item['forum'] = forum
            item['comment'] = {
                # Storing text in an array
                'text_segments': comment.xpath('.//p/text()').extract(),
                'quotes': comment.xpath('.//blockquote/p/text()').extract(),
                'likes': comments.xpath('//span[contains(text(),\'Likes\')]/text()').extract_first(),
                'date': comments.xpath('//span[@class="crawler-post-infos"]/time[@itemprop="datePublished"]/@datetime').extract_first()
            }
            yield item
