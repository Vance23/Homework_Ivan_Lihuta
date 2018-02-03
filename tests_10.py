import random


while True:

    ROCK = 1
    SCISSORS = 2
    PAPER = 3
    QUIT = 4

    user = int(input('Choice: Rock(1), Scissors (2), Paper(3), Quit(4):\n'))

    if user == 4:
        print ('Bye!')
        break

    if user == ROCK:
        print('Rock!')

    elif user == SCISSORS:
        print('Scissors!')

    elif user == PAPER:
        print('Paper!')

    else:
        print('Wrong value! - Try again ->')
        continue

    comp = (random.randint(1, 3))
    print('Comp choice: %d' % (comp))

    if comp == ROCK:
        print('Rock!')

    elif comp == SCISSORS:
        print('Scissors!')

    elif comp == PAPER:
        print('Paper!')

    if comp == user:
        print('Draw!')

    elif comp == SCISSORS and user == ROCK or comp == PAPER and user == SCISSORS or comp == ROCK and user == PAPER:
        print('You won!')

        total_user_victory = 0
        while total_user_victory < 3:
            total_user_victory = total_user_victory + 1
        else:
            print('Game Over!')
        break

    else:
        print('Comp won!')
        total_comp_victory = 0
        while total_comp_victory < 3:
            total_comp_victory = total_comp_victory + 1
        else:
            print('Game Over!')
        break












