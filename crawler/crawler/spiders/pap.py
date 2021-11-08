from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from ..items import PapItem
from w3lib.url import url_query_cleaner
import urllib


def generatePapUrl(searchParams):

    annonceType = searchParams["type"]
    bien = searchParams["bien"]
    ville = searchParams["ville"]
    codePostal = searchParams["codePostal"]
    nPieces = searchParams["nPieces"]
    minChambres = searchParams["minChambres"]
    prix = searchParams["prix"]
    surface = searchParams["surface"]


    return f"https://www.pap.fr/annonce/{annonceType}-{bien}-{ville}-{codePostal}-g439-{nPieces}-{minChambres}-{prix}-{surface}"

def getStartUrlsList(startUrl):
    """ define starting URLs to parse all annonces, even though those that appear only when 'scrolling down' """

    start_urls = [startUrl]
    redirectedStartUrl = urllib.request.urlopen(f"{startUrl}-1").geturl()

    # stop when new redirected URL is == at the starting redirected URL:
    k = 2
    while urllib.request.urlopen(f"{startUrl}-{k}").geturl() != redirectedStartUrl:
        # start_urls.append(urllib.request.urlopen(f"{startUrl}-{k}").geturl())
        start_urls.append(f"{startUrl}-{k}")
        k += 1

    return start_urls

def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

"""
?
one crawler for getting all the URLs of the annonces,
one crawler to visit each of those URLs and extyract info
"""

SEARCH_PARAMS = {
    "type": "location",
    "ville": "paris",
    "codePostal": "75",
    "bien": "appartement",
    "nPieces": None,
    "minChambres": None,
    "prix": None,
    "surface": "jusqu-a-12-m2",
}
startUrl = generatePapUrl(searchParams=SEARCH_PARAMS)

class PapCrawler(CrawlSpider):

    name = 'pap'
    allowed_domains = ['www.pap.fr']
    start_urls = getStartUrlsList(startUrl)

    rules = (
        Rule(LinkExtractor(allow=r'/annonces/'), process_links=process_links, callback='parse_annonce', follow=True),
    )

    def parse_annonce(self, response):
        """ extract info from each crawled annonce URL found """

        print(f"parse_annonce: {response.url}")

        # to ease reading and debugging:
        annoncePostDate = response.xpath("/html/body/div[2]/div/div[1]/div[2]/div/p/text()").get()
        ville = response.xpath("/html/body/div[2]/div/div[1]/div[6]/h2/text()").get()
        fullCodePostal = response.xpath("/html/body/div[2]/div/div[1]/div[6]/h2/text()").get()

        # store annonces info in item:
        item = PapItem()
        item["title"] = response.xpath("/html/body/div[2]/div/div[1]/h1/text()").get()
        item["prix"] = response.xpath("/html/body/div[2]/div/div[1]/h1/span/text()").get()
        item["annonceRefDate"] = response.xpath("/html/body/div[2]/div/div[1]/div[2]/div/p/text()").get()
        item["annonceUrlRef"] = response.url.split('-')[-1]
        item["annoncePostDate"] = annoncePostDate.split('/')[-1] if annoncePostDate is not None else None
        item["location"] = response.xpath("/html/body/div[2]/div/div[1]/div[6]/h2/text()").get()
        item["ville"] = ville.split()[0] if ville is not None else None
        item["fullCodePostal"] = fullCodePostal.split()[-1] if fullCodePostal is not None else None
        item["nPieces"] = response.xpath("/html/body/div[2]/div/div[1]/div[6]/ul[1]/li[1]/strong/text()").get()
        item["surface"] = response.xpath("/html/body/div[2]/div/div[1]/div[6]/ul[1]/li[2]/strong/text()").get()
        item["bien"] = response.xpath("/html/body/div[2]/div/div[1]/div[6]/div/p[1]/b/text()").get()
        item["description"] = response.xpath("/html/body/div[2]/div/div[1]/div[6]/div/p[1]/text()").getall()
        item["telephoneContact"] = response.xpath("/html/body/div[2]/div/div[1]/div[7]/p[2]/span/text()").get()
        item["pictures"] = response.xpath("/html/body/div[2]/div/div[1]/div[5]/a/img").getall()

        yield item
