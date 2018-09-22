import csv
import numpy as np

def Normalize(dataPath):
    with open(dataPath+'/claims_final.csv') as dataSetFile:
        dataSet = csv.reader(dataSetFile, delimiter=',')
        dataMatrix = []
        for entry in dataSet:
            dataMatrix.append(entry)
        maxMatrix = [0] * 8
        minMatrix = [0] * 8
        for row in dataMatrix:
            row[7] = float(row[7])
            if row[7] < minMatrix[7]:
                minMatrix[7] = row[7]
            if row[7] > maxMatrix[7]:
                maxMatrix[7] = row[7]
        for row in dataMatrix:
            for i in range(0, 8):
                if i != 7:
                    continue
                row[i] = (row[i] - minMatrix[i])/(maxMatrix[i] - minMatrix[i])
    return dataMatrix

def Extract(data):
    extData = []
    for i in range(len(data)):
        extData.append([])
        extData[i].append(data[i][2])
        extData[i].append(data[i][6])
        extData[i].append(data[i][7])
    ext = np.r_[extData]
    print(ext)
    return ext
