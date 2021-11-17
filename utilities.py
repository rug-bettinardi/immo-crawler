import os
from utils.tools import loadJson, jprint, saveJson


def mergeNewToOldScrapedData(newJson, oldJson, tgtJson=None):
    """

    :param newJson: str, full path of new JSON file
    :param oldJson: str, full path of old JSON file
    :param tgtJson: optional. str, full path of new JSON file to create by merging old + new
    :return: list of dicts, oldJson + newJson

    """

    new = loadJson(src=newJson)
    old = loadJson(src=oldJson)
    merged = old + new

    if tgtJson:
        saveJson(d=merged, tgt=tgtJson)

    return merged

def eliminateDuplicates(jsonFile):
    pass

if __name__ == "main":

    merged = mergeNewToOldScrapedData(
        newJson=r"C:\CodeRug\immo\crawler\crawler\pap.json",
        oldJson=r"C:\CodeRug\immo\crawler\crawler\pap_old.json",
        tgtJson=r"C:\CodeRug\immo\data\rawDB.json"
    )




