import parse
import numpy as np
import matplotlib.pyplot as plt
DataMatrix = parse.Normalize()
PriceColumn = []
DoctorIdColumn = []
Count = 0
for row in DataMatrix:
    Count += 1
    PriceColumn.append(row[7])
    DoctorIdColumn.append(row[2])
    if Count == 100000:
        break
plt.plot(DoctorIdColumn, PriceColumn, 'ro')
plt.show()