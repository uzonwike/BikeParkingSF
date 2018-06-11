import pygmaps
import webbrowser
import readBikeData
# MAKE SURE COORDINATE LIST IS FORMATTED LIKE [[Lat1, Long1], [Lat2, Long2], ..., [LatN, LongN]] AL
# ALSO COLOR IS STRING LIKE "#0000FFF"
def makeDataMap(coordinateList):
    
    #bigList = readBikeData.GatherData('rows.json')
    
    #DONT CHANGE FOLLOWING LINE
    mymap = pygmaps.maps(37.7749295, -122.4194155, 13)
    for i in range(len(coordinateList)):
        mymap.addpoint(coordinateList[i][0], coordinateList[i][1], "#FF0000")
    mymap.draw('mymap.draw.html')
    url = 'mymap.draw.html'
    webbrowser.open_new_tab(url)

