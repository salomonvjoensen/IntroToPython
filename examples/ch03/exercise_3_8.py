# exercise_3_8.py

"""
Arithmetic, Smallest and Largest
"""

length = 0
sum = 0
average = 0
product = 1
smallest = float('inf')
largest = float('-inf')

for x in range(4):
    x = int(input('Enter a number: '))
    length += 1
    sum += x
    product *= x

    if smallest > x:
        smallest = x
    
    if largest < x:
        largest = x

average = sum / length


print(f'The sum of the {length} numbers are {sum}')
print(f'The average is {average}')
print(f'The product of the numbers is {product}')
print('The smallest number entered was', smallest)
print('The largest number entered was', largest)
