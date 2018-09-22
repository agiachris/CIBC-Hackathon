# Learning, Plotting and Other Files
import criterion
import parse 
import learn

if __name__ == "__main__":

	X = parse.Normalize('/home/agiachris/CIBCData')				# Return Dicitonary with States as Keys and databases and values
	
	for key in X.keys():										# iterate over datasets
		currData = X[key]
		extData = parse.Extract(currData)						# Extract required data (doctor type, price)
		n = criterion.Number(extData)							# Figuring out the best posibble criterion
		learn.Learn(extData, n)									# Cluster and plot