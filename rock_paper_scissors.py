import random
from colorama import Fore, Style, init

init()

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

while True:  # рестартира играта
    player_move = input(
        Fore.CYAN + "Choose [r]ock, [p]aper or [s]cissors: " + Style.RESET_ALL
    )

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        continue  # връща към началото на цикъла

    computer_move = random.choice([rock, paper, scissors])

    print(Fore.YELLOW + f"The computer chose {computer_move}." + Style.RESET_ALL)

    if (player_move == rock and computer_move == scissors) or \
       (player_move == paper and computer_move == rock) or \
       (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!" + Style.RESET_ALL)
    elif player_move == computer_move:
        print(Fore.BLUE + "Draw!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "You lose!" + Style.RESET_ALL)

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print(Fore.MAGENTA + "Thanks for playing!" + Style.RESET_ALL)
        break


