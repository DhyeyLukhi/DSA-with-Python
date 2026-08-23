def natural(number):
    if number == 1:
        return 1
    else:
        print(natural(number-1))
        return number
    

print(natural(100))