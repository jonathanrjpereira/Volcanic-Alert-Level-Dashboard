import requests
import matplotlib.pyplot as plt

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

# if len(volcanoID)==len(level):
#     print (volcanoID)
#     print (volcanoTitle)
#     print (level)
#     print (len(level))


top_volcanoID = volcanoID[0:3] + [volcanoID[8]] + [volcanoID[10]]
top_volcanoTitle = volcanoTitle[0:3] + [volcanoTitle[8]] + [volcanoTitle[10]]
top_level = level[0:3] + [level[8]] + [level[10]]
print(top_volcanoID)
print(top_volcanoTitle)
print(top_level)




def graph(volcanoTitle,level):
    #level = [5,0,3,1,4]
    yaxis = level
    xaxis = volcanoTitle

    shade = ['#E9DCEB','#DCC8E1','#D2B5D3','#AB65A4','#934A93','#832C82']

    plt.bar(xaxis, yaxis, align='center', alpha=0.5, color = [shade[level[0]],shade[level[1]],shade[level[2]],shade[level[3]],shade[level[4]]])
    plt.axis([-1, 5, 0, 6])    # X & Y axis Range
    plt.xlabel('VOLCANO')
    plt.ylabel('VOLCANIC ALERT LEVEL')
    plt.show()

if __name__ == '__main__':
    graph(top_volcanoTitle,top_level)
