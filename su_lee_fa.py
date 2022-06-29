import random

def game():
    user = input('What is your choice? \n"r" for rock \n"s" for scissors \n"p" for paper \n').lower()
    computer = random.choice(('r', 's', 'p'))

    if user == computer:
        return 'Nobody won. It is a tie. Try again!'

    if winner(user, computer):
        return 'Congratulations! You won!'

    return 'Pity! You lost!'

def winner(player, bot):
    if player == 'r' and bot == 's' or player == 's' and bot == 'p' or player == 'p' and bot == 'r':
        return True

print(game())