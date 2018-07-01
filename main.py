# main.py

import helpers
import import_csv
import csv
import os


matches = import_csv.matches

for filename in os.listdir('voorspellingen'):
	print(filename)
	import_csv.read_person('voorspellingen/'+filename)

persons = import_csv.persons

# write to csv
with open('tussenstand.csv', 'w', newline='') as csvfile:
	writer1 = csv.writer(csvfile, delimiter = ',', quotechar = ' ')
	for person in persons:
		persons[person].give_score()
		writer1.writerow([persons[person].name] + [round(persons[person].points)]) 	
