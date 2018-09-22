import parse
import pandas as pd
import numpy as np

def Sort(scores, data):
    # Append scores to dataset
    for i in range(len(data)):
        data[i].append(scores[i])

    for iter_num in range(len(data) - 1, 0, -1):
        for idx in range(iter_num):
            if data[idx][8] > data[idx + 1][8]:
                temp = data[idx]
                data[idx] = data[idx + 1]
                data[idx + 1] = temp

    return data

def File1(sorted):
    provider_info = parse.F1(sorted)
    df = pd.DataFrame(provider_info)
    df.to_csv("/home/agiachris/Desktop/file1.csv")

def File2(sorted):
    dict = {}
    for i in range(len(sorted)):
        if sorted[i][2] not in dict.keys():
            dict[sorted[i][2]] = []
            dict[sorted[i][2]].append(sorted[i])
        else:
            dict[sorted[i][2]].append(sorted[i])

    extracted = []
    for key in dict.keys():
        for i in range(1):
            extracted.append(dict[key][i])

    info = parse.F2(extracted)
    print(info)
    df = pd.DataFrame(info)
    df.to_csv("/home/agiachris/Desktop/file2.csv")