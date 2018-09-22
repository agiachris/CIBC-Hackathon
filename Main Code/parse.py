import csv

def Normalize(DataPath):
    with open(DataPath+'/claims_final.csv') as DataSetFile:
        DataSet = csv.reader(DataSetFile, delimiter=',')
        DataMatrix = []
        for entry in DataSet:
            DataMatrix.append(entry)
        MaxMatrix = [0] * 8
        MinMatrix = [0] * 8
        for row in DataMatrix:
            for i in range(0, 8):
                if i != 7:
                    if i != 4:
                        row[i] = int(row[i])
                    continue
                if i == 7:
                    row[i] = float(row[i])
                if row[i] < MinMatrix[i]:
                    MinMatrix[i] = row[i]
                if row[i] > MaxMatrix[i]:
                    MaxMatrix[i] = row[i]
        for row in DataMatrix:
            for i in range(0, 8):
                if i != 7:
                    continue
                row[i] = (row[i] - MinMatrix[i])/(MaxMatrix[i] - MinMatrix[i])
    return DataMatrix

def Extract(Data):
    extData = []
    for i in range(len(Data)):
        extData.append([])
        for j in range(len(Data[0])):
            if j == 2:
                extData[i].append(Data[i][j])
            elif j == 6:
                extData[i].append(Data[i][j])
            elif j == 7:
                extData[i].append(Data[i][j])
    return extData