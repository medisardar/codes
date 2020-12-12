import random

def play(): #have a function
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's']) #The computer will randomly choose

    if user == computer: #if the user & the computer has the same choise then it's a TIE
        return 'It\'s a tie'

    # ROCK breaks SCISSORS / SCISSORS cuts PAPER / PAPER catches rock
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player
    # ROCK breaks SCISSORS / SCISSORS cuts PAPER / PAPER catches rock
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
