# exercise_3_6.py

"""
Turing test.
"""

problem = input('What is your problem? ')

while True:
    reply = input('Have you had this problem before (yes or no) (stop to exit)? ')

    if reply == 'yes':
        print('Well, you have it again.')
    elif reply == 'no':
        print('Well, you have it now.')
    elif reply == 'stop':
        break
