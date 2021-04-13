from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


def generateUrl(searchParams):

    annonceType = searchParams["type"]
    bien = searchParams["bien"]
    where = searchParams["localisation"]
    nPieces = searchParams["nPieces"]
    minChambres = searchParams["minChambres"]
    prix = searchParams["prix"]
    surface = searchParams["surface"]

    return f"https://www.pap.fr/annonce/{annonceType}-{bien}-{where}-g439-{nPieces}-{minChambres}-{prix}-{surface}"


SEARCH_PARAMS = {
    "type": "location",
    "localisation": "paris-75",
    "bien": "appartement",
    "nPieces": None,
    "minChambres": None,
    "prix": None,
    "surface": "jusqu-a-12-m2",
}
startUrl = generateUrl(searchParams=SEARCH_PARAMS)

class PapCrawler(CrawlSpider):

    name = 'pap'
    allowed_domains = ['www.pap.fr']
    start_urls = [startUrl]

    custom_settings = {
        "BOT_NAME": 'home_sweet_home',
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",  # todo ?
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_DELAY": 3,
        "DEPTH_LIMIT": 2,
    }

    rules = (Rule(LinkExtractor()),)