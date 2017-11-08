import csv
import codecs
import os
import re
import itertools


def generateLanguages(language_codes, writer, tempRow, counter):
	letters = []
	for each in itertools.chain(*[itertools.product(map(chr, range(65,91)), repeat=i) for i in range(1, 5)]):
		letters.append(each);
	letters.pop(0);
	letters.pop(0);
	for i in range(len(language_codes) - 2):
		tempRow.append('=GOOGLETRANSLATE($B%s, B1, $%s$1)' %(counter, ''.join(letters[i])));
	writer.writerow(tempRow);


def main():
	print("Enter the XML filename with the extension")
	print("example: strings.xml ")
	inputFile = input();

	language_codes = ["", "en"]
	languageCodesFile = open("language_codes.txt","r");
	for line in languageCodesFile.readlines():
		language_codes.append(line.strip());

	languageCodesFile.close();


	#Make the root directory for the strings
	if not os.path.exists("translationsOutput"):
		os.makedirs("translationsOutput");

	#Open the XML file and create the writer from the file
	with codecs.open(inputFile, encoding="utf-8") as file:
		
		with codecs.open("translationsOutput/generatedCSV.csv", 'wb', encoding="utf-8") as outputFile:
			writer = csv.writer(outputFile);
			writer.writerow(language_codes);
			
			lines = file.readlines();
			counter = 1;

			for line in lines:
				tempRow = []
				stringName = re.search(r'"([^"]*)"', line);
				if(stringName != None):
					tempRow.append(stringName.group()[1:-1])
				stringText = re.search(r'>([^"]*)</', line);
				if(stringText != None):
					tempRow.append(stringText.group()[1:-2]);
					generateLanguages(language_codes, writer, tempRow, counter);
				counter += 1;
				 
	print("Done - Created generatedCSV.csv")
	print("Find the file in the translationsOutput folder")
main();