# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(10):
    # get one exam result
    while True:
        result = int(input('Enter result (1=pass, 2=fail): '))
        
        if result == 1 or result == 2:
            break
        else:
            print('Only type a 1 for pass or a 2 for fail!')
        
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
