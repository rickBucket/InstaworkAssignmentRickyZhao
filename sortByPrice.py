 #!/usr/bin/python

import json
import sys

# Sorting helper method via Merge Sort
def mSort(toSort):
	if len(toSort) <= 1:
		return toSort
	left = mSort(toSort[:len(toSort)//2])
	right = mSort(toSort[len(toSort)//2:])

	didSort = []
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		if float(left[i]["price"][1:]) < float(right[j]["price"][1:]):
			didSort.append(left[i])
			i += 1
		else:
			didSort.append(right[j])
			j += 1
	didSort += left[i:]
	didSort += right[j:]
	return didSort


# Alternative file name via command line
if (len(sys.argv) > 1):
	filename = sys.argv[1]
else:
	filename = "input.json"

outputData = []

# Read input file and add keys
with open(filename) as json_file:
    inputFile = json.load(json_file)
    for line in inputFile:
    	outputData.append({
     		"name": line[0],
     		"color": line[1],
     		"price": line[2],
     		"storage": line[3],
     		"rating": line[4],
     		"url": line[5]
     	})

# Sort by prices without the "$" and as floats to account for cents precision
outputData = mSort(outputData)

with open("output.json", "w") as outfile:
	json.dump(outputData, outfile, indent = 2)	




	
























