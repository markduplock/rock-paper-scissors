import random
import sys


def show_winner(result):
    if result == "player":
        print("You Win!\n\n")
    elif result == "cpu":
        print("You Lose!\n\n")
    else:
        print("It's a draw!\n\n")


def determine_winner(player_input, cpu_choice):
    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    print(f"You chose {player_input}. CPU chose {cpu_choice}")

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
        print("Not a vaild option")


def main():
    while True:
        player_input = get_player_input()
        if player_input == "quit":
            sys.exit(0)
        cpu_choice = get_cpu_choice()
        result = determine_winner(player_input, cpu_choice)
        show_winner(result)


if __name__ == "__main__":
    main()
