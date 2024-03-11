import random
def roll():
    min_val = 1
    max_val = 6
    result = random.randint(min_val, max_val)
    return result
while True:
    players = input("Enter the number of players (2-4) :")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("Let's Play")
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("Invalid input")

max_score = 33
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("Player number", player_idx + 1, "has just started")
        print("Your total score is :", player_scores[player_idx] )
        current_score = 0
        while True:
            should_roll = input("Do you want to play ?(y) : ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done")
                break
            else:
                current_score += value
                print("You rolled a : ", value)
                print("Your current score is : ", current_score)
        player_scores[player_idx] += current_score

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number ", winning_idx + 1, " has won with a score of  ", max_score)
       

