def biggest():
    n = int(input('Enter numbers count: '))
    bigggesNum = 0

    for i in range(n):
        currentNum = float(input('Enter number:'))
        if currentNum > bigggesNum:
            bigggesNum = currentNum

    print(f'The biggest numbers is : {bigggesNum}')

biggest()