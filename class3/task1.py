#Create a movie ticketing machine, which will output "Sorry you'r not allowed to pass" if their (age<13), "Please call your legal Guardian" (age>=13 and age<18), "Welcome" (age>=18), in a never ending loop. (Hint: Your while condition should always be True)


while True:
    age = int(input("Enter your age: "))
    if age <= 0 or age >= 150:
        print("Invalid age. Please try again.")
    elif age < 13:
        print("Sorry, you're not allowed to pass.")
    elif age < 18:
        print("Please call your legal guardian.")
    else:
        print("Welcome!")
        

