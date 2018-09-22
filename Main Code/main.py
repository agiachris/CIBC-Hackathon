# Learning, Plotting and Other Files
import numpy as np
import criterion
import parse 
import learn
import rank

if __name__ == "__main__":

	X = parse.Normalize('/home/agiachris/CIBCData')				# Return Dicitonary with States as Keys and databases and values
	stored_data = []
	for key in X.keys():										# iterate over datasets
		print(key)
		currData = X[key]
		currData = currData[:100]								# Number of data points to splice
		stored_data += currData
		extData = parse.Extract(currData)						# Extract required data (doctor type, price)
		#n = criterion.Number(extData)							# Figuring out the best posibble criterion
		if key == 'NY':
			score_records = learn.Learn(extData, 50, key)									# Cluster, plot, and store
		else:
			score_records = np.r_[score_records, (learn.Learn(extData, 50, key))]			# Cluster, plot, and store

	sorted_data = rank.Sort(score_records, stored_data)
	rank.File1(sorted_data)
	rank.File2(sorted_data)