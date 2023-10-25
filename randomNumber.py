from random import randint


def randomNum():
    randomNumber = randint(1, 100)
    isRandom = False

    for i in range(3):
        guessedNumber = int(input('Enter number: '))

        if guessedNumber == randomNumber:
            isRandom = True
            break

    if isRandom:
        print('You guessed it!')
    else:
        print(f'The number was: {randomNumber}')


randomNum()
