class ChanceCalculator:

	def __init__(self, known_persons, names):
		self.female_names = filter(lambda x: "tta" == x[-3:], names)
		self.male_names = filter(lambda x: "ss" == x[-2:], names)
		self.known_females = int(known_persons[1])
		self.known_males = int(known_persons[0])
		self.mistake_percentage = "{0}%".format(int(self.calculate_chance() * 100))

	def calculate_chance(self):
		pass