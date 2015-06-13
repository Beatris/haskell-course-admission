from chance_calculator import ChanceCalculator


while True:
    print "Input:"
    known_persons = raw_input().split()
    if known_persons == []:
        break
    names = raw_input().split()
    if names == []:
        break
    chance_calculator = ChanceCalculator(known_persons, set(names))
    print "Output:"
    print chance_calculator.mistake_percentage
    print '-' * 20
