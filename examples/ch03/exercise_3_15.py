# exercise_3_15.py

"""Challenge: Approximating the Mathematical Constant e."""

e_constant = 1
calculation = 1

while True:
    Precision = input('Precision of e? (1-20) ')

    if Precision.isnumeric():
        Precision = int(Precision)
    else:
        print('Only integer numbers, no text.')
        continue
        
    if Precision in range(1, 21):
        break
    else:
        print('Only print integer values between 1 and 20.')
        continue

print(f'Precision:   e value:')

for outer in range(1, Precision+1, 1):
    print(f'{outer:>9}    {e_constant:<.{outer}f}')

    for inner in range(1, outer+1, 1):
        calculation *= inner
    
    e_constant += 1 / calculation
    calculation = 1