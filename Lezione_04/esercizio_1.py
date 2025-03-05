# this is my first exercise with functions
"""Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5."""

def check_value(n:int):
    if n == 5 :
        print(f"{n} è uguale a 5")
    elif n > 5:
        print(f"{n} è maggiore a 5")
    else:
        print(f"{n} è minore di 5")


num=check_value(8)
num2=check_value(5)
num3=check_value(2)
