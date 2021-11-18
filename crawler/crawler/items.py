# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PapItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    prix = scrapy.Field()
    annonceRefDate = scrapy.Field()
    annonceUrlRef = scrapy.Field()
    annoncePostDate = scrapy.Field()
    location = scrapy.Field()
    ville = scrapy.Field()
    fullCodePostal = scrapy.Field()
    nPieces = scrapy.Field()
    surface = scrapy.Field()
    bien = scrapy.Field()
    description = scrapy.Field()
    telephoneContact = scrapy.Field()
    pictures = scrapy.Field()

