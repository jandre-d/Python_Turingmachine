# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing_machine.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: jandre-d <jandre-d@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 12:38:25 by jandre-d       #+#    #+#                 #
#    Updated: 2019/10/21 11:54:24 by jandre-d      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import ft_turing_output as out

#_machine_tape is a string
#_machine_desc is the loaded machine description
#_machine_state is a string

class _turing_machine():
	_machine_tape = None
	_machine_tape_len = None
	_machine_head_loc = None
	_machine_desc = None
	_machine_state = None

	def __init__(self, machine_desc):
		self._machine_desc = machine_desc

	def _setup(self, input):
		self._machine_tape = input
		self._machine_tape_len = len(input)
		self._machine_head_loc = 0
		self._machine_state = self._machine_desc['initial']
		out.print_machine(self._machine_desc)

	def _loop(self):
		while self._machine_state not in self._machine_desc['finals']:
			transition = self.__get_transition(self.__read())
			if not transition:
				break
			out.print_tape(self._machine_tape, self._machine_head_loc)
			out.print_transition(self._machine_state, transition['read'], \
				transition['to_state'], transition['write'], transition['action'])
			self._machine_state = transition['to_state']
			self.__write(transition['write'])
			self.__move(transition['action'])
		return self._machine_tape

	def __move(self, to):
		if to == 'LEFT':
			if self._machine_head_loc == 0:
				self._machine_tape_len += 1
				self._machine_tape = \
					self._machine_desc['blank'] + self._machine_tape
			else:
				self._machine_head_loc -= 1
		else:
			self._machine_head_loc += 1
			if self._machine_head_loc >= self._machine_tape_len:
				self._machine_tape_len += 1
				self._machine_tape = \
					self._machine_tape + self._machine_desc['blank']

	def __read(self):
		return self._machine_tape[self._machine_head_loc]

	def __write(self, char):
		self._machine_tape = \
			self._machine_tape[:self._machine_head_loc] + char + \
				self._machine_tape[self._machine_head_loc + 1:]

	def __get_transition(self, read):
		current_state_transitions = \
			self._machine_desc['transitions'][self._machine_state]
		for transition in current_state_transitions:
			if transition['read'] == read:
				return transition
		print('error: state transition for "{}" is not specified'.format(read))
		return False

	def execute(self, input):
		self._setup(input)
		return self._loop()

def run(machine_desc, input):
	x = _turing_machine(machine_desc)
	return x.execute(input)
