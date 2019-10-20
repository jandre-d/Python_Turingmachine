# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: jandre-d <jandre-d@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 12:38:20 by jandre-d       #+#    #+#                 #
#    Updated: 2019/10/20 14:17:37 by jandre-d      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
import json
import argparse

import ft_turing_machine as machine
import ft_turing_machine_validate as check

def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('jsonfile', help = 'json description of the machine')
	parser.add_argument('input', help = 'input of the machine')
	return parser.parse_args()

def main(arg):
	machine_desc = None
	try:
		file = open(arg.jsonfile)
		machine_desc = json.load(file)
	except Exception as e:
		print('can\'t load file: "', arg.jsonfile, '" exeption msg: "', e, '"')
		sys.exit(1)
	if machine_desc:
		if check.machine(machine_desc) and check.input(arg.input, machine_desc):
			machine.run(machine_desc, arg.input)

main(arguments())
