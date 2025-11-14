input_string = input()
initial_numbers = list(map(int, input_string.split()))

squared_numbers = []

for num in initial_numbers:
    square = num ** 2
    squared_numbers.append(square) 

print(*squared_numbers, sep=' ')