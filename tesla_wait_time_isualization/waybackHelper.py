import json
import urllib


def getAvailableWebArchive(url):
    availableArchiveURLs = f"https://web.archive.org/cdx/search/cdx?url={url}&output=json"
    resp = urllib.request.urlopen(availableArchiveURLs)
    archiveResponse = resp.read().decode('utf-8')
    jsonArchive = json.loads(archiveResponse)
    return jsonArchive


def getDay(datestring):
    return datestring[6:8]


def isSuccessfulRedirect(item):
    if (item[4] == "200"):
        return True
    else:
        return False


def buildDownloadLink(date, modelURL):
    return f"https://web.archive.org/web/{date}/{modelURL}"


def isIndividualDate(item, baseDay):
    if getDay(item[1]) == baseDay:
        return True
    if getDay(item[1]) != baseDay:
        return False


def getValidModelArchiveLinks(jsonArchive):
    validJSONArchive = []
    sublist = []
    baseDay = getDay(jsonArchive[1][1])

    for item in jsonArchive[1:]:
        if isSuccessfulRedirect(item) and item not in sublist:
            if isIndividualDate(item, baseDay):
                sublist.append(item)
            else:
                baseDay = getDay(item[1])
                validJSONArchive.append(sublist[0])
                sublist = []
                sublist.append(item)

    return validJSONArchive