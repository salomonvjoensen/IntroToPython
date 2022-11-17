# exercise_4_9.py

"""Temperature conversion from Fahrenheit to Celcius."""

def fahrenheit_to_celcius(temp_range=100):
    """Prints the temperature range for both"""
    print('Celcius\tFahrenheit')

    for celcius in range(temp_range+1):
        print(f'{celcius:>7}\t{((9/5) * celcius + 32):>10.1f}')