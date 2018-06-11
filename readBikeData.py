#import json information MAKE SURE FILENAME IS CORRECT

import json
import BikeParkNode
import appClass
#import unicode

def GatherData(json1):
    from pprint import pprint
    with open(json1) as file:
        jsonDict = json.load(file)
    bigList = jsonDict['data']
    #Index to Latitude bigList[i][16][1]
    #Index to Longitude bigList[i][16][2]
    #Index to Address bigList[i][8]
    #Index to Location Name bigList[i][9]
    #Index to Street Name bigList[i][10]
    #Index to # of Racks bigList[i][11]
    #Index to # of Spaces bigList[i][12]
    #Index to Placement bigList[i][13]
    #Index to Month Installed bigList[i][14]
    #Index to Year installed bigList[i][15]
    print type(bigList[10][16][1])
    x=(bigList[10][16][1])
    #print type(x.encode('ascii','ignore'))
    y=x.encode('ascii','ignore')
    print ('y',float(y))
    
    return bigList

##########################################################################

def MakeDataObjs(bigList):
    bikeParkList = []
    for i in range(len(bigList)):
        bikeParkObject = BikeParkNode.BikeParkNode(bigList[i][8],bigList[i][9],bigList[i][10],bigList[i][11],bigList[i][12], bigList[i][13], bigList[i][14], bigList[i][15], float(bigList[i][16][1]), float(bigList[i][16][2]))
        bikeParkList.append(bikeParkObject)
    print bikeParkList[10].Lat
    return bikeParkList
    

def MakeAppObj(bikeParkList):
    app=appClass.AppClass(bikeParkList)
    return app
    

