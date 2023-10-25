def hoursPay():
    hours = int(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    difference = 0

    if hours > 40 & hours <= 60:
        difference = hours - 40;
        salary = hours * 1.5
    else:
        salary = hours * rate

    if difference > 0:
        salary = (40 * rate) + (difference * 1.5)

    print(f'Pay: {salary} lv')


hoursPay();