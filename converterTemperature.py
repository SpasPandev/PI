def converter():
    option = int(input('Choose option: Press 1 for celsius -> fahrenheit or 2 for fahrenheit -> celsius: '))

    if option == 1:
        celsius = float(input('Enter celsius: '))
        fahrenheit = (celsius * 9/5) + 32
        print(f'The temperature in fahrenheit is: {fahrenheit}')
    elif option == 2:
        fahrenheit = float(input('Enter fahrenheit: '))
        celsius = (fahrenheit - 32) * 5/9
        print(f'The temperature in celsius is: {celsius}')
    else:
        print('Wrong input!')


converter()
