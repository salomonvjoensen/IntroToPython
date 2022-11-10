# exercise_3_10.py

"""7% Investment Return."""

Investment = 1000
Rate = 0.07

print(f'Year:{" "*18}Savings') # " "*18 prints 18 spaces

for year in range(0, 31):
    savings = Investment * (1 + Rate) ** year    
    print(f'{year:>4}, the savings are: {savings:.2f}')
