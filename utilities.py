import os
import ntpath
from utils.tools import loadJson, saveJson, jprint

def removeDuplicateDictsInList(lstDicts):
    """ taken from https://stackoverflow.com/a/9428041 """

    return [i for n, i in enumerate(lstDicts) if i not in lstDicts[n + 1:]]

def mergeNewToOldScrapedData(newJson, oldJson, tgtJson=None, moveNewJsonTo=None):
    """
    Merge new scraped data with the already scraped one,
    remove duplicate observations,
    store them, and move the new observation to another location (to be deleted)

    Args:
        newJson: str, full path of new JSON file
        oldJson: str, full path of old JSON file
        tgtJson: optional. str, full path of new JSON file to create by merging oldJson + newJson
        moveNewJsonTo: optional, str. full path to directory where to move the newJson file (and its .log, if exists)

    Returns:
        mergedJson: list of dicts, oldJson + newJson

    """

    new = loadJson(src=newJson)
    old = loadJson(src=oldJson)
    merged = old + new
    mergedClean = removeDuplicateDictsInList(lstDicts=merged)

    print(f"nb of observations in oldJson: {len(old)}\n"
          f"nb of observations in newJson: {len(new)}\n"
          f"nb of duplicated observations: {len(merged) - len(mergedClean)}\n"
          f"nb of new observations: {len(new) - (len(merged) - len(mergedClean))}\n"
          f"nb of unique observations in updated DataBase: {len(mergedClean)}\n")

    if tgtJson:
        saveJson(d=mergedClean, tgt=tgtJson)

    if moveNewJsonTo:
        os.replace(newJson, os.path.join(moveNewJsonTo, ntpath.basename(newJson)))

        newLog = newJson.replace('.json', '.log')
        if os.path.isfile(newLog):
            os.replace(newLog, os.path.join(moveNewJsonTo, ntpath.basename(newLog)))

    return mergedClean


if __name__ == "main":

    mergedDict = mergeNewToOldScrapedData(
        newJson=r"C:\CodeRug\immo\crawler\crawler\pap.json",
        oldJson=r"C:\CodeRug\immo\data\rawDB.json",
        tgtJson=r"C:\CodeRug\immo\data\rawDB.json",
        moveNewJsonTo=r"C:\CodeRug\immo\data\oldDataToDelete"
    )


