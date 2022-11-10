# exercise_3_11.py

"""Miles per gallon."""

gallons = 0
miles = 0
average = 0
total_gallons = 0
total_miles = 0

while True:
    gallons = float(input('Enter the gallons used (-1 to end): '))

    if gallons == -1:
        break

    miles = float(input('Enter the miles driven: '))
    print('The miles/gallon for this tank was', miles/gallons)
    total_gallons += gallons
    total_miles += miles

if total_gallons == 0 or total_miles == 0:
    print('The overall average miles/gallon was zero')
else:
    print('The overall average miles/gallon was', total_miles/total_gallons)


