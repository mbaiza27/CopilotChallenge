#Create a dictionary where "rock" = 1, "paper" = 2, and "scissors" = 3
outcome_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

#Create a dictionary of winning outcomes
winning_outcomes = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

#Establish the players' choices
rok = ["scissors", "paper", "scissors", "rock", "rock"]
paprya = ["rock", "rock", "paper", "scissors", "paper"]

#Initialize the players' scores
rok_score = 0
paprya_score = 0


rounds = min(len(rok), len(paprya))


#Determine the outcome based on the players' choices
for i in range(rounds):
    rok_move = rok[i]
    paprya_move = paprya[i]

    if rok_move == paprya_move:
        continue
    elif winning_outcomes[rok_move] == paprya_move:
        #Rok wins
        rok_score = rok_score + outcome_points[rok_move]
    else:
        #Paprya wins
        paprya_score = paprya_score + outcome_points[paprya_move]

#Print rok_score and paprya_score to console
print("Player 1 score (Rok):", rok_score, "\nPlayer 2 score (Paprya):",  paprya_score)

#Compare rok_score and paprya_score to determine the winner
if rok_score > paprya_score:
    print("Rok wins")
elif rok_score < paprya_score:
    print("Paprya wins")
    