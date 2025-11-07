password = 12345  
attempts = 5  # this is the maximum amount of attempts the user gets to enter the correct password

while attempts > 0:  # the code is looped until password is entered correct or when the attempts run out
    user_input = int(input("Enter your password: "))  
    if user_input == password:  # this checks if the user entered the correct password 
        print("Access granted.")  
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password. {attempts} attempt(s) remaining.")  # informs the user about how many attempts they have remaining 1212
        else:
            print("Maximum attempts reached. Authorities have been alerted.")  # if the maximum amount of attempts is reached then the authortiies are alerted 