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



# List of property names in their order
fieldnames = ["name", "color", "price", "storage", "rating", "url"]

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
    	tempDict = {}
    	for i in range(len(fieldnames)):
    		tempDict[fieldnames[i]] = line[i]

    	outputData.append(tempDict)

# Sort by prices without the "$" and as ints
outputData = mSort(outputData)


# Output into file with given formatting
with open("output.json", "w") as outfile:
	outfile.write("[" + "\n")
	for i in range(len(outputData)):
		outfile.write("{\"name\":")
		for j in range(len(fieldnames)):
			outfile.write(json.dumps(outputData[i][fieldnames[j]]))
			if j < len(fieldnames)-1:
				outfile.write(", \"" + fieldnames[j+1] + "\":")
		if i+1 == len(outputData):
			outfile.write("}")
		else: 
			outfile.write("},")
		outfile.write("\n")
	outfile.write("]")




	
























