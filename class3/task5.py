#create a list ranging from 0..10, then using a for loop iterate through the list, and print out only even numbers not including 0

numbers = list(range(0, 11))

for num in numbers:
    if num != 0 and num % 2 == 0:
        print(num)