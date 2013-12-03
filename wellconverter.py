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

filelower = filename.lower()

headers = []
headerslen = 0

coordinates = []

exclude_fields = [
	'Site Summary',
	'Download Data',
	'Longitude',
	'Additional Information'
]

for index, row in enumerate(reader):
	if index == 0:
		headers = row
		headerslen = len(headers)
	else:
		wellname = row[3].lower()
		coordinates.append(row[5])
		coordinates.append(row[4])
		mdfilename = filelower + '_' + str(index) + '.md'
		fo = open(mdfilename, 'wb')
		fo.write('---\n' + 'layout: well\n' + 'facility_url: facilities/' + filelower + '\n' + 'facility_class: ' + filelower + '\n' + 'permalink: facilities/' + filelower + '/' + wellname + '\n')
		for i in range(0, 11):
			if headers[i] == 'Well Name':
				fo.write('title: \"' + row[i].strip() + '\"\n')
			elif headers[i] == ('Latitude'):
				fo.write('coordinates: [\n\t' + coordinates[0] + ',\n\t' + coordinates[1] + '\n]\n')
			elif headers[i] not in exclude_fields:
				fo.write(headers[i].lower().replace(' ', '_') + ': \"' + row[i].strip() + '\"\n')

		fo.write('pollutants: [\n  {\n')

		for i in range(11, 18):
			if headers[i].startswith('Drinking Water Health Standards Exceeded'):
				if row[i].startswith('Thallium'):
					fo.write('\ttype: "Tl",\n')
				fo.write('\tname: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Health Based Standard Exceeded'):
				fo.write('\thealth_base_standard_exceeded: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times in Exceedance'):
				fo.write('\tnumber_of_times_in_exceedance: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times Monitored'):
				fo.write('\tnumber_of_times_monitored: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Exceedance Amount'):
				fo.write('\tmax_exceedance_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Allowable Amount'):
				fo.write('\tmax_allowable_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Unit of Measurement'):
				fo.write('\tunit_of_measurement: \"' + row[i].strip() + '\"\n')

		fo.write('  },\n  {\n')

		for i in range(18, 25):
			if headers[i].startswith('Drinking Water Health Standards Exceeded'):
				if row[i].startswith('Thallium'):
					fo.write('\ttype: "Tl",\n')
				fo.write('\tname: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Health Based Standard Exceeded'):
				fo.write('\thealth_base_standard_exceeded: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times in Exceedance'):
				fo.write('\tnumber_of_times_in_exceedance: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times Monitored'):
				fo.write('\tnumber_of_times_monitored: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Exceedance Amount'):
				fo.write('\tmax_exceedance_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Allowable Amount'):
				fo.write('\tmax_allowable_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Unit of Measurement'):
				fo.write('\tunit_of_measurement: \"' + row[i].strip() + '\"\n')

		fo.write('  },\n  {\n')

		for i in range(25, 32):
			if headers[i].startswith('Drinking Water Health Standards Exceeded'):
				if row[i].startswith('Thallium'):
					fo.write('\ttype: "Tl",\n')
				fo.write('\tname: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Health Based Standard Exceeded'):
				fo.write('\thealth_base_standard_exceeded: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times in Exceedance'):
				fo.write('\tnumber_of_times_in_exceedance: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times Monitored'):
				fo.write('\tnumber_of_times_monitored: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Exceedance Amount'):
				fo.write('\tmax_exceedance_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Allowable Amount'):
				fo.write('\tmax_allowable_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Unit of Measurement'):
				fo.write('\tunit_of_measurement: \"' + row[i].strip() + '\"\n')
		
		fo.write('  },\n  {\n')

		for i in range(32, headerslen):
			if headers[i].startswith('Drinking Water Health Standards Exceeded'):
				if row[i].startswith('Thallium'):
					fo.write('\ttype: "Tl",\n')
				fo.write('\tname: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Health Based Standard Exceeded'):
				fo.write('\thealth_base_standard_exceeded: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times in Exceedance'):
				fo.write('\tnumber_of_times_in_exceedance: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Number of Times Monitored'):
				fo.write('\tnumber_of_times_monitored: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Exceedance Amount'):
				fo.write('\tmax_exceedance_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Max. Allowable Amount'):
				fo.write('\tmax_allowable_amount: \"' + row[i].strip() + '\",\n')
			elif headers[i].startswith('Unit of Measurement'):
				fo.write('\tunit_of_measurement: \"' + row[i].strip() + '\"\n')

		fo.write('  }\n]\n')
		fo.write('---')
		fo.close()

print "Conversion complete!"