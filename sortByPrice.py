#!/usr/bin/python

import json
import sys


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

# Sort by prices without the "$" and as ints
outputData.sort(key=lambda s: float(s["price"][1:]))

# Output into file with given formatting
with open("output.json", "w") as outfile:
	outfile.write("[" + "\n")
	for index in range(len(outputData)):
		outfile.write("{\"name\":")
		outfile.write(json.dumps(outputData[index]["name"]))
		outfile.write(", \"color\":")
		outfile.write(json.dumps(outputData[index]["color"]))
		outfile.write(", \"price\":")
		outfile.write(json.dumps(outputData[index]["price"]))
		outfile.write(", \"storage\":")
		outfile.write(json.dumps(outputData[index]["storage"]))
		outfile.write(", \"rating\":")
		outfile.write(json.dumps(outputData[index]["rating"]))
		outfile.write(", \"url\":")
		outfile.write(json.dumps(outputData[index]["url"]))
		if index+1 == len(outputData):
			outfile.write("}")
		else: 
			outfile.write("},")
		outfile.write("\n")
	outfile.write("]")

























