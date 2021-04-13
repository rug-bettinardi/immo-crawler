params = {
    "type": "locations",
    "localisation": "paris-75",
    "bien": "appartement",  
    "nPieces": "du-studio-au-2-pieces",
    "minChambres": "a-partir-de-1-chambres",
    "prix": "entre-400-et-1000-euros",
    "surface": "entre-8-et-12-m2",
}




searchParams = {
    "type": "location",
    "localisation": "paris-75",
    "bien": "appartement",
    "nPieces": None,
    "minChambres": None,
    "prix": None,
    "surface": "jusqu-a-12-m2",
}

def generateUrl(searchParams):

    annonceType = searchParams["type"]
    bien = searchParams["bien"]
    where = searchParams["localisation"]
    nPieces = searchParams["nPieces"]
    minChambres = searchParams["minChambres"]
    prix = searchParams["prix"]
    surface = searchParams["surface"]

    url = f"https://www.pap.fr/annonce/{annonceType}-{bien}-{where}-g439-{nPieces}-{minChambres}-{prix}-{surface}"



