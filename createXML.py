import codecs
import os 
import sys
import csv
from collections import defaultdict

def generateFiles(columns):
	stringNames = columns[""];
	for key in columns:
		if(key != ""):
			if not os.path.exists("translationsOutput/values-%s" %key):
				os.makedirs("translationsOutput/values-%s" %key);
			#Create the output file in the appropriate language folder.
			with codecs.open("translationsOutput/values-%s/strings.xml" %key, 'w', encoding="utf-8") as outputFile:
				#Write the start tag in the file.
				outputFile.write("<resources> \n");
				for i in range(len(columns[key])):
					outputFile.write('\t <string name=\"%s\">%s</string> \n' %(stringNames[i], columns[key][i]));
				#Write the closing tag in the file.
				outputFile.write("</resources>")

			print ('{:10s} {:3s}'.format(key, "Done"));


def main():
	print("Enter the CSV filename with the extension")
	print("example: translations.csv ")
	inputFile = input();

	#Make the root directory for the strings
	if not os.path.exists("translationsOutput"):
		os.makedirs("translationsOutput");

	#Open the csv file and create the reader from the file
	# with codecs.open(inputFile, encoding="utf-8") as file:
	with codecs.open(inputFile, encoding="utf-8") as file:
		columns = defaultdict(list)
		reader = csv.DictReader(file);
		for row in reader:
			for(key, value) in row.items():
				columns[key].append(value);
		

		generateFiles(columns) 
	print("translationsOuput folder will contain the new XML files");

main();