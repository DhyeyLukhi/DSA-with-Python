def sumNatural(number):
    if number == 1:
        return 1
    
    else:
        return number + sumNatural(number-1)



print(sumNatural(10))