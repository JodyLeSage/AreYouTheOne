# ayto.py
# author: Jody LeSage, 2019

from itertools import combinations	# used for combinatorics

def main():
	return


def getProbabilities():
	players = getPlayers
	booths = getTruthBooths

	# generate the 120 possible couple combinations
	couples = list(combinations(players, 2))


def getPlayers():
	players = {
		"AASHA",
		"AMBER",
		"BASIT",
		"BRANDON",
		"DANNY",
		"JASMINE",
		"JENNA",
		"JONATHAN",
		"JUSTIN",
		"KAI",
		"KARI",
		"KYLIE",
		"MAX",
		"NOUR",
		"PAIGE",
		"REMY"
	}
	return players


def getTruthBooths():
	truthBooths = {
		("JUSTIN", "NOUR") : False,
		("BRANDON", "REMY") : False,
		("JENNA", "KAI") : False,
		("DANNY", "JENNA") : False,
		("KARI", "KYLIE") : False
	}
	return truthBooths
	# return {}


def getMatchingCeremonies():
	ceremony1 = {
		("AASHA", "PAIGE"),
		("AMBER", "NOUR"),
		("BASIT", "JONATHAN"),
		("BRANDON", "REMY"),
		("DANNY", "KAI"),
		("JASMINE", "JENNA"),
		("JUSTIN", "MAX"),
		("KARI", "KYLIE")
	}

	ceremony2 = {
		("AASHA", "BRANDON"),
		("AMBER", "NOUR"),
		("BASIT", "JONATHAN"),
		("DANNY", "REMY"),
		("JASMINE", "JUSTIN"),
		("JENNA", "KAI"),
		("KARI", "KYLIE"),
		("MAX", "PAIGE")
	}

	ceremony3 = {
		("AASHA", "MAX"),
		("AMBER", "PAIGE"),
		("BASIT", "REMY"),
		("BRANDON", "JONATHAN"),
		("DANNY", "KAI"),
		("JASMINE", "NOUR"),
		("JENNA", "JUSTIN"),
		("KARI", "KYLIE")
	}

	ceremony4 = {
		("AASHA", "REMY"),
		("AMBER", "NOUR"),
		("BASIT", "DANNY"),
		("BRANDON", "JASMINE"),
		("JENNA", "PAIGE"),
		("JONATHAN", "KYLIE"),
		("JUSTIN", "MAX"),
		("KAI", "KARI")
	}

	ceremony5 = {
		("AASHA", "KAI"),
		("AMBER", "NOUR"),
		("BASIT", "REMY"),
		("BRANDON", "MAX"),
		("DANNY", "KARI"),
		("JASMINE", "PAIGE"),
		("JENNA", "KYLIE"),
		("JONATHAN", "JUSTIN")
	}

	allCeremonies = {
		# ceremony1 : 2
		ceremony1 : 2,
		ceremony2 : 2,
		ceremony3 : 2,
		ceremony4 : 1,
		ceremony5 : 0
	}

	return allCeremonies


if __name__== "__main__":
  main()