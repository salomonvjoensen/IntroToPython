# exercise_3_13.py

"""Factorials."""

factorial = int(input('Type positive integer to be factoriezed: '))
calculation = 1

for number in range(1, factorial+1):
    calculation *= number

print(calculation)