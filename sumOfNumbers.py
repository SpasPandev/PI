def sum():
    numbers = input('Enter numbers: ')
    sum = 0
    numbersArr = numbers.split(', ')

    for i in numbersArr:
        sum += int(numbersArr[i])

    print(sum)
sum()