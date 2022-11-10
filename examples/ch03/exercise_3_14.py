# exercise_3_14.py

"""Challenge: Approximating the Mathematical Constant Pi."""

Pi = 4
term = 1
is_minus = True

Precision = int(input('Precision of Pi? '))

print(f'Precision:,  Pi value:')

for calc in range(3, Precision*2+2, 2):

    print(f'{term:>9}    {Pi}')
    term += 1

    if is_minus:
        Pi -= 4 / calc
        is_minus = False
    else:
        Pi += 4 / (calc)
        is_minus = True
    