def EvenNatural(number):
    if number>0:
        EvenNatural(number-1)
        print(2*number)


EvenNatural(10)