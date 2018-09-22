import csv

def Normalize(dataPath, dataLen):
    with open(dataPath+'/claims_final.csv') as datasetFile:
        dataset = csv.reader(datasetFile, delimiter=',')
        dataMatrix = []
        count = 0
        for entry in dataset:
            dataMatrix.append(entry)
            if count == dataLen:
                break
        maxMatrix = [0] * 8
        minMatrix = [0] * 8
        for row in dataMatrix:
            for i in range(0, 8):
                if i != 7:
                    if i != 4:
                        row[i] = int(row[i])
                    continue
                if i == 7:
                    row[i] = float(row[i])
                if row[i] < minMatrix[i]:
                    minMatrix[i] = row[i]
                if row[i] > maxMatrix[i]:
                    maxMatrix[i] = row[i]
        for row in dataMatrix:
            for i in range(0, 8):
                if i != 7:
                    continue
                row[i] = (row[i] - minMatrix[i])/(maxMatrix[i] - minMatrix[i])
    return dataMatrix

def Trim(dataset):
    subset = []
    for i in range(0, len(dataset)):
        subset.append([])
        for j in range(0, 8):
            if j == 2:
                subset[i].append(dataset[i][j])
            elif j == 6:
                subset[i].append(dataset[i][j])
            elif j == 7:
                subset[i].append(dataset[i][j])
    return subset