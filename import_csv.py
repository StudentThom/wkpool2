# import  matches from csv

import csv
import helpers

matches = {}

with open('uitslagen.csv',newline='') as csvfile:
	reader1 = csv.reader(csvfile, delimiter = ',', quotechar=' ')
	i = 0
	for row in reader1:
		if i != 0:
			print(', '.join(row))
			key = row[2] + row[3]
			value = helpers.match(row[2],row[3])
			matches[key] =  value
			# give result of match
			score = row[4]
			#print("score" + score, sep = ' ')
			if score != "":
				score1 = score[0]
				if len(score) == 3:
					score2 = score[2]
				elif len(score) == 5:
					score2 = score[4]
				else:
					print("Error while reading score (proably because of length in input csv)")
				print(score1,score2,sep=' ')
				if row[5] == "X" or row[5] == "x":
					goal_last_15_minutes = True
				else:
					goal_last_15_minutes = False
				# add result to match
				matches[key].give_result([score1,score2],goal_last_15_minutes)
		else:
			i += 1

###############################################################################
# Input predictions
###############################################################################

persons = {}
def read_person(person_csv_file):
	with open(person_csv_file,newline='') as csvfile:
		# read person's name from filename (delete '.csv')
		naam = person_csv_file[15:-4]
		persons[naam] = helpers.person(naam)
		reader1 = csv.reader(csvfile, delimiter = ',', quotechar=' ')
		i = 0
		for row in reader1:
			if i != 0:
				print(', '.join(row))
				key = row[2] + row[3]
				match = matches[key]
				score = row[4]
				if score != "":
					score1 = score[0]
					if len(score) == 3:
						score2 = score[2]
					elif len(score) == 5:
						score2 = score[4]
					else:
						print("Error while reading score (proably because of length in input csv)")
					print(score1,score2,sep=' ')
					if row[5] == "X" or row[5] == "x":
						goal_last_15_minutes = True
					else:
						goal_last_15_minutes = False
					voorspelling1 = helpers.voorspelling(match,persons[naam] ,[score1,score2], goal_last_15_minutes)
					persons[naam].add_voorspelling(voorspelling1)
		
			else:
				i += 1
	
