#!/usr/bin/python

import json
import sys

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
    	#outputData.append({
    	#	"name": line[0],
    	#	"color": line[1],
    	#	"price": line[2],
    	#	"storage": line[3],
    	#	"rating": line[4],
    	#	"url": line[5]
    	#})
    	outputData.append(tempDict)

# Sort by prices without the "$" and as ints
outputData.sort(key=lambda s: float(s["price"][1:]))

# Output into file with given formatting
with open("output.json", "w") as outfile:
	outfile.write("[" + "\n")
	for i in range(len(outputData)):
		outfile.write("{\"name\":")
		for j in range(len(fieldnames)):
			outfile.write(json.dumps(outputData[i][fieldnames[j]]))
			if j < len(fieldnames)-1:
				outfile.write(", \"" + fieldnames[j+1] + "\":")
	#	outfile.write(json.dumps(outputData[index]["name"]))
	#	outfile.write(", \"color\":")
	#	outfile.write(json.dumps(outputData[index]["color"]))
	#	outfile.write(", \"price\":")
	#	outfile.write(json.dumps(outputData[index]["price"]))
	#	outfile.write(", \"storage\":")
	#	outfile.write(json.dumps(outputData[index]["storage"]))
	#	outfile.write(", \"rating\":")
	#	outfile.write(json.dumps(outputData[index]["rating"]))
	#	outfile.write(", \"url\":")
	#	outfile.write(json.dumps(outputData[index]["url"]))
		if i+1 == len(outputData):
			outfile.write("}")
		else: 
			outfile.write("},")
		outfile.write("\n")
	outfile.write("]")

























