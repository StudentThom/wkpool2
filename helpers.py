# class definitions

class match:
	
	score1 = -1 
	score2 = -1	
	winner = -1
	goal_last_15_minutes = -1

	def __init__(self, team1, team2):
		self.team1 = team1
		self.team2 = team2

	def give_result(self, score, goal_last_15_minutes):
		self.score1 = score[0]
		self.score2 = score[1]
		self.goal_last_15_minutes = goal_last_15_minutes
		
		if self.score1 == self.score2:
			self.winner = "gelijk"
		elif self.score1 > self.score2:
			self.winner = self.team1
		elif self.score2 > self.score1:
			self.winner = self.team2

class voorspelling:
	
	def __init__(self, match, person, score, goal_last_15_minutes):
		self.match = match
		self.person = person
		self.score1 = score[0]
		self.score2 = score[1]
		self.goal_last_15_minutes = goal_last_15_minutes

		self.points_winner = 0
		self.points_15 = 0
		self.points_goals = 0
		self.points_total = 0

		if self.score1 == self.score2:
			self.winner = "gelijk"
		elif self.score1 > self.score2:
			self.winner = self.match.team1
		elif self.score2 > self.score1:
			self.winner = self.match.team2

	def check_voorspelling(self):
		if self.match.winner == self.winner:
			self.points_winner= 2
		if self.match.goal_last_15_minutes == self.goal_last_15_minutes == True:
			self.points_15 = 1
		if (self.match.score1 == self.score1) & (self.match.score2 == self.score2):
			self.points_goals = 1
		
		# total points
		self.points_total= self.points_winner + self.points_15 + self.points_goals
		# double points when belgium is playing
		if self.match.team1 == "BELGIË" or self.match.team1 == "BELGIË":
			self.points_total *= 2
		

class person:

	def __init__(self, name):
		self.name = name
		self.points = 0
		self.voorspellingen = []
		
	def __str__(self):
		return self.name + " heeft " + str(round(self.points)) + " punten"

	def add_voorspelling(self,voorspelling):
		if self.name != voorspelling.person.name:
			print("Error adding voorspelling")
			return("Error adding voorspelling")

		self.voorspellingen.append(voorspelling)

	def give_score(self):
		self.points = 0
		for voorspelling in self.voorspellingen:
			voorspelling.check_voorspelling()
			self.points += voorspelling.points_total
		return self.points

