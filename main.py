import random


def track_score(result, player_score, cpu_score):
    if result == "player":
        player_score += 1

    if result == "cpu":
        cpu_score += 1

    return player_score, cpu_score


def show_winner(result):
    if result == "player":
        print("You Win!\n")
    elif result == "cpu":
        print("You Lose!\n")
    else:
        print("It's a draw!\n")


def determine_winner(player_input, cpu_choice):
    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if player_input == cpu_choice:
        return "draw"

    if winning_moves[player_input] == cpu_choice:
        return "player"

    return "cpu"


def get_cpu_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)


def get_player_input():
    options = ["rock", "paper", "scissors", "quit"]
    while True:
        player_input = (
            input("Choose: 'rock', 'paper', 'scissors', or 'quit': ").strip().lower()
        )
        if player_input in options:
            return player_input
        print("Not a valid option")


def main():
    player_score = 0
    cpu_score = 0

    while True:
        player_input = get_player_input()
        if player_input == "quit":
            break
        cpu_choice = get_cpu_choice()
        print(f"You chose {player_input}. CPU chose {cpu_choice}")
        result = determine_winner(player_input, cpu_choice)
        show_winner(result)
        player_score, cpu_score = track_score(result, player_score, cpu_score)
        print(f"You: {player_score} | CPU: {cpu_score}\n")


if __name__ == "__main__":
    main()
