class ChanceCalculator:

    def __init__(self, known_persons, names):
        self.female_names = filter(lambda x: "tta" == x[-3:], names)
        self.male_names = filter(lambda x: "ss" == x[-2:], names)
        self.known_females = int(known_persons[1])
        self.known_males = int(known_persons[0])
        self.female_chance =\
            self.calculate_chance(self.known_females, self.female_names)
        self.male_chance =\
            self.calculate_chance(self.known_males, self.male_names)
        self.average_chance = self.female_chance * self.male_chance
        self.mistake_percentage = "{0}%".format(int(self.average_chance * 100))

    def calculate_chance(self, known_persons, names):
        unknown_persons = len(names) - known_persons
        if unknown_persons <= 0:
            unknown_persons = 1
        return 1.0 / unknown_persons
