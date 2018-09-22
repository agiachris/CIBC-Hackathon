# Learning, Plotting and Other Files
import criterion
import parse 
import learn

if __name__ == "__main__":

	X = parse.Normalize('/home/agiachris/CIBCData')				# Return Dicitonary with States as Keys and databases and values

	for key in X.keys():										# iterate over datasets
		print(key)
		currData = X[key]
		currData = currData[:100000]
		extData = parse.Extract(currData)						# Extract required data (doctor type, price)
		n = criterion.Number(extData)							# Figuring out the best posibble criterion
		print(n)
		learn.Learn(extData, 50)								# Cluster and plot