import sys
import json

import ft_turing_input

def is_json(json_string):
	try:
		json_object = json.loads(json_string)
	except:
		return False
	return True

def load_machine_json(filename):

	return 0

def main(argv, argc):
	return 1


main(sys.argv, len(sys.argv))

print("Number of arguments", len(sys.argv))

print ('Arument list', sys.argv)

print ("second argument", sys.argv[1])


