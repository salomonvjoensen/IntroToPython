# exercise_3_9.py

"""
Separating the Digits in an Integer
"""

digit = 0
digit_string = ''
number_as_string = input('Write an integer number: ')
length = len(number_as_string) - 1
number = int(number_as_string)

while length != -1:
    digit = number // (10 ** length)    # get the leftmost digit
    number %= 10 ** length              # 'remove' the leftmost digit
    length += -1


    digit_string += str(digit) + '   '
    # number_as_string += digit_string

print(digit_string)