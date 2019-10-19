import sys
import json

import ft_turing_machine

def __print_usage():
	print("""usage: ft_turing [-h] jsonfile input

positional arguments:
jsonfile			json description of the machine

input				input of the machine

optional arguments:
	-h,	--help		show this help message and exit""")

def __is_json(filename):
	try:
		json_object = json.open(filename)
	except:
		return False
	return True

def __check_arguments(argv):
	if len(argv) == 3:
		if not __is_json(argv[1]):
			return False
		return True
	else:
		__print_usage()
		return False

if __check_arguments(sys.argv) == True:
	print ("continue program")