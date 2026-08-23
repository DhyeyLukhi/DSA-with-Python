def f1(number):
    return number + f1(number=number-1) if number != 1 else number


print(f1(0))