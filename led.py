import requests

def getData():
    r = requests.get('https://api.geonet.org.nz/volcano/val')
    data = r.json()
    #print(data)

    feature = data['features']
    #print (feature)

    volcanoID = []
    volcanoTitle = []
    level = []

    for result in feature:
        properties = result['properties']

        volcanoID.append(properties['volcanoID'])
        volcanoTitle.append(properties['volcanoTitle'])
        level.append(properties['level'])

    if len(volcanoID)==len(level):
        # print (volcanoID)
        # print (volcanoTitle)
        # print (level)
        return volcanoID , volcanoTitle , level

def topVolcano():
    volcanoID, volcanoTitle, level = getData()
    top_volcanoID = volcanoID[0:3] + [volcanoID[8]] + [volcanoID[10]]
    top_volcanoTitle = volcanoTitle[0:3] + [volcanoTitle[8]] + [volcanoTitle[10]]
    top_level = level[0:3] + [level[8]] + [level[10]]
    #print(top_volcanoID)
    #print(top_volcanoTitle)
    #print(top_level)
    return top_volcanoID, top_level

if __name__ == '__main__':
    volcano, level = topVolcano()
    print(volcano)
    print(level)
