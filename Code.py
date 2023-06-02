import random #for generating random numbers

transition_matrix = { #dictionary represents the probabilities of transitioning from one state to another in the game
	'rock': {'rock': 0.2, 'paper': 0.5, 'scissor': 0.3}, #these are the probability of transitioning matrix to next possible state
	'paper': {'rock': 0.3, 'paper': 0.2, 'scissor': 0.5},
	'scissor': {'rock': 0.5, 'paper': 0.3, 'scissor': 0.2}
}

hidden_states = ['rock', 'paper', 'scissor']
observed_states = ['rock', 'paper', 'scissor']

transition_probabilities = [
	[0.2, 0.5, 0.3],
	[0.3, 0.2, 0.5],
	[0.5, 0.3, 0.2]
]

emission_probabilities = [
	[0.33, 0.33, 0.33],
	[0.33, 0.33, 0.33],
	[0.33, 0.33, 0.33]
]

initial_probabilities = [0.33, 0.33, 0.33] #it represents the probability of hidden states ith to ith elements

def markov_chain(previous_action):
	probabilities = transition_matrix[previous_action]
	return random.choices(list(probabilities.keys()), weights=list(probabilities.values()))[0]

def hmm(previous_action, current_action):
   
	previous_state_index = hidden_states.index(previous_action)
	current_state_index = hidden_states.index(current_action)
	previous_probability = [initial_probabilities[i] * emission_probabilities[i][previous_state_index] for i in range(3)]
	current_probability = [sum([previous_probability[i] * transition_probabilities[i][j] for i in range(3)]) for j in range(3)]

# update emission probabilities based on the result of the game
	if current_action == previous_action:
    	# tie
    	for i in range(3):
        	if i == current_state_index:
            	emission_probabilities[i][i] += 0.1
        	else:
            	emission_probabilities[i][i] -= 0.05
	else:
    	# player 1 wins
    	if (current_action == 'rock' and previous_action == 'scissor') or (current_action == 'paper' and previous_action == 'rock') or (current_action == 'scissor' and previous_action == 'paper'):
        	for i in range(3):
            	if i == current_state_index:
                	emission_probabilities[i][i] += 0.1
            	else:
                	emission_probabilities[i][i] -= 0.05
    	# player 2 wins
    	else:
        	for i in range(3):
            	if i == previous_state_index:
                	emission_probabilities[i][i] += 0.1
            	else:
                	emission_probabilities[i][i] -= 0.05

 # normalize emission probabilities
	for i in range(3):
    	total_prob = sum(emission_probabilities[i])
    	for j in range(3):
        	emission_probabilities[i][j] /= total_prob

	next_state_index = current_probability.index(max(current_probability))
	return hidden_states[next_state_index]

previous_action1 = random.choice(['rock', 'paper', 'scissor'])
previous_action2 = random.choice(['rock', 'paper', 'scissor'])
player1_score = 0
player2_score = 0
for i in range(10):
    
	action1 = markov_chain(previous_action1)
	action2 = hmm(previous_action1, previous_action2)
    
	previous_action1 = action2
	previous_action2 = action1
	print(f"Round {i+1}: Player 1 chooses {action1}& Player 2 chooses {action2}")
	if action1 == action2:
    	print("Tie!")
	elif (action1 == 'rock' and action2 == 'scissor') or (action1 == 'paper' and action2 == 'rock') or (action1 == 'scissor' and action2 == 'paper'):
    	print("Player 1 wins!")
    	player1_score += 1
    	# update emission probabilities for player 2
    	current_state_index = hidden_states.index(previous_action2)
    	winner_index = hidden_states.index(action1)
    	total_count = sum(emission_probabilities[winner_index])
    	for i in range(len(emission_probabilities[winner_index])):
        	if i == current_state_index:
            	# update the probability of the current observed state based on the outcome of the game
            	emission_probabilities[winner_index][i] = 0.8 * emission_probabilities[winner_index][i] + 0.2 / total_count
        	else:
            	# update the probabilities of the other observed states
            	emission_probabilities[winner_index][i] = 0.2 / total_count
	else:
    	print("Player 2 wins! ")
    	player2_score += 1
    	# update emission probabilities for player 1
    	current_state_index = hidden_states.index(previous_action1)
    	winner_index = hidden_states.index(action2)
    	total_count = sum(emission_probabilities[winner_index])
    	for i in range(len(emission_probabilities[winner_index])):
        	if i == current_state_index:
            	# update the probability of the current observed state based on the outcome of the game
            	emission_probabilities[winner_index][i] = 0.8 * emission_probabilities[winner_index][i] + 0.2 / total_count
        	else:
            	# update the probabilities of the other observed states
            	emission_probabilities[winner_index][i] = 0.2 / total_count
   	 
	print(f"\nScore: Player 1 ::(\033[1m{player1_score}\033[0m)  &  Player 2 ::(\033[1m{player2_score}\033[0m)\n")

if player1_score > player2_score:
	print("Winner: Player 1👍       	Loser: Player 2👎")
elif player1_score < player2_score:
	print("Winner: Player 2👍       	Loser: Player 1👎")
else:
	print("It's a tie 🤝")

