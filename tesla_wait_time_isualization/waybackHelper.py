import json
import urllib3


# Conection timing out? How to solve this porlbem? Try: again later?
def getAvailableWebArchive(url):
    print("Reurning available historic URLs for: ", url)
    webArchiveSearchURL = f"https://web.archive.org/cdx/search/cdx?url={url}&output=json"
    http = urllib3.PoolManager()
    try:
        resp = http.request("GET", webArchiveSearchURL, retries=8)
    except:
        print("Well, there could no download happen for: ", webArchiveSearchURL)

    print("Downloading historic links")
    jsonArchive = json.loads(resp.data)
    return jsonArchive


def getDay(datestring):
    return datestring[:8]


def isSuccessfulRedirect(item):
    if (item[4] == "200"):
        return True

    return False


# Dafuq is JSON archive?
# What does this function do?

def getValidModelArchiveLinks(jsonArchive):
    """Receives a JSON with links and returns only links that are once a day!"""
    validJSONArchive = []
    tempList = []

    successful_redirect_list = [item for item in jsonArchive[1:] if isSuccessfulRedirect(item)]
    baseDay = getDay(successful_redirect_list[1][1])

    for index, item in enumerate(successful_redirect_list):
        print("list index:", index)

        if item not in tempList:
            print(item)
            if getDay(item[1]) == baseDay:
                tempList.append(item)
            else:
                baseDay = getDay(item[1])
                if len(tempList) <1:
                    validJSONArchive.append(item)
                else:
                    validJSONArchive.append(tempList[0])
                tempList = []
                tempList.append(item)

    return validJSONArchive