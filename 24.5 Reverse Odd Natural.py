def OddNatural(number):
    if number>0:
        print(2*number-1)
        OddNatural(number-1)


OddNatural(10)