def sumOddNatural(number):
    if number == 1:
        return 2
    
    else:
        return sumOddNatural(number-1) + 2*number



print(sumOddNatural(1))