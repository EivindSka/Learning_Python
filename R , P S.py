import random


# // Rock, Paper Scissors
# :: Consider Importing Sounds on Computer Choise ::
while True:
    choices = ['Rock', 'Paper', 'Scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Rock, Paper or Scissors?: ').capitalize()

    if player == computer:
        print('Computer: ', computer)
        print('Player: ', player)
        print('Tie!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Lose!')
        if computer == 'Scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Win!')
    elif player == 'Scissors':
        if computer == 'Rock':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Lose!')
        if computer == 'Paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Win!')
    elif player == 'Paper':
        if computer == 'Scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Lose!')
        if computer == 'Rock':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Win!')

    play_again = input('Play Again? (yes/no): ').lower()

    if play_again != 'yes':
        break
print('Good Bye!')
