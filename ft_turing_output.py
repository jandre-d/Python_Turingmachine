# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing_output.py                                :+:    :+:             #
#                                                      +:+                     #
#    By: jandre-d <jandre-d@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 15:37:01 by jandre-d       #+#    #+#                 #
#    Updated: 2019/10/20 15:37:13 by jandre-d      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def _print_transition(state, read, to_state, write, action):
	print('({}, {}) -> ({}, {}, {})'.format(
		state, read, to_state, write, action))

def print_machine(machine_desc):
		print('*' * 80)
		print('*',' ' * 78, '*', sep = '')
		print('*{:^78}*'.format(machine_desc["name"]))
		print('*',' ' * 78, '*', sep = '')
		print('*' * 80)
		for key in ('Alphabet', 'States', 'Initial', 'Finals'):
			print('{:8}: {}'.format(key, machine_desc[key.lower()])
				.replace("'", ''))
		for state in machine_desc["transitions"]:
			for tran in machine_desc["transitions"][state]:
				_print_transition(state, tran["read"],
					tran["to_state"], tran["write"], tran["action"])
		print('*' * 80)
