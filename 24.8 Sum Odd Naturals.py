def sumOddNatural(number):
    if number == 1:
        return 1
    
    else:
        return sumOddNatural(number-1) + 2*number-1



print(sumOddNatural(10))