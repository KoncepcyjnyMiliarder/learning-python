possible_moves = ['r', 'p', 's']
winning_moves = [['r', 's'], ['s', 'p'], ['p', 'r']]
round_count = 4

for i in range(round_count):
	player_a_move = ''
	player_b_move = ''

	while player_a_move not in possible_moves:
		player_a_move = input("Player A, rock(r), paper(p) or scissors(s)?")
	while player_b_move not in possible_moves:
        	player_b_move = input("Player B, rock(r), paper(p) or scissors(s)?")

	if [player_a_move, player_b_move] in winning_moves:
		print("Player A won this round!")
	elif [player_b_move, player_a_move] in winning_moves:
		print("Player B won this round!")
	else:
		print("That's a draw!")

print("Game over!")
