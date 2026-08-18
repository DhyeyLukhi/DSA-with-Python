def sumSquareNatural(number):
    if number == 1:
        return 1
    
    else:
        return sumSquareNatural(number-1) + number**2


print(sumSquareNatural(4))