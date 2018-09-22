# Learning, Plotting and Other Files
import criterion
import parse 
import learn

if __name__ == "__main__":
	X = parse.Normalize('/home/agiachris/CIBCData')
	data = X[:3000]
	extData = parse.Extract(data)
	print(extData)
	n = criterion.Number(extData)
	learn.Learn(extData, n)