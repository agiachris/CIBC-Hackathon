# Learning, Plotting and Other Files
import criterion
import parse 
import learn

if __name__ == "__main__":
	X = parse.Normalize('/home/agiachris/CIBCData')
	print (X)
	Data = X[:3000,[2, 6, 7]]
	n = criterion.Number(Data)
	learn.Learn(Data, n)