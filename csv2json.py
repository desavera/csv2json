import csv
import json

input_file = open('input.csv', 'r')
output_file = open('output.json', 'w')

fieldnames = ("category","product","userId","eventTime","eventType")
reader = csv.DictReader( input_file, fieldnames)
out = json.dumps( [ row for row in reader ] )
ouput_file.write(out)
