
"""import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def BarChart(allVal, xtick, colors, xlabel, ylabel):
    n_groups=len(allVal[0])
    for i in range(len(allVal)):
        if n_groups>len(allVal[i]):
            n_groups=len(allVal[i])
    

   
    std_men = (2, 3, 4, 1, 2)

    
    std_women = (3, 5, 2, 3, 3)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rectList=[0]*len(allVal)
    for h in range(len(allVal)):
        
        for i in index:
            allVal[h][i]=float(allVal[0][i])
            allVal[h][i]=float(allVal[1][i])

    for h in range(len(allVal)):
        rectList[h]=plt.bar(index+(bar_width*h), tuple(allVal[h]), bar_width,
                     alpha=opacity,
                     color=colors[h],
                     yerr=std_men,
                     error_kw=error_config,
                     label='Men')

    
        



    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Scores by group and gender')
    plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))
    plt.legend()

    plt.tight_layout()
    plt.show()
#def CreateBar


def LinePlot(xval, yval, labelx, labely, graphTitle):
    plot(xval,yval)
    xlabel(labelx)
    ylabel(labely)
    title(graphTitle)
    grid(True)
    show()


def ScatterPlot(xval, yval, labelx, labely):

    N = min([len(xval),len(yval)])
    #x = np.random.rand(N)
    #y = np.random.rand(N)
    colors = np.random.rand(N)
    #area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
    area=([np.pi*25]*N)

    plt.scatter(xval, yval, s=area, c=colors, alpha=0.5)
    plt.xlabel(labelx)
    plt.xlabel(labely)
    plt.show()
    

#def PlotPieChart(node):

#def ComputePossiblePermutations(DataList):
    






    """
def BarChart(allVals, xtick):
std_men = (2, 3, 4, 1, 2)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()
minindex=len(allVal[0])

for i in range(len(allVal)):
    if minindex<len(allval[i]):
        minindex=len(allVal[i])
    
bar_width = 0.35
opacity = 0.4
error_config = {'ecolor': '0.3'}

rectList=[]
for i in range(len(minindex)):
    rect=plt.bar(index, xval, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_men,
                 error_kw=error_config,
                 label='Men')
    rectList.append(rect)


plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width, xticks)
plt.legend()

plt.tight_layout()
plt.show()
"""


    
    
