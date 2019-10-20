# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing_output.py                                :+:    :+:             #
#                                                      +:+                     #
#    By: jandre-d <jandre-d@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 15:37:01 by jandre-d       #+#    #+#                 #
#    Updated: 2019/10/20 21:10:55 by jandre-d      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def print_transition(state, read, to_state, write, action):
	print('({}, {}) -> ({}, {}, {})'.format(
		state, read, to_state, write, action))

def print_machine(machine_desc):
		print('*' * 80)
		print('*',' ' * 78, '*', sep = '')
		print('*{:^78}*'.format(machine_desc['name']))
		print('*',' ' * 78, '*', sep = '')
		print('*' * 80)
		for key in ('Alphabet', 'States', 'Initial', 'Finals'):
			print('{:8}: {}'.format(key, machine_desc[key.lower()]))
		for state in machine_desc['transitions']:
			for tran in machine_desc['transitions'][state]:
				print_transition(state, tran['read'],
					tran['to_state'], tran['write'], tran['action'])
		print('*' * 80)

def print_tape(machine_tape, machine_head_loc, end = ' '):
	print('[', machine_tape[:machine_head_loc],
	'<', machine_tape[machine_head_loc], '>',
		machine_tape[machine_head_loc + 1:], ']', end=end, sep='')
