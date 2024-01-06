import scrapy


class WowClassicItem(scrapy.Item):
    """
    Item class for storing scraped data from WoW Classic forum threads.

    Each item represents structured data from a single comment in a forum thread,
    including metadata and content of the comment.
    """

    topic = scrapy.Field()  # The title of the forum thread.
    forum = scrapy.Field()  # The name of the forum where the thread is posted.
    # A dictionary containing structured data about the comment.
    comment = scrapy.Field()
    # The text of the comment, broken into segments.
    text_segments = scrapy.Field()
    quote = scrapy.Field()  # Any quoted text from other comments.
    likes = scrapy.Field()  # The number of likes the comment has received.
    date = scrapy.Field()  # The date and time when the comment was posted.
