def numbers():
    start = int(input('Enter start of range: '))
    end = int(input('Enter end of range: '))

    for i in range(start, end):
        if int(i) % 7 == 0 and int(i) % 5 == 0:
            print(i)


numbers()
