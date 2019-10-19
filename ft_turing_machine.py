class TuringMachine:
	name = ''
	alphabet = []
	blank = ''
	states = []
	initial = ''
	finals = []


def load_machine(filename):
	try:
		json_object = json.open(filename)
	except Exception as e:
		print("ERROR Loading File:", filename, " msg:",e)
		return False
	return json_object