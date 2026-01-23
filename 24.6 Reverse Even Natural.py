def EvenNatural(number):
    if number>0:
        print(2*number)
        EvenNatural(number-1)


EvenNatural(10)