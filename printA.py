def print_pattern():
    num = int(input('enter range: '))
    for i in range(num):
        if i == 0:
            print(' *** ')
        elif i == num / 2:
            print('*****')
        else:
            print('*   *')


print_pattern()
