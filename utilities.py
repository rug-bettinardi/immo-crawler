import os
from utils.tools import loadJson, saveJson, jprint

def removeDuplicateDictsInList(lstDicts):

    return [i for n, i in enumerate(lstDicts) if i not in lstDicts[n + 1:]]  # taken from https://stackoverflow.com/a/9428041
    # return {frozenset(item.items()): item for item in lstDicts}.values()  # taken from: https://stackoverflow.com/a/23358757

def mergeNewToOldScrapedData(newJson, oldJson, tgtJson=None):
    """

    Args:
        newJson: str, full path of new JSON file
        oldJson: str, full path of old JSON file
        tgtJson: optional. str, full path of new JSON file to create by merging oldJson + newJson

    Returns:
        merged: list of dicts, oldJson + newJson

    """

    new = loadJson(src=newJson)
    old = loadJson(src=oldJson)
    merged = old + new



    if tgtJson:
        saveJson(d=merged, tgt=tgtJson)

    return merged


if __name__ == "main":

    merged = mergeNewToOldScrapedData(
        newJson=r"C:\CodeRug\immo\crawler\crawler\pap.json",
        oldJson=r"C:\CodeRug\immo\crawler\crawler\pap_old.json",
        tgtJson=r"C:\CodeRug\immo\data\rawDB.json"
    )



    merged = mergeNewToOldScrapedData(
        newJson=r"C:\CodeRug\immo\crawler\crawler\pap.json",
        oldJson=r"C:\CodeRug\immo\crawler\crawler\pap_old.json",
        tgtJson=None
    )

    rd = removeDuplicateDictsInList(lstDicts=merged)