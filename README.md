# RPS-Game-using-Python
This project aims to implement a rock-paper-scissors game using Python programming language and incorporating Markov models and Hidden Markov Models (HMMs). The game involves two players who each choose one of three options (rock, paper, or scissors), and the winner is determined by a set of rules that dictate which option beats the other. 

In addition to the basic implementation of the game using control flow structures and user input/output functions, Markov models and HMMs are used to improve the game's performance and accuracy. These models allow the computer player to predict the next move of the human player based on the history of previous moves. The Markov models use a probabilistic approach to predict the next move based on the current state and the probabilities of transitioning to different states. On the other hand, the HMMs are more sophisticated models that consider both the current state and the observations (previous moves) to predict the next move. 

The game's implementation involves training the models using a dataset of previous game moves and using the trained models to predict the next move of the human player. The computer player's move is then chosen based on the rules of the game and the predictions of the models. The game's accuracy and performance are evaluated based on the number of games won by the computer player against human players.
The game starts by initializing the transition matrix, which represents the probabilities of transitioning from one state to another in the game. The hidden and observed states are also defined, and the initial, emission, and transition probabilities are initialized. 

The function `markov_chain` generates a random move based on the transition probabilities. The function `hmm` implements the HMM model and predicts the opponent's next move based on the previous moves. The `if` statement updates the emission probabilities based on the result of the game.

The game runs for ten rounds. In each round, both players choose their move based on the previous moves. If both players choose the same move, the round ends in a tie. If one player's move beats the other player's move, the winning player gets a point. The `if` and `else` statements update the emission probabilities for the respective player based on the outcome of the game. 

Finally, the score of each player is displayed. 

Overall, this code uses a Markov model and an HMM to predict the opponent's next move, making the game more challenging and interesting.
