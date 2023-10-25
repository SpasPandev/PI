def evenOrOdd():
    num = int(input('Enter Number: '))

    if num == 0:
        print('0 is neither even nor odd')
    elif num % 2 == 0:
        print('Even')
    else:
        print('Odd')


evenOrOdd()