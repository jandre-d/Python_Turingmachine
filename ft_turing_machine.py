# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing_machine.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: jandre-d <jandre-d@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 12:38:25 by jandre-d       #+#    #+#                 #
#    Updated: 2019/10/20 15:37:18 by jandre-d      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import ft_turing_output as out

class _turing_machine():
	
	_machine_tape = None
	_machine_tape_len = None
	_machine_head_loc = None
	_machine_desc = None

	def __init__(self, machine_desc):
		self._machine_desc = machine_desc

	def run(self, input):
		self._machine_head_loc = 0
		self._machine_tape = input
		self._machine_tape_len = len(input)
		
		out.print_machine(self._machine_desc)
		return self._machine_tape

def run(machine_desc, input):
	x = _turing_machine(machine_desc)
	return x.run(input)
