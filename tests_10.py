import random

total_user_victory = 0
total_comp_victory = 0

while True:

    ROCK = 1
    SCISSORS = 2
    PAPER = 3
    QUIT = 'q'


    user_choice = input('Choice: Rock(1), Scissors (2), Paper(3), Quit("q"):\n')

    if user_choice == QUIT:
        print ('Bye!')
        break

    user_choice = int(user_choice)

    if user_choice == ROCK:
        print('Rock!')

    elif user_choice == SCISSORS:
        print('Scissors!')

    elif user_choice == PAPER:
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

    if comp == user_choice:
        print('Draw!')

    elif comp == SCISSORS and user_choice == ROCK \
            or comp == PAPER and user_choice == SCISSORS\
            or comp == ROCK and user_choice == PAPER:
        print('You won!')

        if total_user_victory < 2:
            total_user_victory += 1
            print('\n\n\n')
            continue
        else:
            print('Game Over!')
        break

    else:
        print('Comp won!')
        if total_comp_victory < 2:
            total_comp_victory += 1
            print('\n\n\n')
            continue
        else:
            print('Game Over!')
        break


    print('\n\n\n')
