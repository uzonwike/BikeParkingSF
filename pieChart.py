## Make pie chart using street name and percent of space that each street's storage space takes up in SF
## Takes in the bigList from the GatherData function
import matplotlib.pyplot as plt
import readBikeData

def makePieChart(bigList):
    streetNameList = []
    bikeSpaceList = []
    x = 0
    ##bigList = readBikeData.GatherData('rows.json')
    for i in range(len(bigList)):
        streetName = bigList[i][10].lower()
        bikeSpaceInt = int(bigList[i][12])
        if streetName in streetNameList:
            ndx = streetNameList.index(streetName)
            bikeSpaceList[ndx] += bikeSpaceInt
        else:
            streetNameList.append(streetName)
            bikeSpaceList.append(bikeSpaceInt)
    bikeSpaceSum = sum(bikeSpaceList)

    ##I omited any area that was less then 1% of the total bike space to get a cleaner pie chart
    while x < len(bikeSpaceList):
        if(bikeSpaceList[x] < (bikeSpaceSum * .01) and x >= 0):
            del bikeSpaceList[x]
            del streetNameList[x]
            x-=1

        else:
            x+=1

    plt.axis("equal")
    plt.pie(bikeSpaceList, labels = streetNameList, autopct = "%1.1f%%", shadow = False)
    plt.title("Bike Space to Street Name Distribution")
    plt.show()


        
        
    
    
