# exercise_3_12.py

"""Palindromes."""

number = 12321
Palindrome_ask = 'Enter a 5 digit number to determine if it is a palindrome: '
Is_palindrome = 'It is a palindrome.'
Not_palindrome = 'It is not a palindrome.'
Rerun_ask = 'Check for another palindrome? Type \'yes\' to check another: '

while True:
    number = input(Palindrome_ask)

    if len(number) != 5:
        print('Not a 5 digit number.')
        continue
    else:
        number = int(number)

        # remainder after dividing with 10 to get the fifth digit
        fifthdigit = number % 10

        # remainder after dividing with 100 and flooring that with 10
        # to get the fourth digit
        fourthdigit = (number % 100) // 10

        # remainder after dividing with 1000 and flooring that with 100
        # to get the third digit
        thirddigit = (number % 1000) // 100

        # remainder after dividing with 10000 and flooring that with 1000
        # to get the second digit
        seconddigit = (number % 10000) // 1000

        # flooring the number with 10000 to get the first digit
        firstdigit = number // 10000

        if firstdigit == fifthdigit and seconddigit == fourthdigit:
            print(Is_palindrome)
        else:
            print(Not_palindrome)
        
        confirm = input(Rerun_ask)

        if confirm in 'yes':
            continue
        else:
            break
