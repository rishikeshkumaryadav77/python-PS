# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to play the game
def play_game():
    player_positions = {"Player 1": 0, "Player 2": 0}
    players = list(player_positions.keys())
    
    while True:
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            dice = roll_dice()
            print(f"{player} rolled a {dice}")
            
            new_position = player_positions[player] + dice
            
            if new_position > 100:
                print(f"{player} rolled too high and stays at {player_positions[player]}")
                continue
            
            # Check for snakes or ladders
            if new_position in snakes:
                print(f"Oops! {player} got bitten by a snake and goes from {new_position} to {snakes[new_position]}")
                new_position = snakes[new_position]
            elif new_position in ladders:
                print(f"Yay! {player} climbed a ladder from {new_position} to {ladders[new_position]}")
                new_position = ladders[new_position]
            
            player_positions[player] = new_position
            print(f"{player} is now at position {new_position}\n")
            
            if new_position == 100:
                print(f"{player} wins the game! 🎉")
                return

# Start the game
play_game()