'''
CSV to Markdown Converter
This converter pulls rows from a CSV table and turns them into individual .md files
Usage: python csvconverter.py filename.csv
'''

import csv
import sys

reader = csv.reader(open(sys.argv[1]))

csvname = (sys.argv[1])

filename = csvname[:-4]

headers = []
headerslen = 0

for index, row in enumerate(reader):
	if index == 0:
		headers = row
		headerslen = len(headers)
	else:
		mdfilename = filename + '_' + str(index) + '.md'
		fo = open(mdfilename, 'wb')
		fo.write('---\n')
		for i in range(0, headerslen):
			fo.write(headers[i].lower().replace(' ', '_') + ': \"' + row[i].strip() + '\"\n')
		fo.write('---')
		fo.close()

print "Conversion complete!"