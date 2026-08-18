def OddNatural(number):
    if number>0:
        OddNatural(number-1)
        print(2*number-1)


OddNatural(10)