import readBikeData 
import PlotData
import pieChart
import mapTest
#import histoPlot


def main():
    #gather data into lists
    dataList=readBikeData.GatherData('rows.json')
    BikeObjsList=readBikeData.MakeDataObjs(dataList)
    app=readBikeData.MakeAppObj(BikeObjsList)
    RackList=app.collectRacks()
    SpaceList=app.collectSpaces()
    StreetList=app.collectStreetName()
    YrList=app.collectYrInstalled()
    LocationList=app.collectLocation()
    AddressList=app.collectAddress()
    MoList=app.collectMo()
    PlacementList=app.collectPlacement()
    LatList=app.collectLat()
    LongList=app.collectLong()
    print LatList[:10]
    print LongList[:10]

    
    
    #observation: racks are usually half the number of spaces
   # PlotData.ScatterPlot(RackList,SpaceList, "Racks", "Spaces")
    
    #market street has majority of the street spaces
   # pieChart.makePieChart(dataList)

    #
    #histoPlot.makeDataHist(dataList)

    #
    coordinateList=[]
    for i in range(len(LatList)):
        coordinateList.append([LatList[i],LongList[i]])
    mapTest.makeDataMap(coordinateList)
    #print (coordinateList[2519])
    #print (coordinateList[2518])
    #print (coordinateList[2517])
    

main()
    
   
