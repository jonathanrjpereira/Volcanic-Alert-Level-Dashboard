import requests

r = requests.get('https://api.geonet.org.nz/volcano/val')
data = r.json()
#print(data)

feature = data['features']
#print (feature)

volcano = []
level = []

for result in feature:
    properties = result['properties']
    volcano.append(properties['volcanoID'])
    level.append(properties['level'])
    #print(properties['volcanoID'])

if len(volcano)==len(level):
    print (volcano)
    print (level)
