import math


def area():
    r = float(input('Side R: '))

    areaInCm = math.pi * r*r
    perimeterInCm = 2 * math.pi * r

    print(f'Area: {round(areaInCm, 3)}')

    print(f'Perimeter: {round(perimeterInCm, 3)}')

area()