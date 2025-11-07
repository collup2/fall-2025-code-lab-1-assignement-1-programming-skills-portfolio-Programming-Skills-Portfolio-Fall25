name = input("Enter your full name: ")  # asks the user to enter their FULL name
hometown = input("Enter your hometown: ")
age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    print("My name is", name)
    print("I live in", hometown)
    print("My age is", age)
else:
    print("Invalid age input. Please enter a number next time.")  # if user enters anything other than their age, they get this output
    