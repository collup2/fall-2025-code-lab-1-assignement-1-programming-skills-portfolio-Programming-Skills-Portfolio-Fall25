password = 12345

while True:
    user_input = int(input("Enter your password: "))  # user enters the correct password
    if user_input == password:
        print("Access granted.")  # if user enters the correct password
        break
    else:
        print("Incorrect password. Try again.")  # if user enters an invalid password