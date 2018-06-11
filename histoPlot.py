##Make Histogram of Bike racks made over the years
import readBikeData
import matplotlib.pyplot as plt
def makeDataHist(bigList):
    yearList = []
    #bigList = readBikeData.GatherData('rows.json')
    for i in range(len(bigList)):
        year = bigList[i][15]
        racks = int(bigList[i][11])
        if('UK' != year):
            for x in range(racks):
                yearList.append(int(year))




    plt.hist(sorted(yearList))
    plt.title("Bike Rack Construction Histogram")
    plt.xlabel("Year")
    plt.ylabel("# of Racks Built")
    plt.show()
