import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import math
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--outFile', '-o', type=str, action='store', default ='Ibrahim_Dami_BME163_Assignment_Week4.png', help='output file')
parser.add_argument('--inFile', '-i', type=str, action='store', default ='BME163_source_file__assignment_4.txt', help='input file')

args = parser.parse_args()
plt.style.use('BME163.mplstyle')

inFile = open(args.inFile)
outFile = args.outFile
figureWidth =10
figureHeight = 3

plt.figure(figsize=(figureWidth, figureHeight))

panel1Width=5
panel1Height=2

panel1 = plt.axes([0.10,0.15,panel1Width/figureWidth, panel1Height/figureHeight])

xlabelDict = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[], '10':[], '>10':[] }

for line in inFile:
    splitLine = line.rstrip().split('\t')
    gene = splitLine[0].split('_')
    coverage = gene[3]
    if coverage in xlabelDict.keys():
        xlabelDict[coverage].append(float(splitLine[1]))
    elif int(coverage) > 10:
        xlabelDict['>10'].append(float(splitLine[1]))


def swarmplot(y, x, size):
    minDist = size / 72
    var = minDist / 5
    plottedList = []
    for yPos in y :
        plotted = False
        xPos = x
        if len(plottedList) == 0:
            plottedList.append((xPos, yPos))
            plotted = True
        else:
            closeList = []
            for i in plottedList:
                xVal = i[1] * (panel1Height/25)
                yVal = yPos * (panel1Height/25)
                if np.abs(xVal - yVal) <= minDist:
                    closeList.append(i)
            if len(closeList) == 0:
                plottedList.append((xPos, yPos))
                continue
            for shift in np.arange(0, 0.4, var):
                for val in [1, -1]:
                    if plotted == False:
                        shift *= val
                        xCoord = xPos + shift
                        distList = []
                        for j in closeList:
                            xDist = (abs(j[0] - xCoord) / 12) * panel1Width
                            yDist = (abs(j[1] - yPos) / 25) * panel1Height
                            dist= math.sqrt((xDist)**2 + (yDist)**2)
                            distList.append(dist)
                        if min(distList) > minDist:
                            plottedList.append((xCoord, yPos))
                            plotted = True

    for s, t in plottedList:
        panel1.plot(s, t, marker = 'o',
                    markerfacecolor = 'black',
                    markersize = size,
                    markeredgewidth = 0,
                    linewidth = 0
                    )
    if xPos != 11:
        print(1000 - len(plottedList), 'of points could not be plotted at position', xPos)
    else:
        print(1000-len(plottedList), 'of points could not be plotted at position >10')

for key, bins in zip(xlabelDict.keys(), range(1, 12)):
    randList = random.sample(xlabelDict[key], 1000)
    swarmplot(randList, bins, 1)

for n in range(1, 12):
    key = str(n)
    pos = n
    width = 0.4
    if key in xlabelDict.keys():
        median = np.median(xlabelDict[key])
    else:
        median = np.median(xlabelDict['>10'])
    panel1.plot([pos-width, pos+width],
                [median, median],
                linewidth = 0.75,
                color ='red'
                )

panel1.set_xlim(0, 12)
panel1.set_ylim(75, 100)
panel1.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
panel1.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '>10'])

panel1.set_xlabel('Subread Coverage')
panel1.set_ylabel('Identity (%)' , rotation = 90)
panel1.xaxis.label.set_size(12)
panel1.yaxis.label.set_size(12)

panel1.tick_params(bottom=True, labelbottom=True, left=True, labelleft=True,
                       right=False, labelright=False,
                       top=False, labeltop=False
                       )

plt.savefig(outFile, dpi = 600)
