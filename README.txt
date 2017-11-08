This revision of the code does not work with documents that have anything in the XML file other than the strings. Make sure there are no comments or extra text. A sample XML file is supplied for reference on how to format your XML. Any other format of XML can not be guaranteed to work in this revision of the code. 


##To use:
In python 3, run createCSV and type the name of the XML document with the extension.
eg. strings.xml

This will create a folder (translationsOutput) and within that, a CSV file (generatedCSV) will be created. 
Open that CSV file in Google Spreadsheets and wait for that to load, it may take a while depending on the amount of strings in your initial XML file.

Once the spreadsheet is done loading, save it as CSV file in the same folder as your python scripts. 
File -> Download as -> Comma-separated values (.csv, current sheet)

Then in python, run createXML and type the name of the new CSV file. 
eg. generatedCSV - generatedCSV.csv

This will create a series of folders inside the translationsOutput folder, each containing the XML file with the tranlated strings. 

These folders can be imported into Android Studio and used in your application.


I have only tested on Windows and Linux computers, both using Python 3. Not sure if works on MacOS


If you would like for less than the 104 default langauges, the language codes can be removed from the language_codes.txt file. 
A full reference of the codes/languages can be found here: https://cloud.google.com/translate/docs/languages

A video Tutorial can be found here:
[Video Tutorial](https://youtu.be/s1QJnglyvFA)
