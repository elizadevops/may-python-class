#print a multiplication table of a number given by the user (eg: inp=5, 5*0=0,5*1=5 5*2=10, ... 5*10=50)

num = int(input("Enter a number: "))

for i in range(11):
    print(f"{num} * {i} = {num * i}")