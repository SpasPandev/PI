def leapYear():
    year = int(input('Enter year: '))
    if year % 4 == 0:
        print('Yes, the year is leap')
    else:
        print('No, the year is not leap')

leapYear()