# Learning, Plotting and Other Files
import criterion
import parse 
import learn

if __name__ == "__main__":
	X = parse.Normalize('/home/agiachris/CIBCData')
	data = X[:3000]
	extData = parse.Extract(data)
	n = criterion.Number(extData)
	print(n)
	learn.Learn(extData, n)