# Using the while loop keep asking the user to input an integer value till the sum of those values reaches 100 or above. Dont forget to store all those values and print the condition was met (Hint: Use a list to store all the values)
sum = 0
list1 = []

while sum < 100:
    num = int(input("Enter an number: "))
    sum += num   #sum=sum=num
    list1.append(num)

print("The condition was met! The total is", list1)