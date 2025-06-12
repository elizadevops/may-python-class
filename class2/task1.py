age=int(input("Enter your age: "))
if age>0 and age<13:
    print("You are Child")
elif age<13 and age<18:
    print("You are Teenager ")
elif age>=18 and age<65:
    print("You are Adult ")
elif age>=65:
    print("You are Elder ")
else:
    print("Provide right age")
