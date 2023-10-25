def area():

    a = float(input('Side A: '))
    b = float(input('Side B: '))
    h = float(input('Side H: '))

    areaInCm = (a + b) / 2 * h

    print('Area:')
    print(round(areaInCm, 2))

area()

