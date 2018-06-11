import BikeParkNode
class AppClass():
    def __init__ (self, BikeParkNodeList):
        self.BikeParkNodeList=BikeParkNodeList

"""
Find the nearest parking node based on current location
"""
    def FindNearestNode (self, LAT, LONG):
        closestNode = self.BikeParkNodeList[0]
        for x in range(len(self.BikeParkNodeList)):
            if closestNode.computeDistance(LAT,LONG) > self.BikeParkNodeList[x].computeDistance(LAT,LONG):
                closestNode = self.BikeParkNodeList[x]
        return closestNode
            
  """
  Collect functions to build lists of the values in all the different categories such as location, address, racks, etc
  """
    def collectLocation (self) :
        locationList=[]
        for x in range(len(self.BikeParkNodeList)):
            locationList.append(self.BikeParkNodeList[x].location)
        return locationList


    def collectStreetName (self):
        streetList=[]
        for x in range(len(self.BikeParkNodeList)):
            streetList.append(self.BikeParkNodeList[x].street_name)
        return streetList


    def collectRacks (self):
        racksList=[]
        for x in range(len(self.BikeParkNodeList)):
            racksList.append(self.BikeParkNodeList[x].racks)
        return racksList


    def collectSpaces (self):
        spacesList=[]
        for x in range(len(self.BikeParkNodeList)):
            spacesList.append(self.BikeParkNodeList[x].spaces)
        return spacesList


    def collectYrInstalled (self):
        yrList=[]
        for x in range(len(self.BikeParkNodeList)):
            yrList.append(self.BikeParkNodeList[x].yr_installed)
        return yrList


    def collectAddress (self) :
        addressList=[]
        for x in range(len(self.BikeParkNodeList)):
            addressList.append(self.BikeParkNodeList[x].address)
        return addressList


    def collectMo (self):
        moList=[]
        for x in range(len(self.BikeParkNodeList)):
            moList.append(self.BikeParkNodeList[x].mo_installed)
        return moList


    def collectPlacement (self):
        placementList=[]
        for x in range(len(self.BikeParkNodeList)):
            placementList.append(self.BikeParkNodeList[x].placement)
        return placementList


    def collectLat (self):
        latList=[]
        for x in range(len(self.BikeParkNodeList)):
            latList.append(self.BikeParkNodeList[x].Lat)
        return latList


    def collectLong (self):
        longList=[]
        for x in range(len(self.BikeParkNodeList)):
            longList.append(self.BikeParkNodeList[x].Long)
        return longList
        
     



"""def main():
    Node1=BikeParkNode.BikeParkNode("a","b","c","d","e","f","g",6.4531,3.3958)
    Node2=BikeParkNode.BikeParkNode("a","b","c","d","e","f","g",40.7127,-74.0059)
    NodeList=[Node1,Node2]
    app=AppClass(NodeList)
    print len(app.BikeParkNodeList)
    print app.collectSpaces()
    print app.collectYrInstalled()
    print app.collectLocation()
    print app.collectStreetName()
    
    """
    

#main()
    




                       
                           
                           
