import random

while True:

    Rock = 1
    Scissors = 2
    Paper = 3

    user = int(input('You choice --> Rock(1), Scissors (2), Paper(3):\n'))

    if user == 1:
        print('Rock!')

    elif user == 2:
        print('Scissors!')

    elif user == 3:
        print('Paper!')

    else:
        print('Wrong value! - Try again -->')
        continue

    comp = (random.randint(1, 3))
    print('Comp choice: %d' % (comp))

    if comp == 1:
        print('Rock!')

    elif comp == 2:
        print('Scissors!')

    elif comp == 3:
        print('Paper!')

    if comp == user:
        print('Draw!')

    elif comp == 2 and user == 1 or comp == 3 and user == 2 or comp == 1 and user == 3:
        print('You wine!')

    else:
        print('Comp wine!')

# пока не правильно прописать ограничение цикла до 3-х побед











