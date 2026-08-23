def reverseNatural(number):
    if number == 1:
        print(1)
        return 1
    else:
        print(number)
        return reverseNatural(number-1)





reverseNatural(100)